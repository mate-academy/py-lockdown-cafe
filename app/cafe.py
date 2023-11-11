import datetime

from errors import VaccineError, NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated!")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated!")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError

 def go_to_cafe(friends: list, cafe: Cafe):
     vaccinated_friends = [friend for friend in friends if friend.get("vaccine")]

     if len(vaccinated_friends) < len(friends):
         raise VaccineError("All friends should be vaccinated")

     masks_to_buy = sum(not friend.get("wearing_a_mask", False) for friend in friends)
     if masks_to_buy > 0:
         return f"Friends should buy {masks_to_buy} masks"

     return f"Friends can go to {cafe.name}"
