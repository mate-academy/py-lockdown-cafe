from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    masks_to_buy = 0
    try:
        for friend in friends:
            if friend["wearing_a_mask"] is False:
                masks_to_buy += 1
            try:
                cafe.visit_cafe(friend)
            except VaccineError:
                return "All friends should be vaccinated"
            except NotWearingMaskError:
                continue
        if masks_to_buy > 0:
            raise NotWearingMaskError

    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
