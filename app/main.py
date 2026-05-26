from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        for friend in friends:
            if "vaccine" not in friend:
                raise VaccineError

            if (
                friend["vaccine"]["expiration_date"]
                < __import__("datetime").date.today()
            ):
                raise VaccineError

    except VaccineError:
        return "All friends should be vaccinated"

    try:
        for friend in friends:
            if friend["wearing_a_mask"] is False:
                raise NotWearingMaskError

    except NotWearingMaskError:
        masks_to_buy = len(
            [friend for friend in friends if not friend["wearing_a_mask"]]
        )
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
