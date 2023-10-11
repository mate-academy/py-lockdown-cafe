import app.errors as errors
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for person in friends:
            try:
                cafe.visit_cafe(person)
            except errors.NotWearingMaskError:
                masks_to_buy += 1

        if masks_to_buy > 0:
            raise errors.NotWearingMaskError
        return f"Friends can go to {cafe.name}"
    except errors.NotVaccinatedError:
        return "All friends should be vaccinated"
    except errors.NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
