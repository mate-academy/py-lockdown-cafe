class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):

    def __str__(self) -> str:
        return ("There are people in your life "
                "worth living for! Get vaccinated!!!")


class OutdatedVaccineError(VaccineError):

    def __str__(self) -> str:
        return "Your vaccination is overdue! Get vaccinated!!!"


class NotWearingMaskError(Exception):

    def __str__(self) -> str:
        return "The mask saves from viruses!!!"
