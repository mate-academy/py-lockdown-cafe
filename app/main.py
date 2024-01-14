from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    # error = False
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            print("All friends should be vaccinated")
            # error = True
        except NotWearingMaskError:
            masks_to_buy += 1
            print(f"Friends should buy {masks_to_buy} masks")
            # error = True
    # if error is False:
    return f"Friends can go to {cafe.name}"
