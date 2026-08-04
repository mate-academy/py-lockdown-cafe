class NotVaccinatedError(Exception):
    pass


class NotWearingMaskError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self._name = name

    @staticmethod
    def visit_cafe(self, visitor: dict) -> None:
        if not "vaccine" in visitor:
            raise NotVaccinatedError()
        if
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()

