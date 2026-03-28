# main.py
import datetime
from app.cafe import Cafe
from typing import List, Dict


def go_to_cafe(friends: List[Dict[str, object]], cafe: Cafe) -> str:
    # Перевірка вакцинації для кожного друга
    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"
        if friend["vaccine"]["expiration_date"] < datetime.date.today():
            return "All friends should be vaccinated"

    # Якщо всі друзі вакциновані, перевіряємо маски
    mask_needed = sum(1 for f in friends if not f.get("wearing_a_mask", False))
    if mask_needed > 0:
        return f"Friends should buy {mask_needed} masks"

    # Якщо все добре, можна йти в кафе
    return f"Friends can go to {cafe.name}"
