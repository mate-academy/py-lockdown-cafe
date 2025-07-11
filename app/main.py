from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    vaccine_issue_found = False
    count = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)

        except VaccineError:
            vaccine_issue_found = True

        except NotWearingMaskError:
            if person["wearing_a_mask"] is False:
                count += 1

    if vaccine_issue_found:
        return "All friends should be vaccinated"

    if count > 0:
        return f"Friends should buy {count} masks"

    return f"Friends can go to {cafe.name}"
