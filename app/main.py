import app.errors as errors
import app.cafe as cafe
import datetime


def go_to_cafe(friends: list, cafe: cafe.Cafe) -> str:
    masks_to_buy = 0
    for visitor in friends:
        try:
            _ = cafe.visit_cafe(visitor)
        except errors.VaccineError:
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
