from datetime import (date,
                      timedelta)


from app.errors import (VaccineError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> (str
                                            | VaccineError
                                            | NotWearingMaskError):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated!")

        if visitor["vaccine"].get("expiration_date",
                                  date.today()
                                  - timedelta(days=1)) < date.today():
            raise OutdatedVaccineError(f"The vaccine of {visitor['name']} "
                                       f"is expired!")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"Visitor {visitor['name']} "
                                      f"shall wear a mask!")

        return f"Welcome to {self.name}"
