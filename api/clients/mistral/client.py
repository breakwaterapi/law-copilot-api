from mistralai.client import Mistral

def init_mistral_client(api_key):
    return Mistral(api_key=api_key)