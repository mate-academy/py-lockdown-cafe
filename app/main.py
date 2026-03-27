from app import errors

from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    number_of_unvaccinated_people = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            number_of_unvaccinated_people += 1
        except errors.NotWearingMaskError:
            masks_to_buy += 1

    if number_of_unvaccinated_people:
        return "All friends should be vaccinated"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
