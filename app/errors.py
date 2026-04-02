# app/errors.py

class VaccineError(Exception):
    """Classe base para erros relacionados à vacinação."""
    pass


class NotVaccinatedError(VaccineError):
    """Lançado quando um visitante não possui um comprovante de vacina."""
    pass


class OutdatedVaccineError(VaccineError):
    """Lançado quando a vacina de um visitante está expirada."""
    pass


class NotWearingMaskError(Exception):
    """Lançado quando um visitante não está usando máscara."""
    pass
