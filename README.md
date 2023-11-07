# indices-trade-lab-backend

![Django tests](https://github.com/TechInnovatorsHub/indices-trade-lab-backend/actions/workflows/django.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8-blue)
![Django Version](https://img.shields.io/badge/django-4.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

Indices Trade Lab is a Forex trading website built using Django Rest Framework. This project provides a platform for trading various indices. Users can access real-time market data, analyze trends, and execute trades.

## Features

- Real-time market data for various indices.
- User authentication and authorization.
- Trading functionality with buy/sell orders.
- Portfolio management and transaction history.
- Performance analytics and reports.
- RESTful API for integration with other systems.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/indices-trade-lab-backend.git
cd indices-trade-lab-backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv indices-backend
source indices-backend/bin/activate  # On Windows, use: indices-backend\Scripts\activate
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser for admin access: # if not on organization database

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

The application should now be accessible at `http://localhost:8000/`.

## Configuration

- Configure settings, such as database and secret keys, in the settings.py file.
- Set up environment variables for sensitive information.

### Frontend Implementation

Please see this repository for the frontend: [indices trade lab](https://github.com/TechInnovatorsHub/indices-trade-lab)

## Testing

Tests are run using [pytest](https://docs.pytest.org/en/latest/).
All tests are available in their respective `/tests/` folder

To execute the tests, use the following command:

```bash
pytest
```

## Contribution

We welcome contributions to Indices Trade Lab. Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Create a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.

## Contact

For any questions or issues, please contact [TechInnovatorsHub](mailto:techinnovatorshub@gmail.com).

Happy trading!
