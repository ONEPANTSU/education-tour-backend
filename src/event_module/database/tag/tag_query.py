from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_query import BaseQuery
from src.event_module.database.tag.tag_models import TagModels
from src.event_module.models import EventTag


class TagQuery(BaseQuery):
    _models: TagModels = TagModels()

    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        schema = self._schema_read_class(
            id=model[0].id,
            name=model[0].name,
        )
        return schema

    async def get_by_filter_query(
        self, event_id: int | None, session: AsyncSession
    ) -> list[_schema_read_class] | None:
        try:
            statement = select(self._model)
            if event_id is not None:
                statement = statement.join(
                    EventTag, EventTag.tag_id == self._model.id
                ).filter(EventTag.event_id == event_id)

            tag_rows = await session.execute(statement)
            return self._convert_models_to_schema_list(models=tag_rows.all())
        except Exception as e:
            logger.error(str(e))
            return None
