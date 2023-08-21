class VaccineError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message="Visitor is not vaccinated!"):
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, expiration_date, message="Vaccine is outdated!"):
        self.expiration_date = expiration_date
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message="Visitor is not wearing a mask!"):
        super().__init__(message)
