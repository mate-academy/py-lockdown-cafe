import datetime


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError (Exception):
    pass


class NotWearingMaskError  (Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError

        vcc_expiration_date = visitor["vaccine"]["expiration_date"]
        current_date = datetime.date.today()

        if not vcc_expiration_date >= current_date:
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"


def go_to_cafe(fiends: list, cafe: Cafe) -> str:
    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    friends = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": False
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": False
        },
    ]
    print(go_to_cafe(friends, Cafe("KFC")) == "Friends should buy 2 masks")
