import datetime
from app.cafe import Cafe
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        for i in friends[::-1]:
            cafe.visit_cafe(i)
        return f"Friends can go to {cafe.name}"
    except (NotVaccinatedError, OutdatedVaccineError):
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy = len(
            list(filter(lambda x: not x.get("wearing_a_mask"), friends))
        )
        return f"Friends should buy {masks_to_buy} masks"


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
go_to_cafe(friends, Cafe("KFC")) == "Friends can go to KFC"
