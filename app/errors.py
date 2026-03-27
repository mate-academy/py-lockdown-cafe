"""
This module defines custom exception classes for the lockdown cafe.
"""
from abc import ABC, abstractmethod
import datetime


class LockDownError(Exception, ABC):
    """
    Base class for lockdown-related errors.
    """

    def __init__(self, visitor_name: str) -> None:
        """
        Initializes a LockDownError object.

        :param visitor_name: The name of the visitor who caused the error.
        :type visitor_name: str
        """
        self.visitor_name = visitor_name

    @staticmethod
    @abstractmethod
    def condition(visitor: dict) -> bool:
        """
        Checks if the error condition is met.

        :param visitor: A dictionary representing the visitor.
        :type visitor: dict
        :return: True if the error condition is met, False otherwise.
        :rtype: bool
        """
        pass

    @classmethod
    def check(cls, visitor: dict) -> None:
        """
        Checks if the error condition is met and raises the exception if it is.

        :param visitor: A dictionary representing the visitor.
        :type visitor: dict
        :raises LockDownError: If the error condition is met.
        """
        if cls.condition(visitor):
            raise cls(visitor.get("name", "A visitor"))


class VaccineError(LockDownError, ABC):
    """
    Base class for vaccine-related errors.
    """


class NotVaccinatedError(VaccineError):
    """
    Raised when a visitor is not vaccinated.
    """

    @staticmethod
    def condition(visitor: dict) -> bool:
        """
        Checks if the visitor is not vaccinated.

        :param visitor: A dictionary representing the visitor.
        :type visitor: dict
        :return: True if the visitor is not vaccinated, False otherwise.
        :rtype: bool
        """
        return not bool(visitor.get("vaccine"))

    def __str__(self) -> str:
        """
        Returns a string representation of the error.

        :return: A string representation of the error.
        :rtype: str
        """
        return f"{self.visitor_name} is not vaccinated!"


class OutdatedVaccineError(VaccineError):
    """
    Raised when a visitor's vaccine is outdated.
    """
    @staticmethod
    def condition(visitor: dict) -> bool:
        """
        Checks if the visitor's vaccine is outdated.

        :param visitor: A dictionary representing the visitor.
        :type visitor: dict
        :return: True if the visitor's vaccine is outdated, False otherwise.
        :rtype: bool
        """
        return (
            datetime.date.today()
            > visitor.get("vaccine", {}).get(
                "expiration_date",
                datetime.date.min
            )
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the error.

        :return: A string representation of the error.
        :rtype: str
        """
        return f"{self.visitor_name}'s vaccine is outdated!"


class NotWearingMaskError(LockDownError):
    """
    Raised when a visitor is not wearing a mask.
    """
    @staticmethod
    def condition(visitor: dict) -> bool:
        """
        Checks if the visitor is not wearing a mask.

        :param visitor: A dictionary representing the visitor.
        :type visitor: dict
        :return: True if the visitor is not wearing a mask, False otherwise.
        :rtype: bool
        """
        return not visitor.get("wearing_a_mask", False)

    def __str__(self) -> str:
        """
        Returns a string representation of the error.

        :return: A string representation of the error.
        :rtype: str
        """
        return f"{self.visitor_name} is not wearing mask!"
