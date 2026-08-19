from app.errors import VaccineError
from app.errors import NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_to_buy += 1
    except VaccineError:
        return "All friends should be vaccinated"

    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":

    visitor = [
        {
            "name": "John",
            "age": 21,
            "wearing_a_mask": True,
        },
        {
            "name": "Alisa",
            "age": 19,
            "wearing_a_mask": True,
        },
    ]

    print(go_to_cafe(visitor, Cafe("name")))
