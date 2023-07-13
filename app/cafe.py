from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(name=visitor["name"])

        elif visitor["vaccine"]["expiration_date"] < \
                OutdatedVaccineError.current_date:
            raise OutdatedVaccineError(name=visitor["name"])

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(name=visitor["name"])

        return f"Welcome to {self.name}"
