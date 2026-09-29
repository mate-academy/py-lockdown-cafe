from datetime import date
from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)

kfc = Cafe("KFC")

friends = [
    {"name": "Paul",
     "age": 27,
     "vaccine": {"expiration_date": date(year=2029, month=7, day=24)},
     "wearing_a_mask": True
     },
    {"name": "Alice",
     "age": 22,
     "vaccine": {"expiration_date": date(year=2027, month=6, day=13)},
     "wearing_a_mask": True
     },
    {"name": "Sam",
     "age": 22,
     "vaccine": {"expiration_date": date(year=2019, month=2, day=7)},
     "wearing_a_mask": True
     }
]


def go_to_cafe(friends: list, cafe: object) -> str:

    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except NotWearingMaskError:
            masks_to_buy += 1

        except VaccineError:
            return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
