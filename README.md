# Job Application Tracker API

A portfolio-ready Django REST API for tracking job applications, interview stages, follow-up dates, and notes.

## Features

- Create, list, update, and delete job applications
- Track statuses: wishlist, applied, interview, offer, and rejected
- Filter by status and location
- Search by company, role, location, and notes
- Sort by application date, status, company, or last update
- Automated API tests

## Tech stack

- Python 3.12+
- Django
- Django REST Framework
- django-filter
- SQLite for local development

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```

The API is available at `http://127.0.0.1:8000/api/applications/`.

## Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/api/applications/` | List applications |
| POST | `/api/applications/` | Create an application |
| GET | `/api/applications/<id>/` | View one application |
| PATCH | `/api/applications/<id>/` | Update an application |
| DELETE | `/api/applications/<id>/` | Delete an application |

Useful query parameters include `?status=applied`, `?search=python`, and `?ordering=-updated_at`.

## Example request

```json
{
  "company_name": "Example Labs",
  "role": "Junior Python Developer",
  "status": "applied",
  "location": "Remote",
  "job_url": "https://example.com/jobs/123",
  "applied_on": "2026-09-30",
  "notes": "Follow up after one week"
}
```

## Design notes

The project intentionally uses a simple local database so it can be run without paid services. Authentication and PostgreSQL are planned next improvements; the current open API is for local portfolio demonstration only.

## Attribution

This is an original portfolio implementation built with the official Django and Django REST Framework documentation. No third-party project is presented as original work.

- https://docs.djangoproject.com/
- https://www.django-rest-framework.org/
- https://django-filter.readthedocs.io/

## Roadmap

- Add user authentication and per-user application ownership
- Add interview events and follow-up reminders
- Add PostgreSQL configuration through environment variables
- Add API documentation with OpenAPI
- Add GitHub Actions CI