import pytest

from objects.page_objects.home_page import HomePage
from utils.constants import SearchFormType, CheckBoxState, Airport


@pytest.mark.parametrize(
    'departure_airport, destination_airport, travel_date_from_now_days',
    [
        (Airport.RTM, Airport.MAD, 7),
    ],
    ids=[
        f'departure airport: {Airport.RTM}, destination airport: {Airport.MAD}, travel date 7 days from now',
    ]
)
@pytest.mark.one_way_search
def test_one_way_flight_search(
        page,
        departure_airport,
        destination_airport,
        travel_date_from_now_days,
):
    HomePage(page) \
        .open() \
        .choose_search_form_type(form_type=SearchFormType.ONE_WAY) \
        .set_departure_place(airport=departure_airport) \
        .set_destination_place(airport=destination_airport) \
        .toggle_booking_checkbox(new_state=CheckBoxState.UNCHECKED) \
        .set_departure_date(days_from_now=travel_date_from_now_days) \
        .submit_search_form()
