from errors import VaccineError, NotVaccinatedError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> None:
        if not ("vaccine" in visitors):
            raise NotVaccinatedError("NotVaccinated")


