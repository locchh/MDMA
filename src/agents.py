import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from src.tools import web_search

# Chat Agent


# Mood Detector Agent


# Music Selector Agent
music_selector_agent = AssistantAgent(
    name="music_selector_agent",
    model_client=OpenAIChatCompletionClient(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4.1-nano",
        temperature=0
    ),
    system_message="""
    You are a music selector agent.
    Your task is to select music based on the user's mood.
    """,
    tools=[web_search],
    reflect_on_tool_use=True
)