from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    VaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as ve:
            print(f"Exception occurred for {friend["name"]}: {ve}")
            return "All friends should be vaccinated"
        except NotWearingMaskError as nwme:
            count += 1
            print(f"Exception occurred for {friend["name"]}: {nwme}")
    if count:
        return f"Friends should buy {count} masks"
    return f"Friends can go to {cafe.name}"
