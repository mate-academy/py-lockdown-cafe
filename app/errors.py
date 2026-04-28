class VaccineError(Exception):
    def __init__(
            self,
            visitor_name: str,
            *args
    ) -> None:
        super().__init__(*args)
        self.visitor_name = visitor_name

    def __str__(
            self
    ) -> str:
        return "VaccineError"


class NotVaccinatedError(VaccineError):
    def __str__(
            self
    ) -> str:
        return f"{self.visitor_name} has not been vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(
            self
    ) -> str:
        return f"{self.visitor_name}'s vaccine is outdated"


class NotWearingMaskError(Exception):
    def __init__(
            self,
            visitor_name: str,
            *args
    ) -> None:
        super().__init__(*args)
        self.visitor_name = visitor_name

    def __str__(
            self
    ) -> str:
        return f"{self.visitor_name} is not wearing a mask"
