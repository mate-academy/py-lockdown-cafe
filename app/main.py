from app import errors
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    for i in friends:
        try:
            cafe.visit_cafe(i)
        except (errors.NotVaccinatedError, errors.OutdatedVaccineError):
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            count += 1

    if count != 0:
        return f"Friends should buy {count} masks"
    else:
        return f"Friends can go to {cafe.name}"

#
# friends = [
#     {
#         "name": "Alisa",
#         "vaccine": {
#             "expiration_date": datetime.date.today()
#         },
#         "wearing_a_mask": False
#     },
#     {
#         "name": "Bob",
#         "vaccine": {
#             "expiration_date": datetime.date.today()
#         },
#         "wearing_a_mask": False
#     },
# ]
# print(go_to_cafe(friends, Cafe("KFC")))
