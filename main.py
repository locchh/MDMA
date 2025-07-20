from asyncio import run
from dotenv import load_dotenv
load_dotenv()

from autogen_agentchat.agents import UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from src.agents import music_selector_agent

async def main():
    
    # User Proxy Agent
    user_proxy = UserProxyAgent("user_proxy")

    # Termination Condition
    termination = TextMentionTermination("exit", sources=[user_proxy])

    # Team
    team = RoundRobinGroupChat(
        [music_selector_agent, user_proxy],
        termination_condition=termination
    )

    # Console
    await Console(team.run_stream(task="Find some music for me"))



if __name__ == "__main__":
    run(main())
