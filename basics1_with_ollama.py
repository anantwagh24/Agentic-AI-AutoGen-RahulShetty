import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():

    model_client= OllamaChatCompletionClient(model="mistral", base_url="https://localhost:11434")

    assistnat= AssistantAgent(name="personal", model_client=model_client)

    await Console(assistnat.run_stream(task="what is 25*10"))
    await model_client.close()

asyncio.run(main())

