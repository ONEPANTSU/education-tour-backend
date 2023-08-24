from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_query import BaseQuery
from src.database_utils.cascade_base_response_handler import CascadeBaseResponseHandler
from src.schemas import Response
from src.tour_module.database.tour.text.tour_data_key import TourDataKey
from src.tour_module.database.tour.text.tour_details import TourDetails
from src.tour_module.database.tour.text.tour_message import TourMessage
from src.tour_module.database.tour.tour_models import TourModels
from src.tour_module.database.tour.tour_query import TourQuery
from src.tour_module.database.tour_event.tour_event_models import TourEventFilter
from src.tour_module.database.tour_event.tour_event_query import TourEventQuery
from src.university_module.database.university_tour.university_tour_models import (
    UniversityTourFilter,
)
from src.university_module.database.university_tour.university_tour_query import (
    UniversityTourQuery,
)
from src.user_module.database.user_tour.user_tour_models import UserTourFilter
from src.user_module.database.user_tour.user_tour_query import UserTourQuery
from src.utils import Status, return_json


class TourResponseHandler(CascadeBaseResponseHandler):
    _query: TourQuery = TourQuery()
    _message: TourMessage = TourMessage()
    _data_key: TourDataKey = TourDataKey()
    _details: TourDetails = TourDetails()

    _dependencies: dict[BaseQuery, object] = {
        TourEventQuery(): TourEventQuery.dependency_fields[TourEventFilter.TOUR],
        UniversityTourQuery(): UniversityTourQuery.dependency_fields[
            UniversityTourFilter.TOUR
        ],
        UserTourQuery(): UserTourQuery.dependency_fields[UserTourFilter.TOUR],
    }

    _models: TourModels = TourModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    async def get_by_filter(
        self,
        university_id: int | None,
        session: AsyncSession,
    ) -> Response:
        try:
            schemas = await self._query.get_by_filter_query(
                university_id=university_id,
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
                details=self._details.get("wrong_event_id"),
            )
