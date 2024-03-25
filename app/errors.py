class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name
        super().__init__(f"{visitor_name} is not vaccinated")


class OutdatedVaccineError(VaccineError):
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name
        super().__init__(f"{visitor_name}'s vaccine is outdated")


class NotWearingMaskError(Exception):
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name
        super().__init__(f"{visitor_name} is not wearing a mask")
