from .cafe import Cafe
from .errors import NotVaccinatedError
from .errors import OutdatedVaccineError
from .errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_friends = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            vaccinated_friends += 1
        except NotVaccinatedError:
            return f"{friend} should be vaccinated"
        except OutdatedVaccineError:
            return f"{friend} has an outdated vaccine"
        except NotWearingMaskError:
            masks_to_buy += 1
        except Exception as e:
            print(f"Unexpected error for {friend}: {e}")

    if vaccinated_friends != len(friends):
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
