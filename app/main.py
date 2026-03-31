from app.cafe import Cafe

from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    non_vaccinated_count = 0
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, visitor=friend)
        except VaccineError:
            non_vaccinated_count += 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if non_vaccinated_count:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if not masks_to_buy and not non_vaccinated_count:
        return f"Friends can go to {cafe.name}"
