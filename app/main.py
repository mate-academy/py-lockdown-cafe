
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

def go_to_cafe(friends, cafe):
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except NotVaccinatedError:
        return "All friends should be vaccinated"
    except OutdatedVaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy = sum(not friend.get("wearing_a_mask", False) for friend in friends)
        return "Friends should buy {} masks".format(masks_to_buy)
    return "Friends can go to {}".format(cafe.name)
