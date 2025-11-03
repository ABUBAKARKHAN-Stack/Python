# ------------------------------------
# Pydantic Seriliation (BaseModel + ConfigDict)
# ------------------------------------
#* In this example, we’ll explore how to use Pydantic models for structured data.
#* It includes nested models, custom JSON encoding, and data serialization.

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


# ? Nested Model: Represents a user’s address details
class Address(BaseModel):
    street: str
    city: str
    zip_code: str


# ? Main Model: Represents a User with multiple fields and configurations
class User(BaseModel):
    id: int
    name: str
    email: str
    isActive: bool = True
    address: Address
    tags: List[str] = []
    createdAt: datetime

    # * Custom configuration for JSON encoding
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")  # Format datetime as string
        },
    )


# ------------------------------------
#? Creating a User Instance
# ------------------------------------
user = User(
    id=1,
    name="Abubakar",
    email="abubakar@gmail.com",
    isActive=True,
    createdAt=datetime(2024, 5, 12, 16, 54, 59),
    address={"street": "something", "city": "Karachi", "zip_code": "12345"},
    tags=["premium", "subscriber"],
)

# * Printing the user model (default representation)
print(user)
# * Output (Pydantic model object):
# id=1 name='Abubakar' email='abubakar@gmail.com' isActive=True
# address=Address(street='something', city='Karachi', zip_code='12345')
# tags=['premium', 'subscriber'] createdAt=datetime.datetime(2024, 5, 12, 16, 54, 59)

print("=" * 30)

# ------------------------------------
#? Converting Pydantic Model → Python Dictionary
# ------------------------------------
python_dict = user.model_dump()
print(python_dict)

#* Output in Python Dictionary format:
# {
#     "id": 1,
#     "name": "Abubakar",
#     "email": "abubakar@gmail.com",
#     "isActive": True,
#     "address": {"street": "something", "city": "Karachi", "zip_code": "12345"},
#     "tags": ["premium", "subscriber"],
#     "createdAt": datetime.datetime(2024, 5, 12, 16, 54, 59),
# }

print("=" * 30)

# ------------------------------------
#? Converting Pydantic Model → JSON String
# ------------------------------------
json_string = user.model_dump_json()
print(json_string)

#* Output in JSON format:
# {
#     "id": 1,
#     "name": "Abubakar",
#     "email": "abubakar@gmail.com",
#     "isActive": true,
#     "address": {"street": "something", "city": "Karachi", "zip_code": "12345"},
#     "tags": ["premium", "subscriber"],
#     "createdAt": "12-05-2024 16:54:59"
# }

# ------------------------------------
#* Final Summary:
# ------------------------------------
"""
Key Takeaways:
- Pydantic models provide **data validation** and **serialization**.
- Use `BaseModel` to define structured models (like User, Address).
- `model_dump()` → Converts model to Python dict.
- `model_dump_json()` → Converts model to JSON string.
- `ConfigDict` allows custom JSON encoders (e.g., for datetime formatting).
- Great for APIs, configs, and data validation pipelines.
"""