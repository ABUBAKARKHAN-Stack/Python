from pydantic import BaseModel,computed_field,Field

# class Product(BaseModel):
#     price: float
#     quantity: int

#     @computed_field
#     @property
#     def total_price(self) -> float:
#         if self.quantity > 0:
#             return self.quantity * self.price
#         else: 
#             raise ValueError("Invalid Quantity")


# p1 = Product(price=99.99,quantity=2)
# print(p1.total_price)

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(...,ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_bill(self) -> float:
        return self.nights * self.rate_per_night

booking = Booking(
    user_id=1,
    rate_per_night=55.5,
    nights=10,
    room_id=1,
)
print(booking.total_bill)
print(booking.model_dump())