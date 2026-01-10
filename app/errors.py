class VaccineError(Exception):
    def __init__(
            self,
            message: str = "There is some problem with the vaccine"
    ) -> None:
        self.message = message
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    def __init__(
            self,
            message: str = "Sorry, to enter this cafe you must be vaccinated."
                           " Vaccinate and come back!"
    ) -> None:
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            message: str = "Sorry, your vaccine is outdated."
                           " Revaccinate and come back!"
    ) -> None:
        self.message = message
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(
            self,
            message: str = "Sorry, "
                           "to enter this cafe you must be wearing a mask."
                           " Put it on, please"
    ) -> None:
        self.message = message
        super().__init__(self.message)
