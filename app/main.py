from app.cafe import Cafe
from typing import List, Dict
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError)  # Добавьте эти импорты


def go_to_cafe(friends: List[Dict[str, any]], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "Все друзья должны быть вакцинированы"
        except NotWearingMaskError:
            if not friend.get("wearing_a_mask", False):  # Исправлено условие
                masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Друзья должны купить {masks_to_buy} масок"

    return f"Друзья могут посетить {cafe.name}"
