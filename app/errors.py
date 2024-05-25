class VaccineError(Exception):
    def __init__(self, message="All friends should be vaccinated"):
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, message="All friends should wear a mask"):
        super().__init__(message)
