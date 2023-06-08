class VaccineError(Exception):
    """Error to check general issues with vaccines"""
    def __str__(self) -> str:
        return "General issue with vaccine"


class NotVaccinatedError(VaccineError):
    """Error to prevent not vaccinated people to enter cafe"""
    def __str__(self) -> str:
        return "Not vaccinated people can't enter cafe"


class NotWearingMaskError(Exception):
    """Error to prevent people who don't wear mask to enter cafe"""
    def __str__(self) -> str:
        return "People without mask can't enter cafe"


class OutdatedVaccineError(VaccineError):
    """Error to prevent people with outdated vaccine to enter cafe"""
    def __str__(self) -> str:
        return "People with outdated vaccine can't enter cafe"
