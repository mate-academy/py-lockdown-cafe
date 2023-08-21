from app.errors import NotWearingMaskError


def go_to_cafe(cafe, friends: list, cafe_name: str = None) -> str:
    masks_to_buy = 0

    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe_name}"
