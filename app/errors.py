class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    """Виняток, що виникає, коли особа не носить маску."""
    pass
