from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError, OutdatedVaccineError, NotVaccinatedError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            return f"Friends should buy {cafe.count_friends - 1} masks"
        return f"Friends can go to {cafe.name}"
