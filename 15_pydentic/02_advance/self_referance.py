from typing import List, Optional
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    content: str
    # Self Referancing the Comment Model
    replies: Optional[List["Comment"]] = None


#* Forward Referances
Comment.model_rebuild()

comment = Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(
            id=3, content="reply 2", replies=[Comment(id=4, content="Nested Reply")]
        ),
    ],
)

print(comment.model_dump()) #? For Better Printing (it gives output in **python dictionary** format)
