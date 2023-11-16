from app.cafe import Cafe
import app.errors


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = len(friends) - sum((friend["wearing_a_mask"] for friend in friends))

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except app.errors.VaccineError:
            return "All friends should be vaccinated"
        except app.errors.NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"
