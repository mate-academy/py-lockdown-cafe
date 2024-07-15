from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotWearingMaskError, VaccineError) as e:
            if isinstance(e, VaccineError):
                return "All friends should be vaccinated"
            elif isinstance(e, NotWearingMaskError):
                masks += 1
    if masks > 0:
        return f"Friends should buy {masks} masks"

    return "Friends can go to " + cafe.name
