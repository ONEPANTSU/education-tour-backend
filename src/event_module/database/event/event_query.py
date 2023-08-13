import json

from loguru import logger
from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.address_schema import Address
from src.database_utils.base_query import BaseQuery
from src.event_module.database.event.event_models import EventModels
from src.event_module.models import Event
from src.event_module.schemas import EventRead


class EventQuery(BaseQuery):
    _models: EventModels = EventModels()

    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    async def create(
        self, model_create: _schema_create_class, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            model_create.fix_time()
            await session.execute(insert(self._model).values(**model_create.dict()))
            await session.commit()
        except IntegrityError as e:
            return e

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        if type(model[0].address) is str:
            address = Address(**json.loads(model[0].address))
        else:
            address = model[0].address
        schema = self._schema_read_class(
            id=model[0].id,
            name=model[0].name,
            description=model[0].description,
            date_start=model[0].date_start,
            date_end=model[0].date_end,
            reg_deadline=model[0].reg_deadline,
            max_users=model[0].max_users,
            category_id=model[0].category_id,
            address=address,
        )
        return schema

    async def update(
        self, model_update: _schema_update_class, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            model_update.fix_time()
            await session.execute(
                update(self._model)
                .values(**model_update.dict())
                .where(self._model.id == model_update.id)
            )
            await session.commit()
        except IntegrityError as e:
            return e

    async def get_by_categories_query(
        self, category_list: list[int], session: AsyncSession
    ) -> list[EventRead] | None:
        try:
            events = []
            for category_id in category_list:
                event_rows = await session.execute(
                    select(Event).filter(Event.category_id == category_id)
                )
                events += self._convert_models_to_schema_list(models=event_rows.all())
            return events
        except Exception as e:
            logger.error(str(e))
            return None

    async def get_by_category_query(
        self, category_id: int, session: AsyncSession
    ) -> list[EventRead] | None:
        try:
            event_rows = await session.execute(
                select(Event).filter(Event.category_id == category_id)
            )
            events = self._convert_models_to_schema_list(models=event_rows.all())
            return events
        except Exception as e:
            logger.error(str(e))
            return None
