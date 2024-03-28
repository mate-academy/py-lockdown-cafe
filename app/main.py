import datetime
from cafe import Cafe
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_friends = [friend for friend in friends if friend.get("vaccine")]
    masks_to_buy = sum(not friend.get("wearing_a_mask") for friend in friends)

    if not vaccinated_friends:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
