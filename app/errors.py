class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message="Non vaccinated! You can`t go to cafe") -> None:
        super().__init__(message)
    pass


class NotWearingMaskError(Exception):
    def __init__(self, message="Where is your mask? you have to wear the mask") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Vaccine expired! You can`t go to cafe") -> None:
        super().__init__(message)
