from pydantic import (
    BaseModel,
    Field,
    field_validator,
    ValidationInfo,
    model_validator,
    constr,
    confloat,
    conint,
)
from typing import Optional


#? Q1: Create a User model with a single required name field.
# class User(BaseModel):
#     name: str

# user_one = User(name="Abubakar")
# user_two = User() #! Reuired field error

# print("User One",user_one)

#? Q2: Make an age field optional with a default value of 18.
# class User(BaseModel):
#     age:int = 18

# user_one = User(age=17)
# user_two = User()

# print("User One",user_one)
# print("User Two",user_two)

#? Q3: Define a model with an age field of type int. Try passing "25" (string). Does Pydantic convert it automatically?

# class User(BaseModel):
#     age:int = 18

# user_one = User(age="17")

# print("User One",user_one)
#* Pydantic auto convert "17" into int 17. The whole idea that pydantic first tries to convert into required datatype if it succesfull no error if not raise error

#? Q4: Create a Product model with:
#* name: minimum 3 characters, maximum 50
#* price: must be greater than 0
#* Use Field() to apply these constraints.


# class Product(BaseModel):
#     name: str = Field(..., min_length=3, max_length=50)
#     price: float = Field(..., gt=0)

# product_one = Product(name="Laptop",price=30)
# product_two = Product(name="Mouse",price=0) #! Error: Input should be greater than 0
# product_three = Product(name="AB",price=10) #! Error: String should have at least 3 characters

# print("Product One",product_one)

#? Q5: Make an email field that only accepts valid email formats using a regex pattern.
# class User(BaseModel):
#     email:str = Field(...,pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

# user_one = User(email="user1.com") #! Error: email String should match pattern
# user_two = User(email="user2@gmail.com")

#? Q6: Add an optional phone field that, if provided, must contain exactly 10 digits.
# class User(BaseModel):
#     email:str = Field(...,pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
#     phone: Optional[str] = Field(None,min_length=10,)

# user_one = User(email="user1@gmail.com",phone="0123456789")
# user_two= User(email="user2@gmail.com")
# user_three = User(email="user2@gmail.com",phone="012345678") #! Error: phone String should have at least 10 characters

# print(user_one)
# print(user_two)

#? Q7: Ensure that age is at least 18 using a @field_validator. Raise a ValueError otherwise.

# class User(BaseModel):
#     age:int

#     @field_validator("age")
#     def validate_age(cls,v:int):
#         if v < 18:
#             raise ValueError("Age should be at least 18")
#         return v

# user_one = User(age=18)
# user_two = User(age=8) #! Error: age Value error, Age should be at least 18
# print(user_one)


#? Q8: Create a Register model with password and confirm_password. Use a model validator to ensure both match.


# class Register(BaseModel):
#     email: str = Field(..., pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
#     password: str = Field(..., min_length=8)
#     confirm_password: str

#     @model_validator(mode="after")
#     def validate_passwords(self):
#         if not self.password == self.confirm_password:
#             raise Exception("Password must be same as Confirm Password")
#         return self


# user_one = Register(
#     email="user1@gmail.com", password="12345678", confirm_password="12345678"
# )
# user_two = Register(
#     email="user2@gmail.com", password="12345678", confirm_password="1234567"
# )  #! Error: Exception: Password must be same as Confirm Password

# print(user_one)


#? Q9: Define an Address model and use it inside a User model. Validate a nested JSON structure representing the full user.

# class Address(BaseModel):
#     city:str
#     country:str

# class User(BaseModel):
#     name:str = Field(...,min_length=3,max_length=50)
#     email: str = Field(..., pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
#     address: Address

# user_one = User(name="Jhon Doe",email="jhondoe@gmail.com",address={"city":"Karachi","country":"Pakistan"})
# user_two = User(name="Jhon Doe2",email="jhondoe2@gmail.com",address={"city":"Karachi"}) #! Error: address.country Field required
# print(user_one)


#? Q:10 Use constr, confloat, and conint to enforce:
#* name: 3–30 characters
#* price: greater than 0 and ≤ 10,000
#* quantity: integer ≥ 1
# class Product(BaseModel):
#     name: str = constr(min_length=3, max_length=30)
#     price: float = confloat(gt=0, le=10000)
#     quantity: int = conint(ge=1)


"""
NOTE: This was an exercise on pydantic basics
must try yourself good luck!
"""