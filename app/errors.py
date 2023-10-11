class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError (Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("All members have to wear mask", *args)
