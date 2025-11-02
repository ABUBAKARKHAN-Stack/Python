from pydantic import BaseModel, field_validator, model_validator,Field


class User(BaseModel):
    username: str

    @field_validator("username")
    def validate_username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters.")
        return v


user_one = User(username="Abcd")
print(user_one)


class SignupData(BaseModel):
    password: str = Field(...,min_length=8)
    confirm_password: str

    @model_validator(mode="after")
    def isMatch(self):
        if self.password != self.confirm_password:
            raise ValueError("Password do not match")
        return self

# user_three = SignupData(password="12345678",confirm_password="1234567")
user_three = SignupData(password="12345678",confirm_password="12345678")
print(user_three)
