from src.database_utils.cascade_base_response_handler import CascadeBaseResponseHandler
from src.event_module.database.event_tag.event_tag_models import EventTagFilter
from src.event_module.database.event_tag.event_tag_query import EventTagQuery
from src.event_module.database.tag.tag_models import TagModels
from src.event_module.database.tag.tag_query import TagQuery
from src.event_module.database.tag.text.tag_data_key import TagDataKey
from src.event_module.database.tag.text.tag_details import TagDetails
from src.event_module.database.tag.text.tag_message import TagMessage


class TagResponseHandler(CascadeBaseResponseHandler):
    _query: TagQuery = TagQuery()
    _message: TagMessage = TagMessage()
    _data_key: TagDataKey = TagDataKey()
    _details: TagDetails = TagDetails()

    _dependencies: dict[EventTagQuery, object] = {
        EventTagQuery(): EventTagQuery.dependency_fields[EventTagFilter.TAG]
    }

    _models: TagModels = TagModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table
