FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

WORKDIR /app

RUN python -m pip install --upgrade pip && pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --ignore-pipfile

COPY backend .
WORKDIR /app/src
CMD ["gunicorn", "--bind", ":8000", "duty_bot.wsgi:application"]
