from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_response_handler import BaseResponseHandler
from src.schemas import Response
from src.user_module.database.user_university.text.user_university_data_key import (
    UserUniversityDataKey,
)
from src.user_module.database.user_university.text.user_university_details import (
    UserUniversityDetails,
)
from src.user_module.database.user_university.text.user_university_messages import (
    UserUniversityMessage,
)
from src.user_module.database.user_university.user_university_models import (
    UserUniversityModels,
)
from src.user_module.database.user_university.user_university_query import (
    UserUniversityQuery,
)
from src.utils import Status, return_json


class UserUniversityResponseHandler(BaseResponseHandler):
    _query: UserUniversityQuery = UserUniversityQuery()
    _message: UserUniversityMessage = UserUniversityMessage()
    _data_key: UserUniversityDataKey = UserUniversityDataKey()
    _details: UserUniversityDetails = UserUniversityDetails()

    _models: UserUniversityModels = UserUniversityModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _schema_delete_class: type = _models.delete_class
    _model: type = _models.database_table

    async def get_by_filter(
        self,
        user_university_filter,
        value: int,
        session: AsyncSession,
    ) -> Response:
        try:
            schemas = await self._query.get_by_dependency(
                dependency_field=self._query.dependency_fields[user_university_filter],
                value=value,
                session=session,
            )
            if schemas is not None:
                data = {
                    self._data_key.get("schema"): schemas,
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
                        + str(model_delete.university_id)
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
                    + str(model_delete.university_id)
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
