from httpx import AsyncClient

from src.event_module.database.category.text.category_message import CategoryMessage
from src.event_module.schemas import CategoryRead
from src.schemas import Response
from src.utils import Status, return_json
from tests.test_event_module.constants.category_constants import CATEGORIES

category_message = CategoryMessage()


async def test_create_category(ac: AsyncClient):
    json = (await ac.post("/event/category/", json={"name": CATEGORIES[0].name})).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    correct_response = return_json(
        status=Status.SUCCESS, message=category_message.get("create_success")
    )
    assert response == correct_response


async def test_get_all_categories(ac: AsyncClient):
    json = (await ac.get("/event/category/")).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    assert response.data["categories_count"] == 1


async def test_get_category_by_id(ac: AsyncClient):
    json = (await ac.get(f"/event/category/{CATEGORIES[0].id}")).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    correct_response = return_json(
        status=Status.SUCCESS,
        message=category_message.get("get_one_success").format(id=CATEGORIES[0].id),
        data={
            "category": CategoryRead(
                id=CATEGORIES[0].id, name=CATEGORIES[0].name
            ).dict()
        },
    )

    assert response == correct_response


async def test_update_category(ac: AsyncClient):
    json = (
        await ac.put(
            f"/event/category/{CATEGORIES[0].id}",
            json={"id": CATEGORIES[0].id, "name": CATEGORIES[0].name},
        )
    ).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    correct_response = return_json(
        status=Status.SUCCESS,
        message=category_message.get("update_success").format(id=CATEGORIES[0].id),
    )

    get_json = (await ac.get(f"/event/category/{CATEGORIES[0].id}")).json()
    updated_name = get_json["data"]["category"]["name"]

    assert response == correct_response and updated_name == CATEGORIES[0].name


async def test_delete_category(ac: AsyncClient):
    json = (
        await ac.delete(
            f"/event/category/{CATEGORIES[0].id}",
        )
    ).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    correct_response = return_json(
        status=Status.SUCCESS,
        message=category_message.get("delete_success").format(id=CATEGORIES[0].id),
    )

    get_json = (await ac.get(f"/event/category/")).json()
    categories_count = get_json["data"]["categories_count"]

    assert response == correct_response and categories_count == 0
