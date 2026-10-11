from erros import *
from cafe import Cafe

def go_to_cafe(friends: list, cafe: Cafe):
    has_vaccine_issue = False
    masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            has_vaccine_issue = True
        except NotWearingMaskError:
            masks += 1
    if has_vaccine_issue:
        return "All friends should be vaccinated"
    elif masks > 0:
        return f"Friends should buy {masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
