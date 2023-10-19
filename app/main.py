from typing import Any
from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError)


def go_to_cafe(friends: list, cafe: "Cafe") -> Any:
    try:
        count = 0
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                count += 1
        if count > 0:
            return f"Friends should buy {count} masks"
    except VaccineError:
        return "All friends should be vaccinated"
    else:
        return f"Friends can go to {cafe.name}"
