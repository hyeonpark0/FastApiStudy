# 어노테이션 라이브러리를 이용하여 유효성 설정
from typing import Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# q와 item_id 둘다 필수일때 순서는 상관없다
# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# annotated
# from fastapi import FastAPI, Path
# from typing_extensions import Annotated

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import FastAPI, Path
# from typing_extensions import Annotated

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import FastAPI, Path
# from typing_extensions import Annotated
# from typing import Union

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[Union[int, None], Path(title="The ID of the item to get", le=10)], q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import FastAPI, Path
# from typing_extensions import Annotated

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", le=1000)],
#     q: str,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import FastAPI, Path, Query
# from typing_extensions import Annotated

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     *, item_id: int = Path(title="The ID of the item to get", ge=1, le=100), q: int = Path(title="IDKIDK", gt=3)
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results