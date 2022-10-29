class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return ("!!!ATENTION!!! Visitor without "
                "vaccine !!!ATENTION!!!")


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return ("!!!ATENTION!!! Visitor's vaccine is "
                "outdated !!!ATENTION!!!")


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return ("!!!ATENTION!!! Visitor without "
                "mask !!!ATENTION!!!")
