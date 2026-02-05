class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("NotVaccinatedError")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("OutdatedVaccineError")


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("NotWearingMaskError")
