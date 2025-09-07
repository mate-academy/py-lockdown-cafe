class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotWearingMaskError(Exception):
    def __init__(self, visitor_name: str = "") -> None:
        super().__init__(f"Visitor {visitor_name} is not wearing a mask.")


class NotVaccinatedError(VaccineError):
    def __init__(self, visitor_name: str = "") -> None:
        super().__init__(f"Visitor {visitor_name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self, visitor_name: str = "") -> None:
        super().__init__(f"Visitor {visitor_name}'s vaccine is outdated.")
