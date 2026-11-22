class VaccineError(Exception):
    """Główny wyjątek zwiazany ze szczepionkami."""
    pass


class NotVaccinatedError(VaccineError):
    """Wyjętek zgłaszany jesli nie ma klucza 'vaccine'."""
    pass


class OutdatedVaccineError(VaccineError):
    """Wyjątek zgłaszany jeśli klient ma przeterminowaną szczepionkę."""
    pass


class NotWearingMaskError(Exception):
    """Wyjątek zgłaszany jeśli klient nie ma maski"""
    pass
