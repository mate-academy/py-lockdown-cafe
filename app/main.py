from app.errors import NotWearingMaskError
from app.errors import VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_problem = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_problem += 1
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            masks_to_buy += 1
    if vaccine_problem:
        return "All friends should be vaccinated"
    if not vaccine_problem and masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    if not vaccine_problem and not masks_to_buy:
        return f"Friends can go to {cafe.name}"
