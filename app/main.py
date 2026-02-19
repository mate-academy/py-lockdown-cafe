from typing import List
from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    """
    Перевіряє чи можуть друзі піти в кафе разом

    Args:
        friends (list): Список друзів (словників)
        cafe (Cafe): Об'єкт кафе

    Returns:
        str: Повідомлення про результат перевірки
    """
    vaccine_problems = 0
    masks_to_buy = 0

    # Перевіряємо кожного друга
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # Проблеми з вакцинацією (невакцинований або прострочена вакцина)
            vaccine_problems += 1
        except NotWearingMaskError:
            # Проблеми з маскою
            masks_to_buy += 1

    # Повертаємо результат згідно з пріоритетом
    if vaccine_problems > 0:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
