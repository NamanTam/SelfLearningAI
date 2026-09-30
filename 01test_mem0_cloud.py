import os
from dotenv import load_dotenv
from mem0 import MemoryClient

# Load API key from .env
load_dotenv('.env')

api_key = os.getenv("MEM0_API_KEY")

# Connect to hosted Mem0 Platform
client = MemoryClient(api_key=api_key)

# user_id = "naman_test"

messages = [
    {
        "role": "user",
        "content": "Hi, I'm Naman. I like to build AI automations!.",
    },
    {
        "role": "assistant",
        "content": "Hello Naman! I've noted that you like to build AI automations!. I'll keep this in mind for any AI automation related recommendations or discussions.",
    },
]

client.add(messages, user_id='default_user')
#
query = "What shall we build today?"
# 2. Search hosted memories
response = client.search(
    query,
    filters={"user_id": "default_user"}
)

print(response)

