from fastapi import APIRouter

router = APIRouter(prefix="/extract", tags=["Extraction"])


@router.post("/")
def extract_obligations():
    return {
        "message": "Obligation extraction placeholder."
    }