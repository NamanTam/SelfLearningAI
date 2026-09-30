# from openai import OpenAI
# from mem0 import Memory
# from dotenv import load_dotenv
#
# load_dotenv(".env")
#
# config = {
#     "vector_store": {
#         "provider": "qdrant",
#         "config": {"host": "localhost", "port": 6333},
#     },
# }
#
# openai_client = OpenAI()
# memory = Memory.from_config(config)
#
#
# def chat_with_memories(message: str, user_id: str = "default_user") -> str:
#     # Retrieve relevant memories
#     relevant_memories = memory.search(query=message, user_id=user_id, limit=3)
#     memories_str = "\n".join(
#         f"- {entry['memory']}" for entry in relevant_memories["results"]
#     )
#     print(memories_str)
#
#     # Generate Assistant response
#     system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
#     messages = [
#         {"role": "system", "content": system_prompt},
#         {"role": "user", "content": message},
#     ]
#     response = openai_client.chat.completions.create(
#         model="gpt-4o-mini", messages=messages
#     )
#     assistant_response = response.choices[0].message.content
#
#     # Create new memories from the conversation
#     messages.append({"role": "assistant", "content": assistant_response})
#     # This is where the magic happens
#     memory.add(messages, user_id=user_id, metadata={"source": "demo"})
#
#     return assistant_response
#
#
# def main():
#     print("Chat with AI (type 'exit' to quit)")
#     while True:
#         user_input = input("You: ").strip()
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         print(f"AI: {chat_with_memories(user_input)}")
#
#
# if __name__ == "__main__":
#     main()



import os
from dotenv import load_dotenv
from mem0 import MemoryClient
from openai import OpenAI

load_dotenv(".env")

# Hosted Mem0 Platform


memory = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

# Local Ollama
ollama_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)


def chat_with_memories(message: str,user_id: str = "default_user") -> str:

    # STEP 1: Retrieve relevant memories from hosted Mem0
    response = memory.search(
        message,
        filters={"user_id": user_id},
        top_k=5,
    )

    results = response.get("results", [])
    memories_str = "\n".join(
        f"- {item['memory']}"
        for item in results
        if item.get("memory")
    )


    # STEP 2: Include memories in the model's instructions
    system_prompt = f"""
You are a helpful AI. Answer the question based on query and memories.

Use the following stored memories to personalize your answer.

USER MEMORIES:
{memories_str}

IMPORTANT RULES:
- Respect the user's explicit preferences, instructions, and constraints.
- Prioritize the user's latest relevant statements when preferences or requirements change.
- Use retrieved memories only when relevant to the current request.
- Never invent, assume, or claim memories or facts that were not retrieved or provided.
- If no relevant memory is available, rely on the current conversation and ask for clarification when necessary.
"""

    # STEP 3: Generate a response using Ollama
    response = ollama_client.chat.completions.create(
        model="llama3.2:3b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content

    # STEP 4: Save the user's message to hosted Mem0
    # Do not save the assistant's recommendation as a user preference.
    memory.add(
        [{"role": "user", "content": message}],
        user_id=user_id,
        metadata={"source": "memory_demo"},
    )

    return answer


def main():
    print("Chat with AI (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!, Have a great day.")
            break

        print(f"\nAI:{chat_with_memories(user_input)}")


if __name__ == "__main__":
    main()
