from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    imageUrl: Optional[str] = None

cart_data = {
    "user_id": 1,
    "items": ["Laptop","Mouse","Keyboard"],
    "quantities": {
        "laptop":10,
        "mouse":3,
        "keyboard":20
    }
}

cart = Cart(**cart_data)

print(f"Cart: {cart}")


python_post = BlogPost(title="What is python?",content="Python is a single threaded programming language",imageUrl="https://upsplash.com/python.png")

print("Python Post",python_post)