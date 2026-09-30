import os
from dotenv import load_dotenv
from mem0 import MemoryClient

load_dotenv(".env")

# Connect to hosted Mem0 Platform
client = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

user_id = "default_user"

messages = [
    {
        "role": "user",
        "content": "I'm planning to watch a movie tonight. Any recommendations?",
    },
    {
        "role": "assistant",
        "content": "How about a thriller movie? They can be quite engaging.",
    },
    {
        "role": "user",
        "content": "I'm not a big fan of thriller movies, but I love sci-fi movies.",
    },
    {
        "role": "assistant",
        "content": "Got it! I'll n ot suggest thriller recommendations and suggest sci-fi movies in the future.",
    },
]

# Store the conversation on Mem0 Platform
add_result = client.add(
    messages,
    user_id=user_id,
    metadata={"category": "movie_recommendations"},
)

print("Add result:")
print(add_result)

# Search hosted memories
search_result = client.search(
    "what movies should I watch today?",
    filters={"user_id": user_id},
)

print(search_result)
