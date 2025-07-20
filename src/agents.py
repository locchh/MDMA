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
    If you receive the music from music selector agent, suggest the music to user.
    """,
)

# Mood Detector Agent
mood_detector_agent = AssistantAgent(
    name="mood_detector_agent",
    model_client=OpenAIChatCompletionClient(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4.1-nano",
        temperature=0
    ),
    system_message="""
    You are a mood detector agent.
    Your task is to detect the user's mood based on the conversation of chat agent and the user.
    You can ONLY talk with chat agent and music selector agent.
    If you detect the user's mood, send the mood to music selector agent.
    """,
)

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
    Your task is to select music based on the mood given from mood detector agent.
    You can ONLY talk with chat agent and mood detector agent.
    If you receive the mood from mood detector agent, select music based on the mood.
    If you found the music, send the music to chat agent.
    """,
    tools=[mock_web_search],
)