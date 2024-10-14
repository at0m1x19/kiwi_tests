# Kiwi Playwright Tests

This project is set up to run Playwright-based tests for Kiwi's one-way flight search functionality. 
The tests include both regular tests and BDD tests using Gherkin syntax.

## Project Structure

- **tests/**: Contains unit and Gherkin-based test files.
- **features/**: Stores Gherkin `.feature` files.
- **objects/**: Contains page object models for the Playwright tests.
- **.env**: Environment variables required for running tests.

## Getting Started

### Prerequisites

- **Python 3.10+**: Ensure that Python is installed on your system.

### 1. Install Dependencies

To install all necessary Python dependencies:

1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
   
### 3. Running Tests

#### Run All Tests

To run all tests in the suite (both regular and Gherkin tests):

```bash
pytest
```

Run One-Way Search Tests:

```bash
pytest -m one_way_search
```

Run Gherkin BDD Tests:

```bash
pytest -m gherkin
```

Run One-Way Search Gherkin BDD Tests:

```bash
pytest -m gherkin_one_way_search
```

Run Tests with Allure Report Generation:

```bash
pytest -m gherkin_one_way_search --alluredir=allure-results
```

Viewing Allure Reports:

```bash
allure serve allure-results
```