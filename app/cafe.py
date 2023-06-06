from app.rules import (CafeRuleEngine,
                       CafeRuleVaccineValid,
                       CafeRuleVisitorVaccinated,
                       CafeRuleVisitorWearsMask)
from app.utility import Visitor


class Cafe:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__rule_engine = CafeRuleEngine()
        self.__rule_engine.add(CafeRuleVisitorVaccinated())
        self.__rule_engine.add(CafeRuleVaccineValid())
        self.__rule_engine.add(CafeRuleVisitorWearsMask())

    @property
    def name(self) -> str:
        return self.__name

    def visit_cafe(self, visitor: dict) -> str:
        visitor: Visitor = Visitor(**visitor)
        self.__rule_engine.check_rules(visitor)
        return f"Welcome to {self.name}"
