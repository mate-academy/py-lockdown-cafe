from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


def go_to_cafe(cafe: Cafe, friends: list) -> str:
    not_vaccinated_count = 0
    without_mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            print(f'{friend["name"]} is not vaccinated.')
            not_vaccinated_count += 1
        except OutdatedVaccineError:
            print(f'{friend["name"]}\'s vaccine is outdated.')
            not_vaccinated_count += 1
        except NotWearingMaskError:
            print(f'{friend["name"]} is not wearing a mask.')
            without_mask_count += 1

    if not_vaccinated_count:
        return "All friends should be vaccinated"
    if without_mask_count:
        return f"Friends should buy {without_mask_count} masks"
    return f"Friends can go to {cafe.name}"
