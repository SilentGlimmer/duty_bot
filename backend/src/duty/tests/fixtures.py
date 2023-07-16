import pytest
from faker import Faker
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import PostgresDsn

from duty.main import app as duty_app

__all__ = [
    "client",
    "settings",
    "app",
    "faker",
]

from duty.settings import Settings, get_settings


@pytest.fixture(autouse=True, scope="session")
def settings() -> Settings:
    settings = get_settings()
    settings.pg_dsn = PostgresDsn(settings.pg_dsn.unicode_string() + "_test")
    return settings


@pytest.fixture()
def app() -> FastAPI:
    return duty_app


@pytest.fixture()
def client(app) -> TestClient:
    return TestClient(app)


@pytest.fixture()
def faker() -> Faker:
    return Faker()
