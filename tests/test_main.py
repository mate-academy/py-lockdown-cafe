# tests/test_main.py

import datetime
import pytest
from app.main import go_to_cafe
from app.cafe import Cafe

def test_all_friends_can_go():
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
        }
    ]
    assert go_to_cafe(friends, Cafe("KFC")) == "Friends can go to KFC"

def test_not_vaccinated():
    friends = [
        {"name": "Alisa", "wearing_a_mask": True},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": True}
    ]
    assert go_to_cafe(friends, Cafe("KFC")) == "All friends should be vaccinated"

def test_mask_required():
    friends = [
        {"name": "Alisa", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": False},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": False}
    ]
    assert go_to_cafe(friends, Cafe("KFC")) == "Friends should buy 2 masks"
