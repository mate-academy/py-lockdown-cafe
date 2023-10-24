from cafe import Cafe
import errors as e

def go_to_cafe(friends: list, cafe: Cafe) -> None | str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except e.NotWearingMaskError:
            masks_to_buy += 1
        except e.VaccineError:
            return "All friends should be vaccinated"
        else:
            return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"