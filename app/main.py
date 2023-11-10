from cafe import Cafe
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list) -> str | Exception:
    lack_of_masks_count = 0
    issues_count = 0
    for friend in friends:
        if not friend["wearing_a_mask"]:
            lack_of_masks_count += 1
    if lack_of_masks_count > 1:
        raise NotWearingMaskError(f"Friends should buy {lack_of_masks_count} masks")
    if lack_of_masks_count == 1:
        raise NotWearingMaskError

    for friend in friends:
        try:
            Cafe.vizit_cafe(friend)
        except NotVaccinatedError:
            issues_count += 1
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            issues_count += 1
            raise OutdatedVaccineError
    if not issues_count and not lack_of_masks_count:
        return f"Friends can go to {Cafe.__name__}"
