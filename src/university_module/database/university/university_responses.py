from src.database_utils.base_query import BaseQuery
from src.database_utils.cascade_base_response_handler import CascadeBaseResponseHandler
from src.university_module.database.university.text.university_data_key import (
    UniversityDataKey,
)
from src.university_module.database.university.text.university_details import (
    UniversityDetails,
)
from src.university_module.database.university.text.university_messages import (
    UniversityMessage,
)
from src.university_module.database.university.university_models import UniversityModels
from src.university_module.database.university.university_query import UniversityQuery
from src.university_module.database.university_event.university_event_models import (
    UniversityEventFilter,
)
from src.university_module.database.university_event.university_event_query import (
    UniversityEventQuery,
)
from src.university_module.database.university_tour.university_tour_models import (
    UniversityTourFilter,
)
from src.university_module.database.university_tour.university_tour_query import (
    UniversityTourQuery,
)


class UniversityResponseHandler(CascadeBaseResponseHandler):
    _query: UniversityQuery = UniversityQuery()
    _message: UniversityMessage = UniversityMessage()
    _data_key: UniversityDataKey = UniversityDataKey()
    _details: UniversityDetails = UniversityDetails()

    _dependencies: dict[BaseQuery, object] = {
        UniversityEventQuery(): UniversityEventQuery.dependency_fields[
            UniversityEventFilter.UNIVERSITY
        ],
        UniversityTourQuery(): UniversityTourQuery.dependency_fields[
            UniversityTourFilter.UNIVERSITY
        ],
    }

    _models: UniversityModels = UniversityModels()
    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table
