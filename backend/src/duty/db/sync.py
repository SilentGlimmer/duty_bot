from typing import Type, Optional

from sqlalchemy import create_engine, Engine, Pool

from duty.settings import get_settings


def get_engine(poolclass: Optional[Type[Pool]] = None) -> Engine:
    settings = get_settings()
    return create_engine(str(settings.pg_dsn), poolclass=poolclass)
