from datetime import datetime, timedelta

import allure
from playwright.sync_api import expect

from objects.page_objects.base_page import BasePage
import os

from objects.page_objects.search_result_page import SearchResultPage
from utils.constants import SearchFormType, CheckBoxState, Airport


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_form = page.locator('[data-test="LandingPageSearchForm"]')
        self.place_picker_from = self.search_form.locator('[data-test="PlacePickerInput-origin"]')
        self.input_from = self.place_picker_from.locator('[data-test="SearchField-input"]')
        self.input_from_item = self.place_picker_from.locator('[data-test="PlacePickerInputPlace"]')
        self.input_from_item_clear_btn = self.place_picker_from.locator('[data-test="PlacePickerInputPlace-close"]')
        self.place_picker_to = self.search_form.locator('[data-test="PlacePickerInput-destination"]')
        self.input_to = self.place_picker_to.locator('[data-test="SearchField-input"]')
        self.input_to_item = self.place_picker_to.locator('[data-test="PlacePickerInputPlace"]')
        self.input_to_item_clear_btn = self.place_picker_to.locator('[data-test="PlacePickerInputPlace-close"]')
        self.input_place_suggest = page.locator('[data-test="PlacePickerRow-wrapper"]')
        self.booking_checkbox = page.locator('[data-test="bookingCheckbox"] input')
        self.current_date_picker = page.locator(
            '[data-test="NewDatePickerOpen"] [data-value]:has([data-test="DatepickerMonthButton"])'
        ).first
        self.date_picker_done_btn = page.locator('[data-test="SearchFormDoneButton"]')
        self.search_field_date_input = self.search_form.locator('[data-test="SearchFieldDateInput"]')
        self.search_btn = self.search_form.locator('[data-test="LandingSearchButton"]')
        self.search_result_view = self.page.locator('[data-test="SearchResultsView"]')

    @allure.step("Open Home page")
    def open(self, hide_cookie_agreement_banner: bool = True):
        if hide_cookie_agreement_banner:
            self.hide_cookie_agreement_banner()
        self.page.goto(url=os.getenv('BASE_URL'))
        expect(self.search_form).to_be_visible()
        return self

    @allure.step("Set departure place")
    def set_departure_place(self, airport: Airport, clear_input_before: bool = True):
        if clear_input_before:
            while self.input_from_item_clear_btn.is_visible():
                self.input_from_item_clear_btn.click()

        self.input_from.click()
        self.page.keyboard.type(airport.code)
        self.input_place_suggest.filter(has_text=airport.city).first.click()
        expect(self.input_from_item).to_contain_text(airport.city)

        return self

    @allure.step("Set destination place")
    def set_destination_place(self, airport: Airport, clear_input_before: bool = True):
        if clear_input_before:
            while self.input_to_item_clear_btn.is_visible():
                self.input_to_item_clear_btn.click()

        self.input_to.click()
        self.page.keyboard.type(airport.code)
        self.input_place_suggest.filter(has_text=airport.city).first.click()
        expect(self.input_to_item).to_contain_text(airport.city)

        return self

    @allure.step("Choose search form type")
    def choose_search_form_type(self, form_type: SearchFormType):
        current_form_type_locator = self.page.locator('[data-test^="SearchFormModesPicker-active-"]')
        current_form_type_locator.click()

        new_form_type_locator = self.page.locator(f'[data-test="ModePopupOption-{form_type}"]')
        new_form_type_locator.click()

        expect(self.page.locator(f'[data-test="SearchFormModesPicker-active-{form_type}"]'))

        return self

    @allure.step("Toggle the Booking checkbox")
    def toggle_booking_checkbox(self, new_state: CheckBoxState):
        if new_state.value:
            self.booking_checkbox.check(force=True)
            expect(self.booking_checkbox).to_be_checked()
        else:
            self.booking_checkbox.uncheck(force=True)
            expect(self.booking_checkbox).not_to_be_checked()

        return self

    def _get_calendar_current_date(self) -> datetime:
        data_value = self.current_date_picker.get_attribute('data-value')
        data_value_cleaned = data_value.split(' (')[0]
        return datetime.strptime(data_value_cleaned, "%a %b %d %Y %H:%M:%S %Z%z")

    @allure.step("Set departure date")
    def set_departure_date(self, days_from_now: int = 0):
        self.search_field_date_input.click()

        current_date = self._get_calendar_current_date()
        departure_date = current_date + timedelta(days=days_from_now)

        departure_day_locator = self.page.locator(f'[data-value="{departure_date.strftime("%Y-%m-%d")}"]')
        departure_day_locator.click()

        self.date_picker_done_btn.click()
        expect(self.search_field_date_input).to_have_value(departure_date.strftime("%a %d %b"))

        return self

    @allure.step("Submit search form")
    def submit_search_form(self):
        self.search_btn.click()
        expect(self.search_result_view).to_be_visible()

        return SearchResultPage(self.page)
