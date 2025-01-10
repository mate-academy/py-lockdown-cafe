from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            # Спроба перевірити, чи може друг зайти до кафе
            cafe.visit_cafe(friend)
        except VaccineError:
            # Якщо проблеми з вакцинацією
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Якщо у друга немає маски
            masks_to_buy += 1

    # Повертаємо відповідний результат
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
