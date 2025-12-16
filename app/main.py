from typing import List, Dict, Any
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    masks_to_buy: int = 0
    someone_unvaccinated: bool = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            someone_unvaccinated = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if someone_unvaccinated:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
