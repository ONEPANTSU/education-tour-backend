from abc import ABC

from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_models import BaseModels
from src.database_utils.base_query import BaseQuery
from src.database_utils.text.base_data_key import BaseDataKey
from src.database_utils.text.base_details import BaseDetails
from src.database_utils.text.base_message import BaseMessage
from src.schemas import Response
from src.utils import Status, return_json


class BaseResponseHandler(ABC):
    _query: BaseQuery = BaseQuery()
    _message: BaseMessage = BaseMessage()
    _data_key: BaseDataKey = BaseDataKey()
    _details: BaseDetails = BaseDetails()

    _models: BaseModels = BaseModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    async def get_all(self, session: AsyncSession) -> Response:
        try:
            schemas = await self._query.get_all(session=session)
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

    async def get_by_id(self, model_id: int, session: AsyncSession) -> Response:
        try:
            schema = await self._query.get_by_id(model_id=model_id, session=session)
            if schema is not None:
                data = {self._data_key.get("schema"): schema}
                return return_json(
                    status=Status.SUCCESS,
                    message=self._message.get("get_one_success").format(id=model_id),
                    data=data,
                )
            else:
                raise Exception()
        except Exception as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("get_one_error").format(id=model_id),
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
            )

    async def update(
        self, model_update: _schema_update_class, session: AsyncSession
    ) -> Response:
        try:
            if model_update.id in [
                existing.id for existing in await self._query.get_all(session=session)
            ]:
                error = await self._query.update(
                    model_update=model_update, session=session
                )
                if error is None:
                    return return_json(
                        status=Status.SUCCESS,
                        message=self._message.get("update_success").format(
                            id=model_update.id
                        ),
                    )
                else:
                    raise error
            else:
                return return_json(
                    status=Status.ERROR,
                    message=self._message.get("update_error").format(
                        id=model_update.id
                    ),
                    details=self._details.get("wrong_id").format(id=model_update.id),
                )
        except IntegrityError as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("update_error").format(id=model_update.id),
            )

    @logger.catch
    async def delete(self, model_id: int, session: AsyncSession) -> Response:
        try:
            if model_id in [
                existing.id for existing in await self._query.get_all(session=session)
            ]:
                error = await self._query.delete(model_id=model_id, session=session)
                if error is None:
                    return return_json(
                        status=Status.SUCCESS,
                        message=self._message.get("delete_success").format(id=model_id),
                    )
                else:
                    raise error
            else:
                return return_json(
                    status=Status.ERROR,
                    message=self._message.get("delete_error").format(id=model_id),
                    details=self._details.get("wrong_id").format(id=model_id),
                )
        except IntegrityError as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("delete_error").format(id=model_id),
            )
