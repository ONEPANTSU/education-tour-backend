from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from src.database_utils.base_models import BaseModels
from src.database_utils.base_query import BaseQuery


class DependentBaseQuery(BaseQuery):
    _models: BaseModels = BaseModels()

    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    dependency_fields: dict[str, object] = {
        "id": _model  # The Plug (It has to be a field of the model, e.g. _model.id)
    }

    async def delete_by_dependency(
        self, dependency_field, value: int, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            await session.execute(delete(self._model).where(dependency_field == value))
            await session.commit()
        except IntegrityError as e:
            return e

    def get_schema_create_class(self) -> type:
        return self._schema_create_class
