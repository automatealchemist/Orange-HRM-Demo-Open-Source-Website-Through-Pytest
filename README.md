```markdown
# OrangeHRM Demo Website Automation (Pytest Framework)

This repository contains automated test scripts for the OrangeHRM Demo Website using the Pytest framework. The automation covers various features of the website, including login, employee management, and more.

## Features Implemented

- Pytest Framework – A simple and powerful testing framework for automation.
- Page Object Model (POM) – Organizes test scripts in a structured way for better maintenance.
- Logging – Captures test execution details for debugging and analysis.
- Reporting – Generates test execution reports for easy tracking of test results.
- Screenshot Generation – Captures screenshots on test failures to help in debugging.

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/automatealchemist/Orange-HRM-Demo-Open-Source-Website-Through-Pytest.git
cd Orange-HRM-Demo-Open-Source-Website-Through-Pytest
```

### Create and Activate Virtual Environment
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Tests
To execute the test cases, run:
```sh
pytest
```

For detailed reporting with logs and screenshots, run:
```sh
pytest --html=report.html --self-contained-html
```

## Project Structure
```
|-- tests/                 # Contains test cases
|-- pages/                 # Page Object Model (POM) classes
|-- logs/                  # Stores log files
|-- reports/               # Stores test execution reports
|-- screenshots/           # Captures screenshots on test failures
|-- conftest.py            # Pytest configuration file
|-- requirements.txt       # List of dependencies
|-- README.md              # Project documentation
```

## Notes
- Ensure ChromeDriver or the required WebDriver is installed and compatible with your browser.
- Update the config file if needed before running tests.

## Contributions
Feel free to fork this repository and contribute improvements by creating a pull request.

Happy Testing.
```

