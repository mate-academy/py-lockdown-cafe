from typing import List

from app.errors import VaccineError, NotWearingMaskError

from app.cafe import Cafe


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    has_unvaccinated_friend = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            has_unvaccinated_friend = True
        except NotWearingMaskError:
            masks_to_buy += 1
        except (VaccineError, NotWearingMaskError) as e:
            if isinstance(e, VaccineError):
                has_unvaccinated_friend = True
            if isinstance(e, NotWearingMaskError):
                masks_to_buy += 1

    if has_unvaccinated_friend:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
