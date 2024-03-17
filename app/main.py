from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    no_mask = 0
    problems = False
    for human in friends:
        try:
            cafe.visit_cafe(human)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            problems = True
            no_mask += 1

    if no_mask != 0:
        return f"Friends should buy {no_mask} masks"

    if not problems:
        return f"Friends can go to {cafe.name}"

# visitor=[
#                     {
#                         "name": "Alisa",
#                         "vaccine": {
#                             "name": "Pfizer",
#                             "expiration_date": datetime.date.today()
#                             + datetime.timedelta(days=30),
#                         },
#                         "wearing_a_mask": False,
#                     },
#                     {
#                         "name": "Bob",
#                         "vaccine": {
#                             "name": "Pfizer",
#                             "expiration_date": datetime.date.today()
#                             + datetime.timedelta(days=20),
#                         },
#                         "wearing_a_mask": False,
#                     },
#                     {
#                         "name": "Harry",
#                         "vaccine": {
#                             "name": "Moderna",
#                             "expiration_date": datetime.date.today()
#                             + datetime.timedelta(days=45),
#                         },
#                         "wearing_a_mask": True,
#                     },
#                 ]
# print(go_to_cafe(visitor, Cafe("KFS")))
