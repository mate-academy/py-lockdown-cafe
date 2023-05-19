from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list,
               cafe: Cafe
               ) -> str | VaccineError:

    not_wearing_mask_error = None

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return str(e)
        except NotWearingMaskError as e:
            if not not_wearing_mask_error:
                not_wearing_mask_error = e
            if not_wearing_mask_error:
                not_wearing_mask_error.masks_to_buy += 1

    if not_wearing_mask_error is not None:
        return str(not_wearing_mask_error)

    return f"Friends can go to {cafe.name}"
