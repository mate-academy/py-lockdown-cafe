
class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):

    def __init__(self, error_string: str = "") -> None:
        self.error_str = error_string

    def __str__(self) -> str:
        if self.error_str:
            return self.error_str

        return "Visitor has no record of vaccination."


class OutdatedVaccineError(VaccineError):

    def __init__(self, error_string: str = "") -> None:
        self.error_str = error_string

    def __str__(self) -> str:
        if self.error_str:
            return self.error_str

        return ("Visitor cannot visit the cafe "
                + "because he has an outdated vaccination record.")


class NotWearingMaskError(Exception):

    def __init__(self, error_string: str = "") -> None:
        self.error_str = error_string

    def __str__(self) -> str:
        if self.error_str:
            return self.error_str

        return ("Visitor cannot visit the cafe "
                + "because he/she does not have a face mask.")
