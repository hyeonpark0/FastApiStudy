# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Union[str, None] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

############################################
# 유효성 검사
# 길이 50자 초과 하지 않음

# from typing import Union

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

############################################
# 유효성 검사
# 길이 3자 이상

# from typing import Union

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Union[str, None] = Query(default=None, min_length=3, max_length=50)
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

############################################
# 유효성 검사
# 정규식

# from typing import Union

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Union[str, None] = Query(
#         default=None, min_length=3, max_length=50, regex="^fixedquery$"
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


############################################
# ... 사용

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: str = Query(default=..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


############################################
# 다중 값

# from typing import List, Union

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Union[List[str], None] = Query(default=None)):
#     query_items = {"q": q}
#     return query_items

############################################
# 다중값 : 기본값 여러개

# from typing import List

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: List[str] = Query(default=["foo", "bar"])):
#     query_items = {"q": q}
#     return query_items


############################################
# 다중값 : 기본값 여러개
# List 이용

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: list = Query(default=["ha", "ho", "hu"])):
#     query_items = {"q": q}
#     return query_items

############################################
# 추가 메타데이터 선언

# from typing import Union

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Union[str, None] = Query(
#         default=None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

############################################
# 별칭 매개변수

# from typing import Union

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


############################################
# 매개변수 사용 중단

# from typing import Union

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Union[str, None] = Query(
#         default=None,
#         alias="item-query",
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#         max_length=50,
#         regex="^fixedquery$",
#         deprecated=True,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

############################################
# 자동 문서 생성 사용 안함

from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    hidden_query: Union[str, None] = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}