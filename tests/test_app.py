import pytest
from unittest.mock import patch, MagicMock
from app import GPTChat

# Mock the streamlit module
@pytest.fixture
def mock_st():
    with patch('app.st') as mock:
        yield mock

# Test initialization of the GPTChat class
def test_init(mock_st):
    api_key = "test_api_key"
    gpt_chat = GPTChat(api_key)
    mock_st.set_page_config.assert_called_once_with(page_title='Chat', page_icon='💬')
    assert gpt_chat.client is not None

# Test reset_conversation method
def test_reset_conversation(mock_st):
    api_key = "test_api_key"
    gpt_chat = GPTChat(api_key)
    gpt_chat.reset_conversation()
    assert mock_st.session_state['total_cost'] == 0.0

# Test generate_response method
def test_generate_response():
    api_key = "test_api_key"
    gpt_chat = GPTChat(api_key)
    response, usage = gpt_chat.generate_response("Hello", "gpt-3.5-turbo-1106")
    assert response == "Mocked response"
    assert usage.total_tokens == 30

# Test calculate_cost method
def test_calculate_cost():
    api_key = "test_api_key"
    gpt_chat = GPTChat(api_key)
    usage = MagicMock(prompt_tokens=10, completion_tokens=20)
    cost = gpt_chat.calculate_cost("gpt-3.5-turbo-1106", usage)
    assert cost == (10 * 0.001 / 1000 + 20 * 0.002 / 1000)

