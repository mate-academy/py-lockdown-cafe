class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError (Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        try:
            visitor["vaccine"]
        except KeyError:
            raise NotVaccinatedError


if __name__ == "__main__":
    kfc = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
    }
    kfc.visit_cafe(visitor)
