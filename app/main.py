import app.cafe as c
import app.errors as e


def go_to_cafe(friends: list, cafe: c.Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except e.VaccineError:
            return "All friends should be vaccinated"
        except e.NotWearingMaskError:
            masks_to_buy += 1
            continue
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
