from datetime import date


class VaccineInfo:
    def __init__(self, expiration_date: date, name: str) -> None:
        self.__expiration_date = expiration_date
        self.__name = name

    @property
    def expiration_date(self) -> date:
        return self.__expiration_date

    @property
    def is_valid(self) -> bool:
        return self.expiration_date >= date.today()


class Visitor:
    def __init__(
        self,
        name: str = None,
        age: int = None,
        vaccine: dict = None,
        wearing_a_mask: bool = False
    ) -> None:
        self._name = name
        self._age = age
        self._vaccine = VaccineInfo(**vaccine) if vaccine else None
        self._mask = wearing_a_mask

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def vaccine(self) -> VaccineInfo:
        return self._vaccine

    @property
    def is_wearing_mask(self) -> bool:
        return self._mask
