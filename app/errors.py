class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    # def __str__(self) -> str:
    #     return "Visitor is not vaccinated."
    pass


class OutdatedVaccineError(VaccineError):
    # def __str__(self) -> str:
    #     return "Vaccine is outdated."
    pass


class NotWearingMaskError(Exception):
    # def __str__(self) -> str:
    #     return "Visitor is not wearing a mask."
    pass
