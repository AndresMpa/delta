from fastapi import APIRouter

router = APIRouter(
    prefix="/files",
    responses={404: {"description": "Data not found"}},
)


@router.get("/")
async def read_files():
    return {"data": "This is going to be a file"}
