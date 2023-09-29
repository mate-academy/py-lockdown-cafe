from app.cafe import Cafe
from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    digit = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            digit += 1
        except VaccineError as e:
            return str(e)
    if digit > 0:
        return f"Friends should buy {digit} masks"
    return f"Friends can go to {cafe.name}"
