from abc import ABC, abstractmethod

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)
from app.utility import Visitor


class IRule(ABC):
    @abstractmethod
    def validate(self, visitor: Visitor) -> None:
        pass


class CafeRuleVisitorVaccinated(IRule):
    def validate(self, visitor: Visitor) -> None:
        if not visitor.vaccine:
            raise NotVaccinatedError(f"{visitor.name} was not vaccinated")


class CafeRuleVaccineValid(IRule):
    def validate(self, visitor: Visitor) -> None:
        if not visitor.vaccine.is_valid:
            raise OutdatedVaccineError(f"{visitor.name}'s vaccine is outdated")


class CafeRuleVisitorWearsMask(IRule):
    def validate(self, visitor: Visitor) -> None:
        if not visitor.is_wearing_mask:
            raise NotWearingMaskError(f"{visitor.name} does not wear a mask")


class CafeRuleEngine:
    def __init__(self) -> None:
        self._rules: list[IRule] = []

    def add(self, rule: IRule) -> bool:
        if not isinstance(rule, IRule):
            return False
        self._rules.append(rule)

    def check_rules(self, visitor: Visitor) -> None:
        for rule in self._rules:
            rule.validate(visitor)
