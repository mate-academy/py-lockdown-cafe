# errors.py

class VaccineError(Exception):
    """Classe base para erros relacionados à vacinação."""
    pass


class NotVaccinatedError(VaccineError):
    """Lançada quando o visitante não possui o registro de vacinação."""
    pass


class OutdatedVaccineError(VaccineError):
    """Lançada quando a vacina do visitante está vencida."""
    pass


class NotWearingMaskError(Exception):
    """Lançada quando o visitante não está usando máscara."""
    pass
