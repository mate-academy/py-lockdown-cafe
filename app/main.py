# main.py
from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        # Спочатку перевіряємо вакцинацію
        try:
            # Перевіряється і вакцина, і маска одночасно
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1  # Якщо не носить маску, додаємо до кількості

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
