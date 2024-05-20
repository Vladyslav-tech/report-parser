import pytest
from typing import Dict


# Mock classes for testing
class MockParser:
    def __init__(self, first_page: str, summary_content: str):
        self.first_page = first_page
        self.summary_content = summary_content

    def process(self, data: bytes) -> Dict[str, str]:
        return {
            'first_page': self.first_page,
            'summary_content': self.summary_content
        }


class MockApiClient:
    def get(self, url: str):
        class Response:
            def json(self):
                return {'download_url': url}

        return Response()


# Test data
first_page_text = '''
ГУАП  
КАФЕДРА № 43 
ОТЧЕТ  
ЗАЩИЩЕН С ОЦЕНКОЙ  
ПРЕПОДАВАТЕЛЬ  
старший преподаватель     М.Д. Поляк  
должность, уч. степень, звание   подпись, дата   инициалы, фамилия  

ОТЧЕТ О ЛАБОРАТОРНОЙ РАБОТЕ  №2 
Синхронизация потоков средствами POSIX  
по курсу: ОПЕРАЦИОННЫЕ  СИСТЕМЫ  


РАБОТУ ВЫПОЛНИЛ  
СТУДЕНТ  гр. № 4131     Б.А. Гусев  
подпись, дата   инициалы, фамилия  

Санкт -Петербург  2024
'''

summary_content = 'СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ'


@pytest.fixture
def valid_parser_service():
    parser = MockParser(first_page_text, summary_content)
    api_client = MockApiClient()
    return ParserService(parser=parser, api_client=api_client)


@pytest.fixture
def invalid_title_parser_service():
    invalid_first_page_text = '''
    ГУАП  
    ЗАЩИЩЕН С ОЦЕНКОЙ  
    старший преподаватель     М.Д. Поляк  
    Санкт Петербург  2024
    '''
    parser = MockParser(invalid_first_page_text, summary_content)
    api_client = MockApiClient()
    return ParserService(parser=parser, api_client=api_client)


@pytest.fixture
def invalid_summary_parser_service():
    invalid_summary_content = 'Some other content'
    parser = MockParser(first_page_text, invalid_summary_content)
    api_client = MockApiClient()
    return ParserService(parser=parser, api_client=api_client)


@pytest.fixture
def invalid_both_parser_service():
    invalid_first_page_text = '''
    ГУАП  
    ЗАЩИЩЕН С ОЦЕНКОЙ  
    старший преподаватель     М.Д. Поляк  
    Санкт Петербург  2024
    '''
    invalid_summary_content = 'Some other content'
    parser = MockParser(invalid_first_page_text, invalid_summary_content)
    api_client = MockApiClient()
    return ParserService(parser=parser, api_client=api_client)


def test_check_report_valid(valid_parser_service):
    data = valid_parser_service.parse_data(b"dummy data")
    result = valid_parser_service.check_report(data)
    assert result['valid'] == True
    assert 'errors' not in result or len(result['errors']) == 0


def test_check_report_invalid_title(invalid_title_parser_service):
    data = invalid_title_parser_service.parse_data(b"dummy data")
    result = invalid_title_parser_service.check_report(data)
    assert result['valid'] == False
    assert 'Invalid title' in result['errors']


def test_check_report_invalid_summary(invalid_summary_parser_service):
    data = invalid_summary_parser_service.parse_data(b"dummy data")
    result = invalid_summary_parser_service.check_report(data)
    assert result['valid'] == False
    assert 'Invalid summary' in result['errors']


def test_check_report_invalid_both(invalid_both_parser_service):
    data = invalid_both_parser_service.parse_data(b"dummy data")
    result = invalid_both_parser_service.check_report(data)
    assert result['valid'] == False
    assert 'Invalid title' in result['errors']
    assert 'Invalid summary' in result['errors']
