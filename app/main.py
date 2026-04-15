from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccine_issue = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issue = True
            break
        except NotWearingMaskError:
            masks_to_buy += 1

    if vaccine_issue:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


# Пример использования (можно закомментировать при сдаче):
if __name__ == "__main__":
    import datetime

    friends_list = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False
        },
    ]

    my_cafe = Cafe("KFC")
    print(go_to_cafe(friends_list, my_cafe))
