class VaccineError(Exception):
    def __init__(self, message="Vaccine error occurred"):
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message="The visitor is not vaccinated"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Visitors vaccination is outdated"):
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message="Visitor not wearing a mask"):
        super().__init__(message)