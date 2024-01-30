from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    counter_vaccine = 0
    counter_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            counter_vaccine += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            counter_mask += 1
    if counter_mask > 0:
        return f"Friends should buy {counter_mask} masks"
    if counter_vaccine == len(friends):
        return f"Friends can go to {cafe.name}"
