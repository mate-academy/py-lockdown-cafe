from app.errors import NotVaccinatedError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor["name"]} "
                f"is not vaccinated "
                f"and cannot enter the cafe."
            )
