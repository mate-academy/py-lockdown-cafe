class VaccineError(Exception):

    def __init__(self, visitor: dict, *args) -> None:
        super().__init__(*args)
        self.visitor = visitor

    def __str__(self) -> str:
        return (f"{self.visitor['name']} is not "
                f"vaccinated or vaccine is outdated.")


class NotVaccinatedError(VaccineError):

    def __str__(self) -> str:
        return (f"{self.visitor['name']} is not vaccinated "
                f"and therefore is not allowed to enter the cafe.")


class OutdatedVaccineError(VaccineError):

    def __str__(self) -> str:
        return (f"{self.visitor['name']} has outdated vaccine "
                f" therefore is not allowed to enter the cafe.")


class NotWearingMaskError(Exception):

    def __init__(self, visitor: dict, *args) -> None:
        super().__init__(*args)
        self.visitor = visitor

    def __str__(self) -> str:
        return (f"{self.visitor['name']} is not wearing a mask! "
                f"Therefore visitor can not enter.")
