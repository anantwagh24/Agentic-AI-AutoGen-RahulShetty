import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient
from langchain_community.llms.openai import OpenAIChat
from sympy.physics.units import temperature


async def main():
    model_client = OllamaChatCompletionClient(model="mistral",
                                              base_url="http://localhost:11434", temperature=0)

    assistant=AssistantAgent(name="anangAgent", model_client=model_client)

    await Console(assistant.run_stream(task="why Delhi is capital of India"))

    await assistant.close()
    await model_client.close()

asyncio.run(main())