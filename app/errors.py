class VaccineError(Exception):
    """VaccineError"""


class NotVaccinatedError(VaccineError):
    """NotVaccinateError"""


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError """


class NotWearingMaskError(Exception):
    """NotWearingMaskError """
