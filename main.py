import warnings
warnings.filterwarnings("ignore")

from asyncio import run
from dotenv import load_dotenv
load_dotenv()

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from src.agents import chat_agent
from autogen_agentchat.agents import UserProxyAgent
import asyncio
from autogen_core import CancellationToken
from typing import Optional


async def spaced_input_handler(prompt: str, cancellation_token: Optional[CancellationToken] = None) -> str:
    """Input handler that adds proper spacing before the prompt"""
    # Small delay to ensure previous output is fully flushed
    await asyncio.sleep(0.1)
    # Add spacing before the prompt to separate it from previous output
    print(prompt, end="", flush=True)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input)


async def main():
    
    termination = TextMentionTermination("EXIT")

    user_proxy = UserProxyAgent(
        name="user_proxy",
        input_func=spaced_input_handler
    )

    # Team
    team = RoundRobinGroupChat(
        [user_proxy, chat_agent],
        termination_condition=termination
    )

    # Console
    stream = team.run_stream()
    
    await Console(stream)

if __name__ == "__main__":

    run(main())