import app.cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError,\
    NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: app.cafe.Cafe) -> str:
    vaccinated_friends = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            vaccinated_friends += 1
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
