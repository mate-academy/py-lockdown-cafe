class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass


from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
    def visit_cafe(self, visitor: dict) -> None:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if vaccine.get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")
def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
    friends_without_masks = [
        friend for friend in friends
        if not friend.get("wearing_a_mask", False)
    ]
    if friends_without_masks:
        masks_to_buy = len(friends_without_masks)
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
