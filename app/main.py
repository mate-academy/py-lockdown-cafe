from app.errors import NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe):
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except (NotVaccinatedError, OutdatedVaccineError) as e:
        return "All friends should be vaccinated"
    except NotWearingMaskError:


    return f"Friends can go to {cafe.name}"
