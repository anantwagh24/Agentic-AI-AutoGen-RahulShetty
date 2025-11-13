import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient   # ✅ CHANGE HERE
from sympy.physics.units import temperature


async def main1():
    print("I am inside function")

    # ✅ Use local Ollama model (no API key needed)
    model_client = OllamaChatCompletionClient(
        model="mistral",         # or "llama3", "llama2", "phi3", "gemma"
        base_url="http://localhost:11434", temperature=0  # default Ollama endpoint
    )

    assistant = AssistantAgent(
        name="assistant",
        model_client=model_client  )

    await Console(
        assistant.run_stream(task="What is 25 * 25 ?")
    )

    await model_client.close()

asyncio.run(main1())
