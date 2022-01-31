class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message="NotVaccinatedError"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="OutdatedVaccineError"):
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message="NotWearingMaskError"):
        super().__init__(message)
