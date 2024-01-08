from fastapi import FastAPI
from api.router import router
from src.utils.auth import OAuth2PasswordBearer

app = FastAPI()
app.include_router(router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
