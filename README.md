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

- **Python 3.11+**: Ensure that Python is installed on your system.

### 1. Install Dependencies

To install all necessary Python dependencies:

1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
   
### 2. Running Tests

Run All Tests:

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

### Running Tests with GitHub Actions

This repository is set up to automatically run Playwright tests using GitHub Actions on every push or pull request to the `main` branch. Follow the steps below to use it:

1. **Triggering Tests**:
   - Tests are automatically triggered on every push or pull request to the `main` branch.
   - If you want to manually trigger the workflow, you can navigate to the **Actions** tab on GitHub, select the `Run Playwright Tests` workflow, and click the **Run workflow** button.

2. **Viewing Test Results**:
   - After the tests complete, the results are stored as an artifact in GitHub Actions.
   - You can download the artifact by navigating to the **Actions** tab, selecting the specific workflow run, and downloading the `allure-results` artifact.

3. **Generating Allure Reports Locally**:
   - Once you've downloaded the `allure-results` artifact, you can generate the Allure report locally by running:
     ```bash
     allure serve allure-results
     ```

4. **Configuration**:
   - The GitHub Actions workflow uses environment variables defined in the workflow file:
     - `BASE_URL`: The URL of the website to test (default: `https://kiwi.com`).
     - `HEADLESS`: Whether to run the browser in headless mode (`true` or `false`).

   If you need to modify these variables, you can edit the `.github/workflows/test.yml` file in the repository.