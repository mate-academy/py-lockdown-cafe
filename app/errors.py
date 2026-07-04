class VaccineError(Exception):
    def __init__(self, *args: object) -> None:
        self.visitor_name = args[0]
        super().__init__(*args)


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return f"Visitor {self.visitor_name} is not vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return f"Visitor {self.visitor_name}'s vaccine is outdated!"


class NotWearingMaskError(Exception):
    def __init__(self, *args: object) -> None:
        self.visitor_name = args[0]
        super().__init__(*args)

    def __str__(self) -> str:
        return f"Visitor {self.visitor_name} has no mask!"
