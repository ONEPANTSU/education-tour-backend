from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_response_handeler import BaseResponseHandler
from src.event_module.database.category.category_models import CategoryModels
from src.event_module.database.category.category_query import CategoryQuery
from src.event_module.database.category.text.category_data_key import CategoryDataKey
from src.event_module.database.category.text.category_details import CategoryDetails
from src.event_module.database.category.text.category_message import CategoryMessage
from src.event_module.database.event.event_query import EventQuery
from src.schemas import Response
from src.utils import Status, return_json


class CategoryResponseHandler(BaseResponseHandler):
    _query: CategoryQuery = CategoryQuery()
    _message: CategoryMessage = CategoryMessage()
    _data_key: CategoryDataKey = CategoryDataKey()
    _details: CategoryDetails = CategoryDetails()

    _models: CategoryModels = CategoryModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    async def delete(self, model_id: int, session: AsyncSession) -> Response:
        try:
            if model_id not in [
                existing_event.category_id
                for existing_event in await EventQuery().get_all(session=session)
            ]:
                if model_id in [
                    existing.id
                    for existing in await self._query.get_all(session=session)
                ]:
                    error = await self._query.delete(model_id=model_id, session=session)
                    if error is None:
                        return return_json(
                            status=Status.SUCCESS,
                            message=self._message.get("delete_success").format(
                                id=model_id
                            ),
                        )
                    else:
                        raise error
                else:
                    return return_json(
                        status=Status.ERROR,
                        message=self._message.get("delete_error").format(id=model_id),
                        details=self._details.get("wrong_id").format(id=model_id),
                    )
            else:
                return return_json(
                    status=Status.ERROR,
                    message=self._message.get("delete_error").format(id=model_id),
                    details=self._details.get("trying_to_delete_foreign_key").format(
                        id=model_id
                    ),
                )
        except IntegrityError as e:
            logger.error(str(e))
            return return_json(
                status=Status.ERROR,
                message=self._message.get("delete_error").format(id=model_id),
            )
