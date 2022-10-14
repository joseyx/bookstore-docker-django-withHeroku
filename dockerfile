# Pull base image
FROM python:3.10.4-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./poetry.lock ./pyproject.toml ./
RUN pip install poetry==1.2.0
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root --no-ansi

# Copy project
COPY . .