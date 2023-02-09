class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotVaccinatedError: person is not vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError: vaccine is expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError: please wear a mask"
