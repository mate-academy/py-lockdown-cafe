class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Only vaccinated visitors can visit the cafe!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The vaccine must not be expired!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "All visitors must wear masks!"
