from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(
        friends: list,
        cafe: "Cafe"
) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError as e:
            print(f"{e}")
            return "All friends should be vaccinated"
        except OutdatedVaccineError as o:
            print(f"{o}")
            return "All friends should be vaccinated"
        except NotWearingMaskError as m:
            masks_to_buy += 1
            print(f"{m}")

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
