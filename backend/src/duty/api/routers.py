from fastapi import APIRouter

from duty.api.users.views import router as users_router

router = APIRouter(prefix="/api/v1")
router.include_router(users_router)
