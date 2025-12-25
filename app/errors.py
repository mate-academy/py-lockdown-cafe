class VaccineError(Exception):
    def __str__(self) -> str:
        return "Vaccines for everyone!"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You should be vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine should be unexpired!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should wear a mask!"
