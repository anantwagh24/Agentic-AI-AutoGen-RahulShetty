import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main():
    model_client= OpenAIChatCompletionClient(model='gtp-4o')
    assistant =AssistantAgent(name="Assistant", model_client=model_client)

    await Console(assistant.run_stream(task="What is 25 * 8?"))
    await model_client.close()

asyncio.run(main())

