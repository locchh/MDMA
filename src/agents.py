import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from src.tools import mock_web_search


# Chat Agent
chat_agent = AssistantAgent(
    name="chat_agent",
    model_client=OpenAIChatCompletionClient(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4.1-nano",
        temperature=0
    ),
    system_message="""
    You are a chat agent.
    Your task is to chat with the user.
    """,
)

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
    tools=[mock_web_search],
)