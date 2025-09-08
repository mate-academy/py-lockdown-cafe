import datetime

class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError(Exception):
    pass

class NotWearingMaskError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str :
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if (visitor["vaccine"]["expiration_date"]
                and visitor["vaccine"]["expiration_date"] < datetime.date.today()):
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False :
            raise NotWearingMaskError
        return f"Welcome to {self.name}"



def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0 :
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
