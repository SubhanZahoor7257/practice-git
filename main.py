from fastapi import FastAPI

app = FastAPI()


user_db = {"subhan": "subhan@gmail.com", "zeeshan": "zeeshan@gmail.com"}


@app.get("/user-email")
def root(name: str):
    # return {"message": "Hello World"}
    return user_db[name]


"""
- POST
- GET
- PUT
- PATCH
- DELETE
"""
