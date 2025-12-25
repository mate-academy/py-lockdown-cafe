from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    bed_result = []
    neg_count = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            bed_result.append("All friends should be vaccinated")
        except NotWearingMaskError:
            neg_count += 1
            bed_result.append(f"Friends should buy {neg_count} masks")

    if not bed_result:
        return f"Friends can go to {cafe.name}"

    return bed_result[-1]
