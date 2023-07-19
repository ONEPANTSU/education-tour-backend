from httpx import AsyncClient

from src.event_module.utils.event.text.messages import MESSAGE
from src.schemas import Response
from src.utils import Status, return_json
from tests.test_event_module.constants.event_constants import (
    CATEGORIES,
    EVENTS_CREATE,
    EVENTS_READ,
    EVENTS_UPDATE,
)


async def test_create_event(ac: AsyncClient):
    await ac.post("/event/category/", json={"name": CATEGORIES[0].name})
    await ac.post("/event/category/", json={"name": CATEGORIES[1].name})
    json = (await ac.post("/event/", json=EVENTS_CREATE[0])).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    correct_response = return_json(
        status=Status.SUCCESS, message=MESSAGE["create_event_success"]
    )
    assert response == correct_response


async def test_get_all_events(ac: AsyncClient):
    await ac.post("/event/", json=EVENTS_CREATE[1])
    json = (await ac.get("/event/")).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    assert response.data["events_count"] == 2


async def test_get_event_by_id(ac: AsyncClient):
    json = (await ac.get(f"/event/{EVENTS_READ[1]['id']}")).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    correct_response = return_json(
        status=Status.SUCCESS,
        message=MESSAGE["get_one_event_success"].format(event_id=EVENTS_READ[1]["id"]),
        data={"event": EVENTS_READ[1]},
    )

    assert response == correct_response


async def test_get_events_by_category(ac: AsyncClient):
    json = (
        await ac.get(f"/event/category_filter/{EVENTS_READ[1]['category_id']}")
    ).json()
    response = Response(
        status=json["status"],
        message=json["message"],
        data=json["data"],
        details=json["details"],
    )
    correct_response = return_json(
        status=Status.SUCCESS,
        message=MESSAGE["get_events_by_category_success"].format(
            category_id=EVENTS_READ[1]["category_id"]
        ),
        data={"events_count": 1, "events": [EVENTS_READ[1]]},
    )

    assert response == correct_response


async def test_get_events_by_categories(ac: AsyncClient):
    json = (
        await ac.get(
            f"/event/category_filter/?category_list={EVENTS_READ[0]['category_id']}&category_list={EVENTS_READ[1]['category_id']}"
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
        message=MESSAGE["get_events_by_category_success"].format(
            category_id=[EVENTS_READ[0]["category_id"], EVENTS_READ[1]["category_id"]]
        ),
        data={"events_count": 2, "events": EVENTS_READ},
    )

    assert response == correct_response


async def test_update_event(ac: AsyncClient):
    json = (
        await ac.put(
            f"/event/{EVENTS_UPDATE[0]['id']}",
            json=EVENTS_UPDATE[0],
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
        message=MESSAGE["update_event_success"].format(event_id=EVENTS_UPDATE[0]["id"]),
    )

    get_json = (await ac.get(f"/event/{EVENTS_UPDATE[0]['id']}")).json()
    updated_name = get_json["data"]["event"]["name"]

    assert response == correct_response and updated_name == EVENTS_UPDATE[0]["name"]


async def test_delete_event(ac: AsyncClient):
    json = (
        await ac.delete(
            f"/event/{EVENTS_READ[0]['id']}",
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
        message=MESSAGE["delete_event_success"].format(event_id=EVENTS_READ[0]["id"]),
    )

    await ac.delete(
        f"/event/{EVENTS_READ[1]['id']}",
    )

    await ac.delete(
        f"/event/category/{CATEGORIES[0].id}",
    )
    await ac.delete(
        f"/event/category/{CATEGORIES[1].id}",
    )

    get_json = (await ac.get(f"/event/")).json()
    events_count = get_json["data"]["events_count"]

    assert response == correct_response and events_count == 0
