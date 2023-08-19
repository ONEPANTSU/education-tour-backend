from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.dependent_base_query import DependentBaseQuery
from src.university_module.database.university_event.university_event_models import (
    UniversityEventFilter,
    UniversityEventModels,
)


class UniversityEventQuery(DependentBaseQuery):
    _models: UniversityEventModels = UniversityEventModels()

    schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table
    _schema_delete_list_class: type = _models.delete_list_class

    dependency_fields: dict = {
        UniversityEventFilter.UNIVERSITY: _model.university_id,
        UniversityEventFilter.EVENT: _model.event_id,
    }

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        schema = self._schema_read_class(
            id=model[0].id,
            university_id=model[0].university_id,
            event_id=model[0].event_id,
        )
        return schema

    async def delete_by_delete_schema(
        self, model_delete: _schema_delete_list_class, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            for event_id in model_delete.event_list:
                await session.execute(
                    delete(self._model).where(
                        (self._model.university_id == model_delete.university_id)
                        & (self._model.event_id == event_id)
                    )
                )
            await session.commit()
        except IntegrityError as e:
            return e
