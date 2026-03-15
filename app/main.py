from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    has_vaccine_problems = False
    friend_whitout_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            has_vaccine_problems = True
        except NotWearingMaskError:
            friend_whitout_mask += 1
    if has_vaccine_problems:
        return "All friends should be vaccinated"
    if friend_whitout_mask > 0:
        return f"Friends should buy {friend_whitout_mask} masks"
    return f"Friends can go to {cafe.name}"
