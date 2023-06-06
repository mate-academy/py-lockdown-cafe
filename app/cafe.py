from app.rules import (CafeRuleEngine,
                       CafeRuleVaccineValid,
                       CafeRuleVisitorVaccinated,
                       CafeRuleVisitorWearsMask)
from app.utility import Visitor


class Cafe:
    def __init__(self, name: str) -> None:
        self._name = name
        self._rule_engine = CafeRuleEngine()
        self._rule_engine.add(CafeRuleVisitorVaccinated())
        self._rule_engine.add(CafeRuleVaccineValid())
        self._rule_engine.add(CafeRuleVisitorWearsMask())

    @property
    def name(self) -> str:
        return self._name

    def visit_cafe(self, visitor: dict) -> str:
        visitor: Visitor = Visitor(**visitor)
        self._rule_engine.check_rules(visitor)
        return f"Welcome to {self.name}"
