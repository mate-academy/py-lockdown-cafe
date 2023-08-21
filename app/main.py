from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except VaccineError:
                raise
            except NotWearingMaskError:
                masks_to_buy += 1

        if masks_to_buy:
            raise NotWearingMaskError(
                f"Friends should buy {masks_to_buy} masks"
            )
    except VaccineError as error:
        return str(error)
    except NotWearingMaskError as error:
        return str(error)
    else:
        return f"Friends can go to {cafe.name}"
