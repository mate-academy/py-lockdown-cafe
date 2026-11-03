from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated_friends = 0
    not_masked_friends = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError) as e:
            not_vaccinated_friends += 1
            print(e)
        except NotWearingMaskError as e:
            not_masked_friends += 1
            print(e)

    if not_vaccinated_friends > 0:
        return "All friends should be vaccinated"
    if not_masked_friends > 0:
        return f"Friends should buy {not_masked_friends} masks"
    else:
        return f"Friends can go to {cafe.name}"
