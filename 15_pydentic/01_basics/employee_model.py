from typing import Optional
from pydantic import BaseModel, Field
import re


class Employee(BaseModel):
    id: int
    name: str = Field(
        #! This ... make sure that name field must be required
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Abubakar Aijaz",
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
    )


# employee_data = {
#     "id": 1,
#     "name": "ALEX",
#     "department": "IT",
#     "salary": 200000

# }
# employee_one = Employee(**employee_data)
# print(employee_one)


class User(BaseModel):
    email: str = Field(..., pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
    age:str = Field(
        ...,
        ge=0,
        le=120,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount Percentage"
    )


user_one = User(email="alice@example.com")
print(user_one)
