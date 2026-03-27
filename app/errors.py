# Classe base para erros relacionados à vacina
class VaccineError(Exception):
    pass


# Erro quando o visitante não está vacinado
class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Visitante não está vacinado") -> None:
        super().__init__(message)


# Erro quando a vacina do visitante está vencida
class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = (
            "Vacina do visitante está vencida")) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = (
            "Visitante não está usando máscara")) -> None:
        super().__init__(message)
