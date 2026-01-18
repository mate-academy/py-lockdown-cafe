import pytest
import sys
import os
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from cafe import Cafe
from main import go_to_cafe
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

def test_all_vaccinated_and_masked():
    friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
    ]
    kfc = Cafe("KFC")
    assert go_to_cafe(friends, kfc) == "Friends can go to KFC"