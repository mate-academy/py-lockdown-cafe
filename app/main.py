from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    count_issue = 0
    masks_a_buy = 0
    vaccine_count = 0

    for person in friends:
        try:
            cafe.visit_cafe(person)
            count_issue += 1
        except NotVaccinatedError as err:
            print(err)
            vaccine_count += 1
        except OutdatedVaccineError as err:
            vaccine_count += 1
            print(err)
        except NotWearingMaskError as err:
            print(err)
            masks_a_buy += 1

    if vaccine_count > 0:
        return "All friends should be vaccinated"

    elif masks_a_buy > 0:
        return f"Friends should buy {masks_a_buy} masks"

    elif count_issue == len(friends):
        return f"Friends can go to {cafe.name}"
