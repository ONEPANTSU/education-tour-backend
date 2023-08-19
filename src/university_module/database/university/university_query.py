import json

from sqlalchemy import insert, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.address_schema import Address
from src.database_utils.base_query import BaseQuery
from src.university_module.database.university.university_models import UniversityModels


class UniversityQuery(BaseQuery):
    _models: UniversityModels = UniversityModels()

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
            url=model[0].url,
            phone=model[0].phone,
            email=model[0].email,
            address=address,
            description=model[0].description,
            reg_date=model[0].reg_date,
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
