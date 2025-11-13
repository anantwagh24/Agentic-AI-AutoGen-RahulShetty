import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient
from playwright.sync_api import sync_playwright


# Browser Automation Tool (function)
def open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.wait_for_timeout(5000)
        browser.close()


async def main():
    model_client = OllamaChatCompletionClient(model="mistral",
                                              base_url="http://localhost:11434")

    assistant = AssistantAgent(
        name="browser_agent",
        model_client=model_client,
        tools=[open_browser]   # ✅ Expose tool
    )

    await Console(
        assistant.run_stream(task="Open Google in the browser")
    )

    await model_client.close()


asyncio.run(main())
