#############################################
# 기본

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# # async def read_item(item_id):
# async def read_item(item_id : int):
#     return {"item_id": item_id}

#############################################
# 중복 주소 일 때

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

#############################################
# enum 사용


# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

#############################################
# 경로 변환

from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# 매개변수가 /home/johndoe/myfile.txt를 갖고 있어 슬래시로 시작(/)해야 할 수 있습니다.

# 이 경우 URL은: /files//home/johndoe/myfile.txt이며 files과 home 사이에 이중 슬래시(//)가 생깁니다.