from flask import Response
from flask_restful import Resource

from app import api
from ..common import (EMAIL_PARSER_API, Messenger, DefaultAPIResponseSchema)
from ..core import EmailParserService, FilterEmailOnSubjectNameandAttachmentTypeService, ExtractDataFromXlsxFileService


@api.route(EMAIL_PARSER_API)
class EmailParser(Resource):
    def __init__(self):
        self.message = Messenger()

    def get(self, **kwargs):
        "It will process a GET request from url '/api/email-parser'"

        service = EmailParserService(self.message, FilterEmailOnSubjectNameandAttachmentTypeService,
                                     ExtractDataFromXlsxFileService)
        service.read_emails()
        response = DefaultAPIResponseSchema().dumps(None)
        return Response(response, mimetype="application/json")
