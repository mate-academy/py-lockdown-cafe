from app.errors import NotWearingMaskError, OutdatedVaccineError, NotVaccinatedError
from app.cafe import Cafe


def go_to_cafe(friends: dict, cafe: Cafe) -> str:

    vaccinated_friends = sum(1 for friend in friends if friend.get("vaccine"))
    masks_to_buy = 0
    if vaccinated_friends < len(friends):
        return "All friends should be vaccinated"

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
