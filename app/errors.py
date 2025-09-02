class VaccineError(Exception):
    def __init__(self,
                 message: str = "Problema relacionado "
                                "à vacinação.") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Pessoa não vacinada.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self,
                 message: str = "A vacina está vencida "
                                "ou desatualizada.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self,
                 message: str = "Pessoa não está "
                                "usando máscara.") -> None:
        super().__init__(message)
