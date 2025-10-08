class InvalidChaiError(Exception):
    pass


def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError(
                f"Demanded flavor '{flavor}' does not exist in our menu"
            )
        if not isinstance(cups, int):
            raise TypeError("The number of cups must be an integar")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} of {flavor} chai: ruppes{total}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for visiting chai code!")

bill("mint",10)
bill("masala","three")
bill("ginger",3)