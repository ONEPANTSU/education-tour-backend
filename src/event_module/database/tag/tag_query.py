from src.database_utils.base_query import BaseQuery
from src.event_module.database.tag.tag_models import TagModels


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
