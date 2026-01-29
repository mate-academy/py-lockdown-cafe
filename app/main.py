from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_count = 0
    vaccine_error_count = 0
    for i in friends:
        try:
            cafe.visit_cafe(i)
        except NotWearingMaskError as e:
            print(e)
            masks_count += 1
        except VaccineError:
            vaccine_error_count += 1

    if vaccine_error_count == 0 and masks_count == 0:
        return f"Friends can go to {cafe.name}"

    if vaccine_error_count:
        return "All friends should be vaccinated"

    if vaccine_error_count == 0 and masks_count:
        return f"Friends should buy {masks_count} masks"
