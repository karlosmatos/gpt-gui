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
        'content': "You are Senior Python Software Developer."
    }
]