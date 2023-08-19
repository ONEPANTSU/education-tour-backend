from loguru import logger
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.dependent_base_query import DependentBaseQuery
from src.university_module.database.university_tour.university_tour_models import (
    UniversityTourFilter,
    UniversityTourModels,
)


class UniversityTourQuery(DependentBaseQuery):
    _models: UniversityTourModels = UniversityTourModels()

    schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table
    _schema_delete_list_class: type = _models.delete_list_class

    dependency_fields: dict = {
        UniversityTourFilter.UNIVERSITY: _model.university_id,
        UniversityTourFilter.TOUR: _model.tour_id,
    }

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        schema = self._schema_read_class(
            id=model[0].id,
            university_id=model[0].university_id,
            tour_id=model[0].tour_id,
        )
        return schema

    async def get_by_dependency(
        self, dependency_field, value: int, session: AsyncSession
    ) -> list[_schema_read_class] | None:
        try:
            models = await session.execute(
                select(self._model).filter(dependency_field == value)
            )
            schema_list = self._convert_models_to_schema_list(models=models.all())
            return schema_list
        except Exception as e:
            logger.error(str(e))
            return None

    async def delete_by_delete_schema(
        self, model_delete: _schema_delete_list_class, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            for tour_id in model_delete.tour_list:
                await session.execute(
                    delete(self._model).where(
                        (self._model.university_id == model_delete.university_id)
                        & (self._model.tour_id == tour_id)
                    )
                )
            await session.commit()
        except IntegrityError as e:
            return e
