class VaccineError(Exception):
    def __str__(self) -> str:
        return "Sorry, but every one of our visitors has a valid vaccination!"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Sorry, but every one of our visitors must be vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Sorry, but you do not have a valid vaccination"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return ("Sorry, but you should wear a mask to protect "
                "others in case you have the virus,"
                " and you should wear a mask to protect yourself.")
