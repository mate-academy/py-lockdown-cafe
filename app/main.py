from app.cafe import Cafe
from app.errors import NotVaccinatedError
from app.errors import  NotWearingMaskError



def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_to_buy += 1
            except NotVaccinatedError:
            # return "All friends should be vaccinated"
                raise
    except NotVaccinatedError as e:
        return "All friends should be vaccinated"
    if not masks_to_buy == 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"