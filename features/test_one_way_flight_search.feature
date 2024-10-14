@gherkin
@gherkin_one_way_search
Feature: One Way Flight Search

  Scenario: Search for a one-way flight from Rotterdam to Madrid 7 days from now
    Given I am on the Kiwi homepage
    When I choose the one-way search form
    And I set the departure airport to "Rotterdam"
    And I set the destination airport to "Madrid"
    And I toggle the booking checkbox to "Unchecked"
    And I set the departure date to 7 days from now
    Then I should see the search results