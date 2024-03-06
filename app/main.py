from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(cafe: Cafe, friends: list) -> str:
    can_return = True
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (
            NotVaccinatedError,
            OutdatedVaccineError,
            NotWearingMaskError
        ) as e:
            can_return = False
            if isinstance(e, (NotVaccinatedError, OutdatedVaccineError)):
                return "All friends should be vaccinated"
            elif isinstance(e, NotWearingMaskError):
                masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if can_return:
        return f"Friends can go to {cafe.name}"
