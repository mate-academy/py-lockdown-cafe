
from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe):
    counter = 0
    counter2 = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            counter += 1
        except VaccineError:
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            counter2 += 1
    if counter2 > 0:
        print(f"Friends should buy {counter2} masks")
    if len(friends) == counter:
        print(f"Friends can go to {cafe.name}")
