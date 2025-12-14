class VaccineError(Exception):
    pass

class NotVaccinatedError(VaccineError):
    def __init__(self, message="Visitor is not vaccinated."):
        self.message = message
        super().__init__(self.message)

class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Visitor's vaccine is outdated."):
        self.message = message
        super().__init__(self.message)

class NotWearingMaskError(Exception):
    def __init__(self, message="Visitor is not wearing a mask."):
        self.message = message
        super().__init__(self.message)