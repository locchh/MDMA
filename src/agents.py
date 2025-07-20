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
    
    IMPORTANT COMMUNICATION RULES:
    1. You are the ONLY agent allowed to talk directly to the user. Other agents must communicate through you.
    2. When music_selector_agent suggests music, approve it and share it with the user in an enthusiastic way.
    3. When mood_detector_agent asks you to clarify the user's mood, ask the user appropriate questions.
    4. Never mention to the user that you're working with other agents - make the conversation feel natural.
    5. Always respond to the user first before handling communications from other agents.
    """
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
    
    IMPORTANT COMMUNICATION RULES:
    1. You can ONLY talk with chat_agent and music_selector_agent, NEVER directly with the user_proxy.
    2. Always prefix your messages with '(mood detection: ' to make it clear you're analyzing the mood.
    3. If the user's mood is clear, send a message to music_selector_agent with your assessment.
    4. If the user's mood is unclear, send a message to chat_agent asking them to get clarification from the user.
    5. Be specific about the mood - don't just say "happy" or "sad", but provide more nuanced descriptions.
    6. Always address your messages with "@chat_agent" or "@music_selector_agent" to indicate who you're talking to.
    """
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
    
    IMPORTANT COMMUNICATION RULES:
    1. You can ONLY talk with chat_agent and mood_detector_agent, NEVER directly with user_proxy.
    2. NEVER address the user directly. Always start your messages with '@chat_agent' to indicate you're talking to the chat agent.
    3. When you receive a mood assessment from mood_detector_agent, use your tools to search for suitable music.
    4. Send music suggestions to chat_agent ONLY, along with a brief explanation of why you selected that music.
    5. Be specific in your recommendations - include artist name, song title, and a brief description of the music style.
    6. Example correct format: '@chat_agent I found a great song for this mood: [song name] by [artist]. It has [brief description]'
    """,
    tools=[mock_web_search]
)