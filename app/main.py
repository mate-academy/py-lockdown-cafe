from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError


def go_to_cafe(friends, cafe):
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except NotVaccinatedError:
        return "All friends should be vaccinated"
    except (OutdatedVaccineError, NotWearingMaskError) as error:
        if isinstance(error, OutdatedVaccineError):
            return "All friends should be vaccinated"
        if isinstance(error, NotWearingMaskError):
            masks_to_buy = sum(1 for friend in friends if not friend.get("wearing_a_mask"))
            return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"