from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, name: str) -> None:
    cafe = Cafe(name)
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy == 0:
        print(f"Friends can go to {cafe.name}")
    elif masks_to_buy == len(friends):
        print("All friends should be vaccinated")
    else:
        print(f"Friends should buy {masks_to_buy} masks")
