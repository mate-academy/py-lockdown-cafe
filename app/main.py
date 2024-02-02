import datetime
from app.cafe import Cafe
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: str, cafe: Cafe) -> None:
    masks_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"


friends = [
    {
        "name": "Alisa",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    },
]

print(go_to_cafe(friends, Cafe("KFC")))
