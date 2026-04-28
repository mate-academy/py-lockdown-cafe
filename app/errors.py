class VaccineError(Exception):
    def __str__(
            self
    ) -> str:
        return "VaccineError"


class NotVaccinatedError(VaccineError):
    def __str__(
            self
    ) -> str:
        return "Visitor has not been vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(
            self
    ) -> str:
        return "Visitor's vaccine is outdated"


class NotWearingMaskError(Exception):
    def __str__(
            self
    ) -> str:
        return "Visitor is not wearing a mask"
