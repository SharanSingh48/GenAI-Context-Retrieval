import requests
from datetime import datetime, timedelta

CHAT_API_URL = "http://localhost:8000/chat"

now = datetime.now()

messages = [
    {
        "session_id": "session_1",
        "role": "user",
        "content": "What are embeddings?",
        "timestamp": (now - timedelta(days=4)).isoformat()
    },
    {
        "session_id": "session_1",
        "role": "assistant",
        "content": "Embeddings are vector representations of text used for semantic similarity.",
        "timestamp": (now - timedelta(days=4, minutes=-1)).isoformat()
    },
    {
        "session_id": "session_2",
        "role": "user",
        "content": "How does semantic search work?",
        "timestamp": (now - timedelta(days=2)).isoformat()
    },
    {
        "session_id": "session_2",
        "role": "assistant",
        "content": "Semantic search uses embeddings to retrieve results based on meaning rather than keywords.",
        "timestamp": (now - timedelta(days=2, minutes=-1)).isoformat()
    },
    {
        "session_id": "session_3",
        "role": "user",
        "content": "We need to improve chat context retrieval for our LLM.",
        "timestamp": (now - timedelta(days=1)).isoformat()
    },
    {
        "session_id": "session_3",
        "role": "assistant",
        "content": "Ranking messages by semantic similarity and recency can improve context selection.",
        "timestamp": (now - timedelta(days=1, minutes=-1)).isoformat()
    }
]

for message in messages:
    response = requests.post(CHAT_API_URL, json=message)
    if response.status_code == 200:
        print(f"Inserted: {message['content']}")
    else:
        print(f"Failed to insert: {message['content']} | Status: {response.status_code}")
