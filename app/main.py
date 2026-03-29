from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe):
    masks_to_buy = 0
    guests = Cafe(cafe)

    for member in friends:
        try:
            guests.visit_cafe(member)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    return f"Friends should buy {masks_to_buy} masks" if masks_to_buy > 0\
        else f"Friends can go to {cafe.name}"
