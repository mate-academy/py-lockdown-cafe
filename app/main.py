from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> None | str:
    wear_mask = 0
    counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            counter += 1
        except VaccineError as e:
            return f"{e}"
        except NotWearingMaskError:
            wear_mask += 1
    if len(friends) == counter:
        return f"Friends can go to {cafe.name}"

    if wear_mask:
        return f"Friends should buy {wear_mask} masks"
