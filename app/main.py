from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_vaccine = 0
    count_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            count_vaccine += 1
        except NotWearingMaskError:
            count_mask += 1
    if count_vaccine > 0:
        return "All friends should be vaccinated"
    if count_vaccine == 0 and count_mask > 0:
        return f"Friends should buy {count_mask} masks"
    if count_vaccine + count_mask == 0:
        return f"Friends can go to {cafe.name}"
