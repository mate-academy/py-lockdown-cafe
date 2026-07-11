from app.errors import NotWearingMaskError
from app.errors import VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: str) -> str | None:
    mask_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy += 1
    if mask_to_buy:
        return f"Friends should buy {mask_to_buy} masks"
    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    kfc = Cafe("KFC")

    visitor = {
        "name": "John",
        "age": 21,
        "wearing_a_mask": True,
    }

    print(kfc.visit_cafe(visitor))
