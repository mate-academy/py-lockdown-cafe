import app.cafe
import app.errors


def go_to_cafe(friends: list, cafe: app.cafe.Cafe) -> str:
    count = 0
    masks_to_buy = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except app.errors.VaccineError:
            count += 1
        except app.errors.NotWearingMaskError:
            masks_to_buy += 1
    if count != 0:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    elif count == 0:
        return f"Friends can go to {cafe.name}"
