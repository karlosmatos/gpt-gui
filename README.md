# GPT-GUI

GPT-GUI is a Python application that provides a graphical user interface for interacting with OpenAI's GPT models. It uses the Streamlit library for the UI and the OpenAI API for generating responses.


https://github.com/karlosmatos/gpt-gui/assets/105454484/5a965fac-8fec-433c-8634-3f3396c1a549


## Installation

1. Clone the repository and move to the project directory.

```
git clone https://github.com/karlosmatos/gpt-gui.git
cd gpt-gui
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage

1. Set your OpenAI API key in the .env file:
```
OPENAI_API_KEY='your key'
```

2. Run the application:
```
python -m streamlit run app.py
```

## Features
- Choose between different GPT models.
- Maintain a chat history with the AI.
- Calculate the cost of the conversation based on the number of tokens used.

## Testing
Tests are located in the tests/ directory. You can run them using pytest:

```
pytest tests
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENCE) file for details.
