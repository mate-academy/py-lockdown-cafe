from cafe import Cafe
from errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    if not isinstance(friends, list) or not isinstance(cafe, Cafe):
        return "All friends should be vaccinated"

    masks_to_buy = 0
    vaccine_issue_found = False

    for friend in friends:
        if not isinstance(friend, dict):
            return "All friends should be vaccinated"

        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issue_found = True
        except NotWearingMaskError:
            masks_to_buy += 1

    # Пріоритет: проблеми з вакцинацією блокують усю групу
    if vaccine_issue_found:
        return "All friends should be vaccinated"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
