from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except VaccineError:
                raise VaccineError("The vaccine is expired or unavailable")
            except NotWearingMaskError:
                masks_to_buy += 1
        if masks_to_buy > 0:
            raise NotWearingMaskError(f"Friends should buy "
                                      f"{masks_to_buy} masks")
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
    except VaccineError:
        return "All friends should be vaccinated"
    else:
        return f"Friends can go to {cafe.name}"
