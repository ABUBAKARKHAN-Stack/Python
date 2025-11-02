from pydantic import field_validator, BaseModel, model_validator
from datetime import datetime


class Person(BaseModel):
    firstName: str
    lastName: str

    @field_validator("firstName", "lastName")
    def name_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError("Name must be start with capital letter")
        return v


# p1 = Person(firstName="abubakar",lastName="aijaz") #! Error
p1 = Person(firstName="Abubakar", lastName="Aijaz")
print(p1)


class User(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower().strip()


u1 = User(email="AbubAkar@codePeria.com")
print(u1)


class Product(BaseModel):
    price: float  # * $4.44

    @field_validator("price", mode="before")
    def parsePrice(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", ""))
        return v


p1 = Product(price="$4.44")
print(p1)


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date_range(self):
        if self.end_date <= self.start_date:
            raise ValueError("End Date must be after Start Date")
        return self


# d1 = DateRange(start_date="2025-11-03T14:30:00", end_date="2025-11-03T12:00:00")
d1 = DateRange(start_date="2025-11-03T14:30:00", end_date="2025-11-03T19:00:00")
print(d1)
