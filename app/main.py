import datetime
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    noerror = True
    masks_to_buy = 0

    for person in friends:
        try:
            cafe.visit_cafe(person)

        except Exception as err:
            noerror = False
            if str(err) == "OutdatedVaccineError" or str(
                    err) == "NotVaccinatedError":
                return "All friends should be vaccinated"

            if str(err) == "NotWearingMaskError":
                masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if noerror:
        return f"Friends can go to {cafe.name}"


friends = [
    {
        "name": "Alisa",
        "vaccine": {
            "expiration_date": datetime.date(2100, 12, 5)
        },
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date(2100, 12, 5)
        },
        "wearing_a_mask": True
    },
]
print(go_to_cafe(friends, Cafe("KFC")))
