from api.clients.mistral.client import init_mistral_client
from mistralai.client import Mistral

class MistralChatClient:
    def __init__(self, api_key):
        self.client:Mistral = init_mistral_client(api_key=api_key)
    
    def chat(self, model, messages):
        return self.client.chat.complete(model=model, messages=messages)

