import app.errors


def go_to_cafe(friends: list, cafe: str) -> str:
    masks_to_buy = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except app.errors.VaccineError:
            return "All friends should be vaccinated"
        except app.errors.NotWearingMaskError as e:
            masks_to_buy += 1
            error_message = e
    if masks_to_buy >= 1:
        return f"{error_message} {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
