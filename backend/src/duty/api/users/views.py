from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.cursor import CursorPage
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from duty.api.dependencies import get_session
from duty.api.users.schemas import UserSchema
from duty.user.models import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=CursorPage[UserSchema])
async def list_users(db: AsyncSession = Depends(get_session)):
    return await paginate(db, select(User).order_by(User.id))


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return user
