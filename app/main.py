from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask = 0
            for visitor in friends:
                if visitor["wearing_a_mask"] is False:
                    mask += 1
            return f"Friends should buy {mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
