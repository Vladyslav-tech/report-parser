# from contextlib import contextmanager
# from typing import Generator
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
#
# from config.base import postgres_settings
#
# engine = create_engine(url=postgres_settings.postgres_url, pool_pre_ping=True, echo=False)
#
#
# def create_session() -> scoped_session:
#     return scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
#
#
# @contextmanager
# def get_session() -> Generator[scoped_session, None, None]:
#     session = create_session()
#     try:
#         yield session
#     finally:
#         session.remove()
