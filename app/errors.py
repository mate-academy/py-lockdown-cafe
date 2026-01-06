class VaccineError(Exception):
    pass

class NotVaccinatedError(VaccineError):
    pass

class OutdatedVaccineError(VaccineError):
    pass
#s
class NotWearingMaskError(Exception):
    pass
