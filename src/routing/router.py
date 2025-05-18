from fastapi import APIRouter,Depends


from src.services.base_services import main_service

router=APIRouter()

@router.get('/')
def main(response=Depends(main_service)):
    return response