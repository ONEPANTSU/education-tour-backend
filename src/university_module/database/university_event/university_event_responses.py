from loguru import logger
from sqlalchemy import Enum
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_response_handler import BaseResponseHandler
from src.schemas import Response
from src.university_module.database.university_event.text.university_event_data_key import (
    UniversityEventDataKey,
)
from src.university_module.database.university_event.text.university_event_details import (
    UniversityEventDetails,
)
from src.university_module.database.university_event.text.university_event_messages import (
    UniversityEventMessage,
)
from src.university_module.database.university_event.university_event_models import (
    UniversityEventFilter,
    UniversityEventModels,
)
from src.university_module.database.university_event.university_event_query import (
    UniversityEventQuery,
)
from src.utils import Status, return_json


class UniversityEventResponseHandler(BaseResponseHandler):
    _query: UniversityEventQuery = UniversityEventQuery()
    _message: UniversityEventMessage = UniversityEventMessage()
    _data_key: UniversityEventDataKey = UniversityEventDataKey()
    _details: UniversityEventDetails = UniversityEventDetails()

    _models: UniversityEventModels = UniversityEventModels()
    _schema_create_class: type = _models.create_class

    _schema_delete_list_class: type = _models.delete_list_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    _schema_create_list_class: type = _models.create_list_class
    _schema_read_event_list_class: type = _models.read_event_list_class

    _readable_schema_filter: dict[Enum, type] = {
        UniversityEventFilter.UNIVERSITY: _schema_read_event_list_class,
    }

    async def create_list(
        self, model_create: _schema_create_list_class, session: AsyncSession
    ) -> Response:
        try:
            university_event_filter = UniversityEventFilter.UNIVERSITY

            schemas = await self._query.get_by_dependency(
                dependency_field=self._query.dependency_fields[university_event_filter],
                value=model_create.university_id,
                session=session,
            )
            if schemas is not None:
                readable_schemas = self._readable_schema_filter[
                    university_event_filter
                ]()
                readable_schemas.set_by_university_event_read(
                    university_event_read_list=schemas
                )
                for index in range(model_create.event_list):
                    if model_create.event_list[index] in readable_schemas.event_id_list:
                        model_create.event_list.pop(index)

            for (
                university_event_create
            ) in model_create.get_university_event_create_list():
                error = await self._query.create(
                    model_create=university_event_create, session=session
                )
                if error is not None:
                    raise error
            return return_json(
                status=Status.SUCCESS,
                message=self._message.get("create_success"),
            )
        except IntegrityError as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("create_error"),
            )

    async def get_by_filter(
        self,
        value: int,
        session: AsyncSession,
        university_event_filter: UniversityEventFilter = UniversityEventFilter.UNIVERSITY,
    ) -> Response:
        try:
            schemas = await self._query.get_by_dependency(
                dependency_field=self._query.dependency_fields[university_event_filter],
                value=value,
                session=session,
            )

            if schemas is not None:
                readable_schemas = self._readable_schema_filter[
                    university_event_filter
                ]()
                readable_schemas.set_by_university_event_read(
                    university_event_read_list=schemas
                )
                data = {
                    self._data_key.get("count"): len(schemas),
                    self._data_key.get("schemas"): readable_schemas,
                }
                return return_json(
                    status=Status.SUCCESS,
                    message=self._message.get("get_all_success"),
                    data=data,
                )
            else:
                raise Exception()

        except Exception as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("get_all_error"),
                details=str(e),
            )

    async def delete_by_delete_schema(
        self, model_delete: _schema_delete_list_class, session: AsyncSession
    ) -> Response:
        try:
            error = await self._query.delete_by_delete_schema(
                model_delete=model_delete, session=session
            )
            if error is None:
                return return_json(
                    status=Status.SUCCESS,
                    message=self._message.get("delete_success").format(
                        id="("
                        + str(model_delete.university_id)
                        + " - "
                        + str(model_delete.event_list)
                        + ")"
                    ),
                )
            else:
                raise error
        except IntegrityError as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("delete_error").format(
                    id="("
                    + str(model_delete.university_id)
                    + " - "
                    + str(model_delete.event_list)
                    + ")"
                ),
            )
