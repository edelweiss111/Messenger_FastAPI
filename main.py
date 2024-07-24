from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from routers import users, messages

app = FastAPI()

app.include_router(users.router)
app.include_router(messages.router)


@app.exception_handler(ValidationError)
async def validation_exeption_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={'detail': exc.errors()},
    )


@app.get('/')
async def read_root():
    return {'message': 'Программа работает'}
