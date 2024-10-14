import os

from pytest_bdd import scenarios, given, when, then
from utils.constants import SearchFormType, CheckBoxState, Airport

FEATURES_DIR = os.path.join(os.path.dirname(__file__), '../../features/test_one_way_flight_search.feature')
scenarios(FEATURES_DIR)


@given("I am on the Kiwi homepage")
def open_homepage(homepage):
    homepage.open()


@when("I choose the one-way search form")
def choose_one_way_form(homepage):
    homepage.choose_search_form_type(form_type=SearchFormType.ONE_WAY)


@when('I set the departure airport to "Rotterdam"')
def set_departure_airport(homepage):
    homepage.set_departure_place(airport=Airport.RTM)


@when('I set the destination airport to "Madrid"')
def set_destination_airport(homepage):
    homepage.set_destination_place(airport=Airport.MAD)


@when('I toggle the booking checkbox to "Unchecked"')
def toggle_booking_checkbox(homepage):
    homepage.toggle_booking_checkbox(new_state=CheckBoxState.UNCHECKED)


@when("I set the departure date to 7 days from now")
def set_departure_date(homepage):
    homepage.set_departure_date(days_from_now=7)


@then("I should see the search results")
def verify_search_results(homepage):
    homepage.submit_search_form()
