from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_query import BaseQuery
from src.database_utils.cascade_base_response_handler import CascadeBaseResponseHandler
from src.event_module.database.event.event_models import EventModels
from src.event_module.database.event.event_query import EventQuery
from src.event_module.database.event.text.event_data_key import EventDataKey
from src.event_module.database.event.text.event_details import EventDetails
from src.event_module.database.event.text.event_message import EventMessage
from src.event_module.database.event_tag.event_tag_models import EventTagFilter
from src.event_module.database.event_tag.event_tag_query import EventTagQuery
from src.schemas import Response
from src.tour_module.database.tour_event.tour_event_models import TourEventFilter
from src.tour_module.database.tour_event.tour_event_query import TourEventQuery
from src.university_module.database.university_event.university_event_models import (
    UniversityEventFilter,
)
from src.university_module.database.university_event.university_event_query import (
    UniversityEventQuery,
)
from src.utils import Status, return_json


class EventResponseHandler(CascadeBaseResponseHandler):
    _query: EventQuery = EventQuery()
    _message: EventMessage = EventMessage()
    _data_key: EventDataKey = EventDataKey()
    _details: EventDetails = EventDetails()

    _dependencies: dict[BaseQuery, object] = {
        EventTagQuery(): EventTagQuery.dependency_fields[EventTagFilter.EVENT],
        TourEventQuery(): TourEventQuery.dependency_fields[TourEventFilter.EVENT],
        UniversityEventQuery(): UniversityEventQuery.dependency_fields[
            UniversityEventFilter.EVENT
        ],
    }

    _models: EventModels = EventModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    @logger.catch
    async def create(
        self, model_create: _schema_create_class, session: AsyncSession
    ) -> Response:
        try:
            error = await self._query.create(model_create=model_create, session=session)
            if error is None:
                return return_json(
                    status=Status.SUCCESS, message=self._message.get("create_success")
                )
            else:
                raise error
        except IntegrityError as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("create_error"),
                details=self._details.get("wrong_category_id"),
            )

    @logger.catch
    async def get_by_categories(
        self, category_list: list[int], session: AsyncSession
    ) -> Response:
        try:
            events = await self._query.get_by_categories_query(
                category_list=category_list, session=session
            )
            if events is not None:
                data = {
                    self._data_key.get("count"): len(events),
                    self._data_key.get("schemas"): events,
                }
                return return_json(
                    status=Status.SUCCESS,
                    message=self._message.get("get_by_category_success").format(
                        id=category_list
                    ),
                    data=data,
                )
            else:
                raise Exception()
        except Exception as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("get_by_category_error"),
                details=str(e),
            )

    @logger.catch
    async def get_by_category(
        self, category_id: int, session: AsyncSession
    ) -> Response:
        try:
            events = await self._query.get_by_category_query(
                category_id=category_id, session=session
            )
            if events is not None:
                data = {
                    self._data_key.get("count"): len(events),
                    self._data_key.get("schemas"): events,
                }
                return return_json(
                    status=Status.SUCCESS,
                    message=self._message.get("get_by_category_success").format(
                        id=category_id
                    ),
                    data=data,
                )
            else:
                raise Exception()
        except Exception as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("get_by_category_error"),
                details=str(e),
            )
