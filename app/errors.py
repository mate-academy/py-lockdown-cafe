class VaccineError(Exception):
    """Classe base para erros relacionados à vacinação."""
    pass


class NotVaccinatedError(VaccineError):
    """Lançada quando a chave 'vaccine' está ausente."""
    pass


class OutdatedVaccineError(VaccineError):
    """Lançada quando a vacina está expirada."""
    pass


class NotWearingMaskError(Exception):
    """Lançada quando o visitante não está usando máscara."""
    pass
