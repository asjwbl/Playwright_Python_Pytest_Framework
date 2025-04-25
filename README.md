
# 🧪 Playwright-Python-Pytest Test Automation Framework

This repository contains a scalable and maintainable test automation framework built using **Playwright**, **Pytest**, and **Pydantic**, designed to test both **UI** and **API** layers of [AutomationExercise.com](https://automationexercise.com).

---

## 🚀 Features

✅ End-to-end UI test automation using **Playwright**  
✅ REST API test automation using **httpx**  
✅ Modular Page Object Model (POM) structure  
✅ Reusable and abstracted UI components (input, dropdown, button, etc.)  
✅ Dynamic test data generation using **Faker**  
✅ Data validation using **Pydantic models**  
✅ Pre-commit hooks for linting, formatting, and type checks  
✅ Scalable test fixtures via `conftest.py`

---

## 📁 Project Structure

```
Playwright_Python_Pytest_Framework/
│
├── tests/
│   ├── ui_tests/                # All UI test cases
│   ├── api_tests/               # All API test cases
│   └── helpers/                 # Auth and common test helpers
│
├── web_abstractions/
│   ├── components/
│   │   ├── basic_components/    # Reusable UI components
│   │   └── composite_components/# Composite components (e.g., SignupForm)
│   └── views/                   # Page Object Model for views
│
├── models/                      # Pydantic models for API requests/responses
│
├── data/                        # Static or test data (e.g., test files)
│
├── conftest.py                  # Global fixtures (browser, test data, API client)
├── requirements.txt             # Project dependencies
├── pytest.ini                   # Pytest config
├── .pre-commit-config.yaml      # Pre-commit hooks
└── README.md                    # This file
```

---

## 🔧 Installation

```bash
git clone https://github.com/your-org/Playwright_Python_Pytest_Framework.git
cd Playwright_Python_Pytest_Framework
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install
```

---

## 🧪 Running Tests

### Run All UI Tests
```bash
pytest tests/ui_tests/ --headed
```

### Run API Tests
```bash
pytest tests/api_tests/
```

### Run a Specific Test
```bash
pytest tests/ui_tests/test_signup_login.py::test_register_user
```

---

## 🧼 Code Quality

### Format, Lint, and Type-Check
```bash
pre-commit run --all-files
```

---

## 📦 Built With

- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [httpx](https://www.python-httpx.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Faker](https://faker.readthedocs.io/)
- [Pre-commit](https://pre-commit.com/)

---

## 📌 TODO

- [ ] Integrate Allure Reporting
- [ ] Add support for mobile device emulation
- [ ] CI Integration (GitHub Actions/GitLab CI)

---
## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```