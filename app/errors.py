class VaccineError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Only vaccinated visitors can enter")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("The visitor has an outdated vaccination")


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("All visitors must wear masks")
