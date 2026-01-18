import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from cafe import Cafe


def go_to_cafe(friends, cafe):
    masks_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            if "wearing_a_mask" not in friend or not friend["wearing_a_mask"]:
                masks_needed += 1

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"


# Example usage
if __name__ == "__main__":
    kfc = Cafe("KFC")

    friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False
        },
    ]

    print(go_to_cafe(friends, kfc))