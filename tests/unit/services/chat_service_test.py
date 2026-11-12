from unittest.mock import patch
from mistralai.client.models import AssistantMessage, ChatCompletionResponse, ChatCompletionChoice, UsageInfo

from api.init import init
from api.services.chat_service import ChatService

chat_service:ChatService = init()["chat_service"]
def test_chat():
    mock_mistral_return = ChatCompletionResponse(
        id='00ecbb59eb5049ad92c4c0ff2627b06a', 
        object='chat.completion', 
        created=1722004932, 
        model='open-mixtral-8x22b', 
        choices=[ChatCompletionChoice(
            index=0, 
            message=AssistantMessage(
                role='assistant', 
                content="This is a mock response.",
                tool_calls=None
            ),
            finish_reason='stop'
        )], 
        usage=UsageInfo(
            prompt_tokens=5, 
            total_tokens=42, 
            completion_tokens=37
        )
    )
    test_messages = [{"isUser": True, "message": "Test"}]
    with patch("api.clients.mistral.MistralChatClient.chat", return_value=mock_mistral_return):
        assert(chat_service.chat_completion(messages=test_messages)) == "This is a mock response."
