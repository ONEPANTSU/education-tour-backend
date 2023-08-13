from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_models import BaseModels
from src.database_utils.base_query import BaseQuery
from src.database_utils.base_response_handeler import BaseResponseHandler
from src.database_utils.dependent_base_query import DependentBaseQuery
from src.database_utils.text.base_data_key import BaseDataKey
from src.database_utils.text.base_details import BaseDetails
from src.database_utils.text.base_message import BaseMessage
from src.schemas import Response


class CascadeBaseResponseHandler(BaseResponseHandler):
    """
    Cascade Delete Base Class
    """

    _query: BaseQuery = BaseQuery()

    _dependencies: dict[DependentBaseQuery, object] = {
        DependentBaseQuery(): DependentBaseQuery.dependency_fields["id"]
    }

    _message: BaseMessage = BaseMessage()
    _data_key: BaseDataKey = BaseDataKey()
    _details: BaseDetails = BaseDetails()

    _models: BaseModels = BaseModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    async def delete(self, model_id: int, session: AsyncSession) -> Response:
        for query, field in self._dependencies.items():
            await query.delete_by_dependency(
                dependency_field=field, value=model_id, session=session
            )
        return await super().delete(model_id=model_id, session=session)
