class VaccineError(Exception):
    """VaccineError"""
    def __init__(self, message: str = "Vaccine error") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError"""
    def __init__(self,
                 message: str = "Visitor has no valid vaccine information"
                 ) -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError"""
    def __init__(self, message: str = "Vaccine is outdated") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """NotWearingMaskError"""
    def __init__(self, message: str = "Visitor is not wearing a mask") -> None:
        super().__init__(message)
