from cafe import Cafe
from errors import *

def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            return f"Friends can go to {cafe.name}"
        except VaccineError:
            return f"All friends should be vaccinated"
        except NotWearingMaskError:
            mask += 1

