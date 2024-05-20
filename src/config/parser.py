from src.config.base import BaseSettings


class ParserSettings(BaseSettings):
    TITLE_KEYWORDS: list[str] = [
        "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
        "САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ",
        "СТУДЕНТ",
        "САНКТ-ПЕТЕРБУРГ",
        "КАФЕДРА",
        "ОТЧЕТ",
        "ПРЕПОДАВАТЕЛЬ"
    ]
    SUMMARY_KEYWORDS: list[str] = [
        "СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ"
    ]


parser_settings = ParserSettings()
