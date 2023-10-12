from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: "Cafe") -> str:
    violations = checking_visitors(friends, cafe)

    if violations < 0:
        return "All friends should be vaccinated"
    elif violations > 0:
        return f"Friends should buy {violations} masks"
    return f"Friends can go to {cafe.name}"


def checking_visitors(visitors: list[dict], cafe: "Cafe") -> int:
    violations = 0

    for visitor in visitors:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            violations = -1
            break
        except NotWearingMaskError:
            violations += 1

    return violations
