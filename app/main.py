from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    buy_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return f"{e}"
        except NotWearingMaskError:
            buy_masks += 1
    if buy_masks:
        return NotWearingMaskError(buy_masks).__str__()
    return f"Friends can go to {cafe.name}"
