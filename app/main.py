from app.cafe import Cafe

from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friend_with_no_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friend_with_no_mask += 1

    if friend_with_no_mask > 0:
        return f"Friends should buy {friend_with_no_mask} masks"
    return f"Friends can go to {cafe.name}"
