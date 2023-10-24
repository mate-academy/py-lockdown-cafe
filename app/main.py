from app.cafe import Cafe
import app.errors as e


def go_to_cafe(friends: list, cafe: Cafe) -> None | str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except e.VaccineError:
            return "All friends should be vaccinated"
        except e.NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
