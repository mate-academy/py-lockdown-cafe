class VaccineError(Exception):
    def __init__(self) -> None:
        super().__init__("Only vaccinated people can visit public places")


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("Only people in masks can visit public places")
