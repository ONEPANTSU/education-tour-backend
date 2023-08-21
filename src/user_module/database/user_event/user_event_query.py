from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.dependent_base_query import DependentBaseQuery
from src.user_module.database.user_event.user_event_models import (
    UserEventFilter,
    UserEventModels,
)


class UserEventQuery(DependentBaseQuery):
    _models: UserEventModels = UserEventModels()

    schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _schema_delete_class: type = _models.delete_class
    _model: type = _models.database_table

    dependency_fields: dict = {
        UserEventFilter.USER: _model.user_id,
        UserEventFilter.EVENT: _model.event_id,
    }

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        schema = self._schema_read_class(
            id=model[0].id,
            user_id=model[0].user_id,
            event_id=model[0].event_id,
        )
        return schema

    async def delete_by_delete_schema(
        self, model_delete: _schema_delete_class, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            await session.execute(
                delete(self._model).where(
                    (self._model.user_id == model_delete.user_id)
                    & (self._model.event_id == model_delete.event_id)
                )
            )
            await session.commit()
        except IntegrityError as e:
            return e

    async def delete_by_user(
        self, user_id: int, session: AsyncSession
    ) -> IntegrityError | None:
        return await self.delete_by_dependency(
            dependency_field=UserEventFilter.USER, value=user_id, session=session
        )