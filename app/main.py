import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .database import get_stored_posts, store_posts
from .schemas import Post, PostCreate
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/posts")
async def get_posts():
    await asyncio.sleep(1.5) 
    posts = await get_stored_posts()
    return {"posts": posts}

@app.get("/posts/{post_id}")
async def get_post(post_id: str):
    posts = await get_stored_posts()
    post = next((post for post in posts if post["id"] == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts", status_code=201)
async def create_post(post: PostCreate):
    posts = await get_stored_posts()
    if not isinstance(posts, list):
        raise HTTPException(status_code=500, detail="Internal server error: posts should be a list")
    new_post = post.dict()
    new_post["id"] = str(uuid.uuid4())
    posts.append(new_post)
    await store_posts(posts)
    return new_post