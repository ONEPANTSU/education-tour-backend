from enum import Enum

from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_response_handeler import BaseResponseHandler
from src.event_module.database.event_tag.event_tag_models import (
    EventTagFilter,
    EventTagModels,
)
from src.event_module.database.event_tag.event_tag_query import EventTagQuery
from src.event_module.database.event_tag.text.event_tag_data_key import EventTagDataKey
from src.event_module.database.event_tag.text.event_tag_details import EventTagDetails
from src.event_module.database.event_tag.text.event_tag_message import EventTagMessage
from src.event_module.schemas import EventListRead, EventTagListDelete, TagListRead
from src.schemas import Response
from src.utils import Status, return_json


class EventTagResponseHandler(BaseResponseHandler):
    _query: EventTagQuery = EventTagQuery()
    _message: EventTagMessage = EventTagMessage()
    _data_key: EventTagDataKey = EventTagDataKey()
    _details: EventTagDetails = EventTagDetails()

    _models: EventTagModels = EventTagModels()
    _schema_create_class: type = _models.create_class

    _schema_delete_list_class: type = _models.delete_list_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    _schema_create_list_class: type = _models.create_list_class
    _schema_read_tag_list_class: type = _models.read_tag_list_class
    _schema_read_event_list_class: type = _models.read_event_list_class

    _readable_schema_filter: dict[Enum, type] = {
        EventTagFilter.TAG: EventListRead,
        EventTagFilter.EVENT: TagListRead,
    }

    async def create_list(
        self, model_create: _schema_create_list_class, session: AsyncSession
    ) -> Response:
        try:
            for event_tag_create in model_create.get_event_tag_create_list():
                error = await self._query.create(
                    model_create=event_tag_create, session=session
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
        self, event_tag_filter: EventTagFilter, value: int, session: AsyncSession
    ) -> Response:
        try:
            schemas = await self._query.get_by_dependency(
                dependency_field=self._query.dependency_fields[event_tag_filter],
                value=value,
                session=session,
            )

            if schemas is not None:
                readable_schemas = self._readable_schema_filter[event_tag_filter]()
                readable_schemas.set_by_event_tag_read(event_tag_read_list=schemas)
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
        self, model_delete: EventTagListDelete, session: AsyncSession
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
                        + str(model_delete.event_id)
                        + " - "
                        + str(model_delete.tag_list)
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
                    + str(model_delete.event_id)
                    + " - "
                    + str(model_delete.tag_list)
                    + ")"
                ),
            )
