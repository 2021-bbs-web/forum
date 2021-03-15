from fastapi import FastAPI
from user import UserManager


app = FastAPI()
user_manager = UserManager()


@app.get("/api/")
def api():
    return {"code": 0, "msg": "OK", "user": user_manager.get_user_num()}
