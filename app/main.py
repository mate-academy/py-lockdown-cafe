from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except NotWearingMaskError:

            masks_to_buy = 0
            for friend in friends:
                if not friend.get("wearing_a_mask"):
                    masks_to_buy += 1

            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"
