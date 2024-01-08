from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from api.src.endpoints import goods
from api.src.utils.auth import create_jwt_token, get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login")
async def login(form_data: OAuth2PasswordBearer = Depends(oauth2_scheme)):
    token = create_jwt_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/secure-item")
async def get_secure_item(current_user: dict = Depends(get_current_user)):
    return {"message": "This is a secure item!", "user": current_user}
