from loguru import logger
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.dependent_base_query import DependentBaseQuery
from src.event_module.database.event_tag.event_tag_models import (
    EventTagFilter,
    EventTagModels,
)
from src.event_module.schemas import EventTagListDelete


class EventTagQuery(DependentBaseQuery):
    _models: EventTagModels = EventTagModels()

    schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    dependency_fields: dict = {
        EventTagFilter.EVENT: _model.event_id,
        EventTagFilter.TAG: _model.tag_id,
    }

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        schema = self._schema_read_class(
            id=model[0].id,
            event_id=model[0].event_id,
            tag_id=model[0].tag_id,
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
        self, model_delete: EventTagListDelete, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            for tag_id in model_delete.tag_list:
                await session.execute(
                    delete(self._model).where(
                        self._model.event_id == model_delete.event_id
                        and self._model.tag_id == tag_id
                    )
                )
            await session.commit()
        except IntegrityError as e:
            return e
