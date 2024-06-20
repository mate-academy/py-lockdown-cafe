from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    without_mask_count = 0
    friends_count = 0
    count = 0
    for friend in friends:
        count += 1
        try:
            if not friend["wearing_a_mask"]:
                without_mask_count += 1
            cafe.visit_cafe(friend)
            friends_count += 1
            if without_mask_count != 0 and friend == friends[-1]:
                raise NotWearingMaskError
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            if count == len(friends):
                return f"Friends should buy {without_mask_count} masks"
    if friends_count == len(friends):
        return f"Friends can go to {cafe.name}"
