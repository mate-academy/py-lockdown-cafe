import datetime


from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:

            # masks_to_buy = 0
            # for person in friends:
            #     if not person.get("wearing_a_mask"):
            #         masks_to_buy += 1

            masks_to_buy = sum(
                1 for _ in friends if not person.get("wearing_a_mask")
            )

            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"

#------------------------------------------------------------------------

# friends = [
#     {
#         "name": "Alisa",
#         "vaccine": {
#             "expiration_date": datetime.date.today()
#         },
#         "wearing_a_mask": True
#     },
#     {
#         "name": "Bob",
#         "vaccine": {
#             "expiration_date": datetime.date.today()
#         },
#         "wearing_a_mask": True
#     },
# ]
# print(go_to_cafe(friends, Cafe("KFC")))
# print(go_to_cafe(friends, Cafe("KFC")) == "Friends can go to KFC")
#
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
#
# print(go_to_cafe(friends, Cafe("KFC")))
# print(go_to_cafe(friends, Cafe("KFC")) == "Friends should buy 2 masks")
#
#
# friends = [
#     {
#         "name": "Alisa",
#         "wearing_a_mask": True
#     },
#     {
#         "name": "Bob",
#         "vaccine": {
#             "expiration_date": datetime.date.today()
#         },
#         "wearing_a_mask": True
#     },
# ]
# print(go_to_cafe(friends, Cafe("KFC")))
# print(go_to_cafe(friends, Cafe("KFC")) == "All friends should be vaccinated")

# print(datetime.date(year=2019, month=2, day=23))
# print(datetime.date.today())
# print(datetime.date(year=2019, month=2, day=23) < datetime.date.today())
