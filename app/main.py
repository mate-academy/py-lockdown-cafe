from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_to_buy = 0
    vaccination_issue = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            vaccination_issue = True
        except OutdatedVaccineError:
            vaccination_issue = True
        except NotWearingMaskError:
            mask_to_buy += 1

    if vaccination_issue:
        return "All friends should be vaccinated"

    if mask_to_buy > 0:
        return f"Friends should buy {mask_to_buy} masks"

    return f"Friends can go to {cafe.name}"
