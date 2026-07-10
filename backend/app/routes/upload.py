from fastapi import APIRouter

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
def upload_circular():
    return {
        "message": "Upload endpoint placeholder."
    }