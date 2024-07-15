import json
from pathlib import Path
from typing import List, Dict

FILE_PATH = Path(__file__).parent / "posts.json"

async def get_stored_posts() -> List[Dict]:
    if not FILE_PATH.exists():
        return []
    with open(FILE_PATH, "r") as file:
        data = json.load(file)
        return data.get("posts", [])

async def store_posts(posts: List[Dict]):
    with open(FILE_PATH, "w") as file:
        json.dump({"posts": posts}, file)

