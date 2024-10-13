from swarm import Swarm, Agent
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client = Swarm()

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
