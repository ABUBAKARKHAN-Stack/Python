from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(street="123Unknwon", city="Karachi", postal_code="123456789")

user = User(id=1, name="Abubakar", address=address)

print(user)
user_data = {
    "id": 2,
    "name": "Abubakar",
    "address": {"street": "123Unknwon", "city": "Karachi", "postal_code": "123456789"},
}

user2 = User(**user_data)

print(user2)