from app.cafe import Cafe
import app.errors


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        for friend in friends:
            cafe.visit_cafe(friend)

        return f"Friends can go to {cafe.name}"
    except app.errors.VaccineError:
        return "All friends should be vaccinated"
    except app.errors.NotWearingMaskError:
        masks_to_buy = sum(1 for friend in friends if not friend.get("wearing_a_mask", False))
        return f"Friends should buy {masks_to_buy} masks"
