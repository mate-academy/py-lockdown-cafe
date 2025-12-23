from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe):
    all_vaccined = True
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            masks_to_buy += 1

    if not all_vaccined:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"


