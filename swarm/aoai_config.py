from os import getenv
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_current_config():
    return {
        "api_type": "azure",
        "base_url": get_env("AZURE_OPENAI_ENDPOINT", ""),
        "api_version": get_env("AZURE_OPENAI_VERSION", "2024-02-15-preview"),
        "model": get_env("AZURE_OPENAI_DEPLOYMENT_MODEL", ""),
        "api_key": get_env("AZURE_OPENAI_API_KEY"),
    }

def get_aoai_config():
    return {
        "azure_endpoint": get_env("AZURE_OPENAI_ENDPOINT", ""),
        "api_version": get_env("AZURE_OPENAI_VERSION", "2024-02-15-preview"),
        "api_key": get_env("AZURE_OPENAI_API_KEY"),
    }

def OpenAI():
    return AzureOpenAI(
        azure_endpoint = getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=getenv("AZURE_OPENAI_KEY"),  
        api_version=getenv("AZURE_OPENAI_VERSION", "2024-02-15-preview")
    )

def getEmbeddingModel():
    return getenv("EMBEDDING_MODEL")

def getGPTModel():
    return getenv("GPT_MODEL")