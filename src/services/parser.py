import os
import re
from typing import Dict, List, Protocol

import requests

from src.intergrations.base import IApiClient
from src.parsers.base import IParser


class IParserService(Protocol):
    def check_report(self, data: dict) -> dict:
        """
        Check the report for validity.
        Args:
            data: The parsed data from the PDF file.
            data = {
                'num_pages': int,
                'first_page': str,
                'last_page': str,
                'summary_content': str,
            }
        Return:
            {
                'valid': bool,
                'errors': list[error_message]
            }
        """
        raise NotImplementedError


class ParserService(IParserService):
    def __init__(self,
                 parser: IParser,
                 api_client: IApiClient,
                 title_keywords: list[str],
                 summary_keywords: list[str]):
        self.__parser = parser
        self.__api_client = api_client
        self.title_keywords = title_keywords
        self.summary_keywords = summary_keywords

    def fetch_data_from_api(self, path_url: str) -> bytes:
        """
        Fetches the PDF file data from the given URL.
        """
        response = self.__api_client.get(path_url).json()
        return response.content

    # def fetch_data_from_api(self, path_url: str) -> bytes:
    #     """
    #     Fetches the PDF file data from the given URL.
    #     """
    #     response = self.__api_client.get(path_url).json()
    #     download_url = response['download_url']
    #     return requests.get(download_url).content

    def fetch_data_from_file(self, file_path: str) -> bytes:
        """
        Fetches the PDF file data from the given file path.
        """
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                return file.read()
        else:
            raise Exception(f"Invalid file path: {file_path}")

    def parse_data(self, data: bytes) -> dict:
        return self.__parser.process(data)

    def _normalize_text(self, text: str) -> str:
        """
        Normalize text by lowering case and removing excessive spaces and hyphens.
        """
        return re.sub(r'[\s\-]+', ' ', text.strip().lower())

    def _is_contain_keyword(self, text: str, keywords: List[str]) -> bool:
        """
        Check if the text contains all the keywords.
        """
        normalized_text = self._normalize_text(text)
        for keyword in keywords:
            normalized_keyword = self._normalize_text(keyword)
            if normalized_keyword not in normalized_text:
                return False
        return True

    def _is_title_valid(self, parsed_data: Dict[str, str]) -> bool:
        """
        Check if the title is valid.
        """
        first_page_text = self._normalize_text(parsed_data.get('first_page', ''))
        return self._is_contain_keyword(first_page_text, self.title_keywords)

    def _is_summary_valid(self, parsed_data: Dict[str, str]) -> bool:
        """
        Check if the summary is valid.
        """
        summary_text = self._normalize_text(parsed_data.get('summary_content', ''))
        return self._is_contain_keyword(summary_text, self.summary_keywords)

    def check_report(self, data: dict) -> dict:
        """
        Check the report for validity.
        """
        result = {
            'valid': True,
            'errors': []
        }
        if not self._is_title_valid(data):
            result['valid'] = False
            result['errors'].append('Invalid title')

        if not self._is_summary_valid(data):
            result['valid'] = False
            result['errors'].append('Invalid summary')

        return result


class GitHubParserService(ParserService):
    def fetch_data_from_api(self, path_url: str) -> bytes:
        """
        Fetches the PDF file data from the given URL.
        """
        response = self.__api_client.get(path_url).json()
        download_url = response['download_url']
        return requests.get(download_url).content
