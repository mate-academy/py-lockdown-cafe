class VaccineError(Exception):
    pass

class NotVaccinatedError(VaccineError):
    pass

class OutdatedVaccineError(VaccineError):
    pass

class NotWearingMaskError(Exception):
    """Visitante não está usando máscara"""
    pass