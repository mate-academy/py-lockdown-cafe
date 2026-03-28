from .cafe import Cafe
from .errors import NotVaccinatedError
from .errors import OutdatedVaccineError
from .errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccination_issue = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            vaccination_issue = True
            break
        except NotWearingMaskError:
            masks_to_buy += 1
        except Exception as e:
            print(f"Unexpected error for {friend['name']}: {e}")

    if vaccination_issue:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
