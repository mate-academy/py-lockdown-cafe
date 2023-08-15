class VaccineError(Exception):
    ...


class NotVaccinatedError(VaccineError):
    def __init__(self):
        super().__init__("The Guy seem to be not vaccinated (")


class OutdatedVaccineError(VaccineError):
    def __init__(self):
        super().__init__("The vaccine is expired")


class NotWearingMaskError(ValueError):
    def __init__(self):
        super().__init__("MF is maskless!")
