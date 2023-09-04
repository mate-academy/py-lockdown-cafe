import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def init(self, name: str) -> None:
        self.name = name

    @staticmethod
    def visit_cafe(visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        expiration_date = visitor["vaccine"].get("expiration_date")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError()

        if "wearing_a_mask" in visitor and not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()

        print("Welcome to KFC")

    def go_to_cafe(self, friends: list, cafe: list) -> str:
        masks_to_buy = 0
        for friend in friends:
            try:

                Cafe.visit_cafe(friend)
            except NotVaccinatedError or OutdatedVaccineError:
                return "All friends should be vaccinated"

            except NotWearingMaskError:
                masks_to_buy += 1
        if masks_to_buy != 0:
            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {self.name}"
