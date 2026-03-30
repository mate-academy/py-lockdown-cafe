import app.cafe as cafe_pkg
import app.errors as errors_pkg


def go_to_cafe(friends: list[dict], cafe: cafe_pkg.Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors_pkg.VaccineError:
            return "All friends should be vaccinated"
        except errors_pkg.NotWearingMaskError:
            pass

    masks_to_buy = sum(
        1 for friend in friends if not friend.get("wearing_a_mask")
    )
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
