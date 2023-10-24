class VaccineError(Exception):
    pass

class NotWearingMaskError(Exception):
    pass

class NotVaccinatedError(VaccineError):
    pass

class OutdatedVaccineError(VaccineError):
    pass
