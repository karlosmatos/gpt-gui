import os
import json
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Constants
API_KEY = os.getenv('OPENAI_API_KEY')  # Replace with your API key
MODEL_MAPPING = {
    'gpt-3.5-turbo-1106': 'gpt-3.5-turbo-1106',
    'gpt-4-1106-preview': 'gpt-4-1106-preview'
}
COST_PER_TOKEN = {
    'gpt-3.5-turbo-1106': {
        'prompt': 0.001 / 1000,
        'completion': 0.002 / 1000
    },
    'gpt-4-1106-preview': {
        'prompt': 0.01 / 1000,
        'completion': 0.03 / 1000
    }
}
DEFAULT_MESSAGES = [
    {
        'role': 'system', 
        'content': """
        You are Senior Python Software Developer.
        """
    }
]

class WizardChat:
    def __init__(self, api_key):
        st.set_page_config(page_title='Chat', page_icon='')
        self.client = OpenAI(api_key=api_key)
        self.initialize_session_state()

    def initialize_session_state(self):
        for key, value in {
            'generated': [],
            'past': [],
            'messages': DEFAULT_MESSAGES.copy(),
            'model_name': [],
            'cost': [],
            'total_tokens': [],
            'total_cost': 0.0
        }.items():
            st.session_state.setdefault(key, value)

    @staticmethod
    def reset_conversation():
        st.session_state.update({
            'generated': [],
            'past': [],
            'messages': DEFAULT_MESSAGES.copy(),
            'model_name': [],
            'cost': [],
            'total_tokens': [],
            'total_cost': 0.0
        })

    def generate_response(self, prompt, model_name):
        st.session_state['messages'].append({'role': 'user', 'content': prompt})
        model = MODEL_MAPPING[model_name]

        completion = self.client.chat.completions.create(
            model=model,
            messages=st.session_state['messages'],
            temperature=0,
        )
        response = completion.choices[0].message.content
        st.session_state['messages'].append({'role': 'assistant', 'content': response})

        return response, completion.usage
                        
    # Add a new method to the WizardChat class
    def process_user_input(self, user_input, model_name):
        output, usage = self.generate_response(user_input, model_name)
        return output, usage
    
    @staticmethod
    def calculate_cost(model_name, usage):
        return (usage.prompt_tokens * COST_PER_TOKEN[model_name]['prompt'] +
                usage.completion_tokens * COST_PER_TOKEN[model_name]['completion'])

    @staticmethod
    def display_chat_history(response_container):
        with response_container:
            for user_message, ai_message in zip(st.session_state['past'], st.session_state['generated']):
                st.chat_message(name='user', avatar='🧑').markdown(user_message)
                st.chat_message(name='ai', avatar='🧙‍♂️').markdown(ai_message)

    def chat_demo(self):
        st.markdown('# Chat', unsafe_allow_html=True)

        st.sidebar.text_input('Conversation Name', key='conversation_name')
        model_name = st.sidebar.radio('Choose a model:', list(MODEL_MAPPING.keys()))
        counter_placeholder = st.sidebar.empty()
        counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
        if st.sidebar.button('Clear Conversation', key='clear'):
            self.reset_conversation()

        if (user_input := st.chat_input(placeholder='Type your message here...', key='input')):
            output, usage = self.process_user_input(user_input, model_name)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            st.session_state['total_tokens'].append(usage.total_tokens)

            cost = self.calculate_cost(model_name, usage)
            st.session_state['cost'].append(cost)
            st.session_state['total_cost'] += cost

        self.display_chat_history(st.container())
        counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")

if __name__ == '__main__':
    wizard_chat = WizardChat(API_KEY)
    wizard_chat.chat_demo()