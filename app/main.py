from __future__ import annotations
from cafe import Cafe
from errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe):
    masks_to_buy = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            masks_to_buy += 1
            if masks_to_buy > 0:
                print(f"Friends should buy {masks_to_buy} masks")
    return f"Friends can go to {cafe.name}"
