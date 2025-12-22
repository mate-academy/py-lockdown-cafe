from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> None:

    masks_to_buy = 0
    has_vaccine_issue = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            has_vaccine_issue = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if has_vaccine_issue:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
