from app.cafe import Cafe
from errors.errors import (
    NotVaccinatedError,
    VaccineError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_friends = [friend for friend in friends if "vaccine" in friend]
    masks_to_buy = sum(not friend.get("wearing_a_mask", False)
                       for friend in friends)

    try:
        for friend in vaccinated_friends:
            cafe.visit_cafe(friend)

        if masks_to_buy > 0:
            raise (NotWearingMaskError
                   (f"Friends should buy {masks_to_buy} masks"))

        return f"Friends can go to {cafe.name}"

    except (NotVaccinatedError,
            VaccineError,
            OutdatedVaccineError,
            NotWearingMaskError) as e:
        return str(e)
