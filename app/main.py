from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: str) -> str:
    no_vaccine, mask = 0, 0
    for friend in friends:
        mate = Cafe(cafe)
        try:
            mate.visit_cafe(friend)
        except VaccineError:
            no_vaccine += 1
        except NotWearingMaskError:
            mask += 1
    if no_vaccine > 0:
        return "All friends should be vaccinated"
    if mask > 0:
        return f"Friends should buy {mask} masks"
    return f"Friends can go to {cafe.name}"
