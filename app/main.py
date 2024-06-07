from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    is_access = True
    is_vaccinated = True
    masks_not_worn = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_not_worn += 1
            is_access = False
        except OutdatedVaccineError:
            is_access = False
            is_vaccinated = False
        except NotVaccinatedError:
            is_access = False
            is_vaccinated = False
    if is_access:
        raise f"Friends can go to {cafe.name}"
    if masks_not_worn:
        raise f"Friends should buy {masks_not_worn} masks"
    if not is_vaccinated:
        raise "All friends should be vaccinated"


if __name__ == "__main__":
    import datetime
    visitor = {
            "name": "John",
            "age": 21,
            "wearing_a_mask": True,
        }
    cafe = Cafe("")
    print(cafe.visit_cafe(visitor))
