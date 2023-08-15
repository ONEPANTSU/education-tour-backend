from abc import ABC, abstractmethod

from loguru import logger
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database_utils.base_models import BaseModels


class AbstractBaseQuery(ABC):
    _models: BaseModels = BaseModels()

    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    @abstractmethod
    async def create(
        self, model_create: _schema_create_class, session: AsyncSession
    ) -> IntegrityError | None:
        pass

    @abstractmethod
    async def get_all(self, session: AsyncSession) -> list[_schema_read_class] | None:
        pass

    @abstractmethod
    async def get_by_id(
        self, model_id: int, session: AsyncSession
    ) -> _schema_read_class | None:
        pass

    @abstractmethod
    async def update(
        self, model_update: _schema_update_class, session: AsyncSession
    ) -> IntegrityError | None:
        pass

    @abstractmethod
    async def delete(
        self, model_id: int, session: AsyncSession
    ) -> IntegrityError | None:
        pass


class BaseQuery(AbstractBaseQuery):
    _models: BaseModels = BaseModels()

    _schema_create_class: type = _models.create_class
    _schema_update_class: type = _models.update_class
    _schema_read_class: type = _models.read_class
    _model: type = _models.database_table

    async def create(
        self, model_create: _schema_create_class, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            await session.execute(insert(self._model).values(**model_create.dict()))
            await session.commit()
        except IntegrityError as e:
            return e

    def _convert_model_to_schema(self, model: _model) -> _schema_read_class | None:
        schema: BaseQuery._schema_read_class = self._schema_read_class(id=model.id)
        return schema

    def _convert_models_to_schema_list(
        self, models: list[_model]
    ) -> list[_schema_read_class] | None:
        return [self._convert_model_to_schema(model=model) for model in models]

    async def get_all(self, session: AsyncSession) -> list[_schema_read_class] | None:
        try:
            logger.warning(self._model)
            models = await session.execute(select(self._model))
            schema_list = self._convert_models_to_schema_list(models=models.all())
            return schema_list
        except Exception as e:
            logger.error(str(e))
            return None

    async def get_by_id(
        self, model_id: int, session: AsyncSession
    ) -> _schema_read_class | None:
        try:
            models = await session.execute(
                select(self._model).filter(self._model.id == model_id)
            )
            schema = self._convert_model_to_schema(model=models.one())
            return schema
        except Exception as e:
            logger.error(str(e))
            return None

    async def update(
        self, model_update: _schema_update_class, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            await session.execute(
                update(self._model)
                .values(**model_update.dict())
                .where(self._model.id == model_update.id)
            )
            await session.commit()
        except IntegrityError as e:
            return e

    async def delete(
        self, model_id: int, session: AsyncSession
    ) -> IntegrityError | None:
        try:
            await session.execute(delete(self._model).where(self._model.id == model_id))
            await session.commit()
        except IntegrityError as e:
            return e
