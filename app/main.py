from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    # Najpierw sprawdzamy szczepienia u wszystkich znajomych
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                # Pomijamy maski w pierwszym przebiegu
                continue
    except VaccineError:
        return "All friends should be vaccinated"

    # Jeśli nikt nie zgłosił VaccineError, liczymy osoby bez masek
    masks_to_buy = 0
    for friend in friends:
        if not friend.get("wearing_a_mask", False):
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
