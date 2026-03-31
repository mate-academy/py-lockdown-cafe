from app.errors import VaccineError, NotVaccinatedError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    check = False
    number = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            check = True
        except NotWearingMaskError:
            number += 1

    if check:
        return "All friends should be vaccinated"
    if number > 0:
        return f"Friends should buy {number} masks"
    return f"Friends can go to {cafe.name}"
