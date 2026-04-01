from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_counter = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError as error:
            print(error)
            return "All friends should be vaccinated"
        except NotWearingMaskError as error:
            mask_counter += 1
            print(error)
    if mask_counter != 0:
        return f"Friends should buy {mask_counter} masks"
    return f"Friends can go to {cafe.name}"
