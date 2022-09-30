class Error(Exception):
    pass


class VaccineError(Error):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Error):
    pass
