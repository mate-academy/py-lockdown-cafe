from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError



def go_to_cafe(friends: list, cafe: Cafe) -> str:
    counter = 0
    for i in friends:
        try:
            cafe.visit_cafe(i)
        except VaccineError("All friends should be vaccinated"):
            raise
        except NotWearingMaskError:
            counter += 1
    if counter > 0:
        return f"Friends should buy {counter} masks"
    return f"Friends can go to {cafe.name}"
