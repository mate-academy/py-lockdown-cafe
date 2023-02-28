
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError


def go_to_cafe(friends: list, cafe: any) -> str:
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except NotWearingMaskError:
        masks_to_buy = sum(not friend.get("wearing_a_mask",
                                          False) for friend in friends)
        return f"Friends should buy {masks_to_buy} masks"
    except NotVaccinatedError:
        return "All friends should be vaccinated"
    except OutdatedVaccineError:
        return "All friends should be vaccinated"

    return f"Friends can go to {cafe.name}"
