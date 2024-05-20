import io

from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

from src.parsers.base import IParser


class PDFParser(IParser):
    """
    PDFParser class to parse the PDF file and extract the content.
    """
    def _get_pdf_reader(self, content: bytes) -> PdfReader:
        """
        Returns the PDF reader object for the given content.
        """
        return PdfReader(io.BytesIO(content))

    def process(self, content: bytes):
        """

        """
        try:
            reader = self._get_pdf_reader(content)
            num_pages = len(reader.pages)
            parsed_data = {
                'num_pages': num_pages,
                'first_page': '',
                'last_page': '',
                'summary_content': ''
            }

            if num_pages > 0:
                parsed_data['first_page'] = reader.pages[0].extract_text()
                parsed_data['last_page'] = reader.pages[num_pages - 1].extract_text()

            summary_content = []
            for page_num in range(num_pages):
                page_text = reader.pages[page_num].extract_text()
                summary_content.append(page_text)

            parsed_data['summary_content'] = "\n".join(summary_content)
            return parsed_data
        except PdfReadError as e:
            raise ValueError("Failed to read the PDF content: " + str(e))
