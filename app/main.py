from app.errors import (VaccineError,
                        NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        print(f"Friends should buy {masks_to_buy} masks")
