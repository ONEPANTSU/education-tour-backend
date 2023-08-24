from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.cascade_base_response_handler import CascadeBaseResponseHandler
from src.event_module.database.event_tag.event_tag_models import EventTagFilter
from src.event_module.database.event_tag.event_tag_query import EventTagQuery
from src.event_module.database.tag.tag_models import TagModels
from src.event_module.database.tag.tag_query import TagQuery
from src.event_module.database.tag.text.tag_data_key import TagDataKey
from src.event_module.database.tag.text.tag_details import TagDetails
from src.event_module.database.tag.text.tag_message import TagMessage
from src.schemas import Response
from src.utils import Status, return_json


class TagResponseHandler(CascadeBaseResponseHandler):
    _query: TagQuery = TagQuery()
    _message: TagMessage = TagMessage()
    _data_key: TagDataKey = TagDataKey()
    _details: TagDetails = TagDetails()

    _dependencies: dict[EventTagQuery, object] = {
        EventTagQuery(): EventTagQuery.dependency_fields[EventTagFilter.TAG]
    }

    _models: TagModels = TagModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    async def get_by_filter(
        self,
        event_id: int | None,
        session: AsyncSession,
    ) -> Response:
        try:
            schemas = await self._query.get_by_filter_query(
                event_id=event_id,
                session=session,
            )
            if schemas is not None:
                data = {
                    self._data_key.get("count"): len(schemas),
                    self._data_key.get("schemas"): schemas,
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
