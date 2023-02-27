import datetime
from errors import *
from cafe import Cafe



def go_to_cafe(friends: list, cafe: object) -> str:
	buy = 0

	for x in friends:
		try:
			buy += 1
			if "vaccine" not in x:
				return "All friends should be vaccinated"
			if cafe.visit_cafe(x):
				return f"Friends can go to {cafe.name}"
		except VaccineError as e:
			return "All friends should be vaccinated"
	return f"Friends should buy {buy} masks"
