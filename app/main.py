from __future__ import annotations
from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_of_person = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_of_person += 1
    return f"Friends should buy {count_of_person} masks" \
        if count_of_person > 0 else f"Friends can go to {cafe.name}"
