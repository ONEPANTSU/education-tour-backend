from loguru import logger
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.dependent_base_query import DependentBaseQuery
from src.tour_module.database.tour_event.tour_event_models import (
    TourEventFilter,
    TourEventModels,
)


class TourEventQuery(DependentBaseQuery):
    _models: TourEventModels = TourEventModels()

    schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table
    _schema_delete_list_class: type = _models.delete_list_class

    dependency_fields: dict = {
        TourEventFilter.TOUR: _model.tour_id,
        TourEventFilter.EVENT: _model.event_id,
    }

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        schema = self._schema_read_class(
            id=model[0].id,
            tour_id=model[0].tour_id,
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
                        (self._model.tour_id == model_delete.tour_id)
                        & (self._model.event_id == event_id)
                    )
                )
            await session.commit()
        except IntegrityError as e:
            return e
