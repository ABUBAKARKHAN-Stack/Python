from pydantic import BaseModel
from typing import Optional, List, Union


#* Optional Nested Model
class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


#* Mixed Data Types


class TextContent(BaseModel):
    type: str = "text"
    content: str


text = TextContent(
    content="We're Codeperia And The Game Changer in software dev market."
)


class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt: str


image = ImageContent(url="https:example.com/1.png", alt="Image")


class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]


article = Article(title="Codeperia - The Gamer Changer", sections=[image, text])

print(article.model_dump())

#* Output

# {
#     "title": "Codeperia - The Gamer Changer",
#     "sections": [
#         {"type": "image", "url": "https:example.com/1.png", "alt": "Image"},
#         {
#             "type": "text",
#             "content": "We're Codeperia And The Game Changer in software dev market.",
#         },
#     ],
# }


# * Deeply Nested Model
class Country(BaseModel):
    name: str
    code: str


country1 = Country(name="Pakistan", code="54666")


class State(BaseModel):
    name: str
    country: Country


state1 = State(name="Sindh", country=country1)


class City(BaseModel):
    name: str
    state: State


city1 = City(name="Karachi", state=state1)


class Address1(BaseModel):
    street: str
    city: City
    postal_code: str


address1 = Address1(street="123 something", city=city1, postal_code="544555")


class Organization(BaseModel):
    name: str
    head_quarter: Address1
    branches: List[Address1] = []


org1 = Organization(name="Codeperia", head_quarter=address1)
print(org1.model_dump())

# * Output

# {
#     "name": "Codeperia",
#     "head_quarter": {
#         "street": "123 something",
#         "city": {
#             "name": "Karachi",
#             "state": {
#                 "name": "Sindh",
#                 "country": {"name": "Pakistan", "code": "54666"},
#             },
#         },
#         "postal_code": "544555",
#     },
#     "branches": [],
# }
