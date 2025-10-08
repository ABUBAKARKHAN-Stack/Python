def brew_chai(flavor):
    try:
        if flavor not in ["masala", "ginger", "elaichi"]:
            raise ValueError("Unsupported Chai Flavor...")
    except ValueError as e:
        print(f"Error while brewing a chai ::  {e}")
    else:
        print(f"brewing {flavor} chai..")


brew_chai("asala")


class OutOfIngredientsError(Exception):
    pass


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")

    print("Chai is ready..")


make_chai(1, 0)
