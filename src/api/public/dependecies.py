from src.config.integrations import github_settings
from src.config.parser import parser_settings
from src.intergrations.base import ApiClient, IApiClient
from src.parsers.base import IParser
from src.parsers.pdf_parser import PDFParser
from src.services.parser import GitHubParserService, IParserService, ParserService


async def get_parser_service() -> IParserService:
    """
    Initialize the PDF Parser Service instance.
    """
    parser: IParser = PDFParser()
    github_api_client: IApiClient = ApiClient(
        protocol=github_settings.GITHUB_PROTOCOL,
        host=github_settings.GITHUB_HOST,
        headers={'Accept': 'application/vnd.github.v3+json'}
    )
    return GitHubParserService(
        parser=parser,
        api_client=github_api_client,
        title_keywords=parser_settings.TITLE_KEYWORDS,
        summary_keywords=parser_settings.SUMMARY_KEYWORDS
    )
