from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
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

        if masks_to_buy:
            return f"Friends should buy {masks_to_buy} masks"
        return f"Friends can go to {cafe.name}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
