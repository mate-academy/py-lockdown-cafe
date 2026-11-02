class VaccineError(Exception):
    """Classe base para erros relacionados à vacina."""
    pass


class NotVaccinatedError(VaccineError):
    """Lançado quando o visitante não possui a chave 'vaccine'."""
    pass


class OutdatedVaccineError(VaccineError):
    """Lançado quando a data de validade da vacina é anterior à data atual."""
    pass


class NotWearingMaskError(Exception):
    """Lançado quando o visitante não está usando máscara."""
    pass
