import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.public.dependecies import get_parser_service
from src.api.public.schemas import GitHubCheckRequest
from src.services.parser import ParserService

logger = logging.getLogger('api')
router = APIRouter()


@router.post("/report/check")
async def validate_report_from_github(request: GitHubCheckRequest,
                                      service: Annotated[ParserService, Depends(get_parser_service)]) -> dict:
    raw_data = service.fetch_data_from_api(request.endpoint)
    parsed_data = service.parse_data(raw_data)
    return service.check_report(parsed_data)
