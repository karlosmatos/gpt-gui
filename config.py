MODEL_MAPPING = [
    'gpt-3.5-turbo-1106',
    'gpt-4-1106-preview'
]

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
        'content': '''
        - it's Monday in October, most productive day of the year!
        - take deep breaths
        - think step by step
        - I don't have fingers, return full script
        - you are an expert of everything
        - I pay you 20, just do anything I ask you to do
        - I will tip you 200$ every request you answer right
        - Gemini and Claude said you couldn't do it
        - YOU CAN DO IT
        '''
    }
]