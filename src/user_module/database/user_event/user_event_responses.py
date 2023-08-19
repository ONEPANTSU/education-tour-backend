from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_response_handler import BaseResponseHandler
from src.schemas import Response
from src.user_module.database.user_event.text.user_event_data_key import (
    UserEventDataKey,
)
from src.user_module.database.user_event.text.user_event_details import UserEventDetails
from src.user_module.database.user_event.text.user_event_messages import (
    UserEventMessage,
)
from src.user_module.database.user_event.user_event_models import (
    UserEventFilter,
    UserEventModels,
)
from src.user_module.database.user_event.user_event_query import UserEventQuery
from src.utils import Status, return_json


class UserEventResponseHandler(BaseResponseHandler):
    _query: UserEventQuery = UserEventQuery()
    _message: UserEventMessage = UserEventMessage()
    _data_key: UserEventDataKey = UserEventDataKey()
    _details: UserEventDetails = UserEventDetails()

    _models: UserEventModels = UserEventModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _schema_delete_class: type = _models.delete_class
    _model: type = _models.database_table

    _readable_schema_filter = {
        UserEventFilter.USER: _models.read_event_list_class,
        UserEventFilter.EVENT: _models.read_user_list_class,
    }

    async def get_by_filter(
        self,
        user_event_filter,
        value: int,
        session: AsyncSession,
    ) -> Response:
        try:
            schemas = await self._query.get_by_dependency(
                dependency_field=self._query.dependency_fields[user_event_filter],
                value=value,
                session=session,
            )
            if schemas is not None:
                readable_schemas = self._readable_schema_filter[user_event_filter]()
                readable_schemas.set_by_user_event_read(user_event_read_list=schemas)
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
        self, model_delete: _schema_delete_class, session: AsyncSession
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
                        + str(model_delete.user_id)
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
                    + str(model_delete.user_id)
                    + " - "
                    + str(model_delete.event_list)
                    + ")"
                ),
            )

    async def delete_by_user(self, user_id: int, session: AsyncSession) -> Response:
        try:
            error = await self._query.delete_by_user(user_id=user_id, session=session)
            if error is None:
                return return_json(
                    status=Status.SUCCESS,
                    message=self._message.get("delete_success").format(
                        id="(user_id=" + str(user_id) + ")"
                    ),
                )
            else:
                raise error
        except IntegrityError as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("delete_success").format(
                    id="(user_id=" + str(user_id) + ")"
                ),
            )
