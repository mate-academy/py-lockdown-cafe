class VaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, message="Not wearing a mask"):
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message="Not vaccinated"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Outdated vaccine"):
        super().__init__(message)
