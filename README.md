# Event Scheduler Backend

## Overview

This backend application is designed to handle event scheduling across different time zones. It allows users to create events, retrieve events, and get a list of valid time zones. The backend is built using Django and Django REST Framework (DRF).

## Features

- Create events with a specific start time, duration, and time zone.
- Retrieve a list of events.
- Fetch a list of valid time zones for event scheduling.

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework 3.14+
- pytz

## Installation

Clone the Repository

```sh
git clone https://github.com/Lembani/event_scheduler_django.git
cd event_scheduler_django
```

### Create a Virtual Environment

```sh
python -m venv venv
```

### Activate the Virtual Environment

On Windows:

```sh
venv\Scripts\activate
```

On macOS/Linux:

```sh
source venv/bin/activate
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Apply Migrations

```sh
python manage.py migrate
```

### Run the Development Server

```sh
python manage.py runserver
```

The server will be accessible at <http://localhost:8000>.

### API Endpoints

- List Events
- Create Event
- List Timezones

#### List Events

```sh
GET /api/events/
```

Retrieves a list of all events.

#### Create Event

```sh
POST /api/events/
```

Creates a new event. Requires the following fields:

- name: The name of the event.
- start_time: The start time of the event in ISO 8601 format.
- duration: The duration of the event in seconds.
- timezone: The time zone in which the event occurs.

### Timezones

#### List Timezones

```sh
GET /api/timezones/
```

Retrieves a list of all valid time zones.

## Configuration

To customize the time zone list or other settings, modify the views.py and urls.py files in the events app.

## Contributing

### Fork the Repository

### Create a Branch

```sh
git checkout -b feature/your-feature
```

- Make Changes
- Commit Changes (git commit -am 'Add some feature')
- Push to the Branch (git push origin feature/your-feature)
- Create a Pull Request

## License

This project is licensed under the MIT License.

## Contact

For questions or issues, please contact <lembanisakala@gmail.com>

## Acknowledgements

- [Lembani Sakala](https://github.com/Lembani)
- [Django REST Framework](https://github.com/encode/django-rest-framework)
- [pytz](https://github.com/python/cpython/tree/master/Lib/pytz)
