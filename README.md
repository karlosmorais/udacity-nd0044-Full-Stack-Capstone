# Casting Agency API

## Project Description
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## API URL
The API is hosted at: `[ADD YOUR DEPLOYED RENDER/HEROKU/AWS URL HERE]` (e.g., `https://casting-agency-xx.onrender.com`)
- Local Base URL: `http://localhost:8080/`

## Authentication for Reviewers
This project uses Auth0 for authentication. Endpoints require a valid JWT token in the `Authorization` header (`Bearer <TOKEN>`).

### Setup Auth0
1. Create an API in Auth0/Tenant.
2. Create three roles: `Casting Assistant`, `Casting Director`, `Executive Producer`.
3. Assign permissions as detailed in the RBAC section below.
4. Update `setup.sh` with your `AUTH0_DOMAIN` and `API_AUDIENCE`.

### Generating Tokens
To test the API, you can generate tokens for each role using the Auth0 dashboard or the provided login link (if configured). 

**Reviewer Note**: If specific tokens are required for grading without setting up a new tenant, please use the following (expired/example tokens - replace with valid ones in `setup.sh` for local testing):
- **Assistant Token**: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpST1NqbXBocTNwcFdWdW1BOWpQTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1qdHFzZGFxeGhrY21vcm5vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2OTkyMmFlYjJlN2UzZDBiNTIxOTIyZWIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNzcxMTg4Mzc3LCJleHAiOjE3NzExOTU1NzcsInNjb3BlIjoiIiwiYXpwIjoiVHhWVnFuaHVjanJkWk1jSkd1aElGVlAzNFZFZ0JXYmoifQ.C9YWVX45dl2LxrW8pViKgztDznwNTSEXu_190jRiFmWcBjKt-dnAPB7UnyfbFWzJgMfa4A925UQG12Hzm86AWdzcFS_O8j7cN42rEBvkZkcxRcbgZg2SNbHoupyR6PbNtExl5piq-y5aAbsWsJ5NrZ0v32y_yx2COwwQKqavbALpojrsnXMxN4maBFgF-DVc34PXdMJ0LW8tiZAGz6Bv4RagF8-08cBbWeA-ftNn5-WDxu1rKzHWhM4HEsex9QRegJm097Jrhq2KbPkJZJwzEaqfv-m5Cxx80RiCdqFK6fQZ2Tlr47JqEWxfSfknrJt3y_pGK7H4-Ak8ij7KZM6uDg`
- **Director Token**: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpST1NqbXBocTNwcFdWdW1BOWpQTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1qdHFzZGFxeGhrY21vcm5vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2OTkyMmIxNGI3MGJlMTAwODE3YTI1NWMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNzcxMTg4MjMwLCJleHAiOjE3NzExOTU0MzAsInNjb3BlIjoiIiwiYXpwIjoiVHhWVnFuaHVjanJkWk1jSkd1aElGVlAzNFZFZ0JXYmoifQ.jwkcO0FCpRghFIDajbgbIwumFfK95rOIKwHQu1AJaTt2VwXtsSslFvx080OmkwZOn1msAYH7pJIMhPs7yuReuD3nGUFtij2K4Cj3cbRP6ystfG_U5fmFXdj6tKkSgIyT-v1sTGBRKRSWJrHio9Yqk1lSH9zIe-NxyQ6IGN1cSzUbhDBjsWa8qfw12CY3SeD-5VS4B3wqlYygGxOb69hbF1u-b4lPxiM4qcaZEoHYNvEy0c1QAHoxyg8WVF5YGMUabUOWR-YVmvqNvp8whk-SrqLcRjuETEFWRx4_pVnVQtUZxO1lnyZ1HG4NCHLyKhCscnk1dsQoYjoE29TJv6imSQ`
- **Producer Token**: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpST1NqbXBocTNwcFdWdW1BOWpQTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1qdHFzZGFxeGhrY21vcm5vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2OTkyMmIzNGI3MGJlMTAwODE3YTI1NjUiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNzcxMTg4MDc4LCJleHAiOjE3NzExOTUyNzgsInNjb3BlIjoiIiwiYXpwIjoiVHhWVnFuaHVjanJkWk1jSkd1aElGVlAzNFZFZ0JXYmoifQ.QG-_fiBXitCBDVwBST42q2lghdfvytV3D8xtpudvw6LiJWscMumPs721JBFlTVZtzrQhCxEkXWfbuVA1KhFBS6YQMSvSvXONB2x0PaBZqhf53mJ8a82hdfDyK3Dhjx5T4980iuN5YsfFtbpuRf7LSWKXpELzrM7oZs6snU-ByfdvzVEiwjAIbs1u6SMCv6fAmoBwTCXeJk2Yijxw-EGdq0ACxcH8fnkioAr6j1ANtq4cVx6Yb0e8KTKMWzfhyRQm88bWG69RTT94Fw1A_GL8vW1jiwvjp-r52kPlseIyAHr22EUOqD358uNeLgd1rjuET7eBFSC9uYU_rHFWv9jidA`

## Getting Started

### Installing Dependencies
1. **Python 3.7+** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).
2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

### Database Setup
With Postgres running, restore a database using the `casting_agency.psql` file provided. In terminal run:

```bash
createdb casting_agency
python manage.py db upgrade
```

### Running the Server

From within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export Flask_APP=app.py
export FLASK_ENV=development
source setup.sh
python app.py
```

## API Reference

### Getting Started
- Base URL: `http://localhost:8080/` (Local), `[DEPLOYED URL]` (Production)
- Authentication: API requires Auth0 token (Bearer token) in the `Authorization` header.

### Error Handling
Errors are returned as JSON objects in the following format:
```json
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 401: AuthError (Unauthorized)
- 403: AuthError (Forbidden)

### Endpoints

#### GET /actors
- General: Returns a list of actors and success value.
- Permission: `get:actors`
- Sample: `curl http://localhost:8080/actors -H "Authorization: Bearer <token>"`

```json
{
  "actors": [
    {
      "age": 25,
      "gender": "Male",
      "id": 1,
      "name": "Test Actor"
    }
  ],
  "success": true
}
```

#### GET /movies
- General: Returns a list of movies and success value.
- Permission: `get:movies`
- Sample: `curl http://localhost:8080/movies -H "Authorization: Bearer <token>"`

```json
{
  "movies": [
    {
      "id": 1,
      "release_date": "2023-01-01",
      "title": "Test Movie"
    }
  ],
  "success": true
}
```

#### POST /actors
- General: Creates a new actor.
- Permission: `post:actors`
- Required: `name`, `age`, `gender`.

#### POST /movies
- General: Creates a new movie.
- Permission: `post:movies`
- Required: `title`, `release_date`.

#### PATCH /actors/<id>
- General: Updates an existing actor.
- Permission: `patch:actors`

#### PATCH /movies/<id>
- General: Updates an existing movie.
- Permission: `patch:movies`

#### DELETE /actors/<id>
- General: Deletes an actor.
- Permission: `delete:actors`

#### DELETE /movies/<id>
- General: Deletes a movie.
- Permission: `delete:movies`

## RBAC (Roles & Permissions)

### Casting Assistant
- Can view actors and movies (`get:actors`, `get:movies`)

### Casting Director
- All permissions of Casting Assistant
- Add or delete an actor from the database (`post:actors`, `delete:actors`)
- Modify actors or movies (`patch:actors`, `patch:movies`)

### Executive Producer
- All permissions of Casting Director
- Add or delete a movie from the database (`post:movies`, `delete:movies`)

## Testing
To run the tests, run
```bash
source setup.sh
python test_app.py
```
