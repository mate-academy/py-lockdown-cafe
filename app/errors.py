class VaccineError(Exception):
    """Base class for all vaccination-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"{visitor_name} is not vaccinated")


class OutdatedVaccineError(VaccineError):
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"{visitor_name} has an outdated vaccine")


class NotWearingMaskError(Exception):
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"{visitor_name} is not wearing a mask")
