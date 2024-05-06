from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select
from workout_api.centro_treinamento.models import CentroModel
from workout_api.centro_treinamento.schemas import CentroIn, CentroOut
from workout_api.contrib.dependencies import DatabaseDependency
router = APIRouter()

@router.post(
    '/', 
    summary='Criar um novo centro de treinamento', 
    status_code=status.HTTP_201_CREATED,
    response_model=CentroOut,
)
async def post(
    db_session: DatabaseDependency, 
    centro_in: CentroIn = Body(...)
    
) -> CentroOut:
    
    centro_out = CentroOut(id=uuid4(),**centro_in.model_dump() )
    centro_model = CentroModel(**centro_out.model_dump())
    
    db_session.add(centro_model)
    await db_session.commit()
    return centro_out

@router.get(
    '/', 
    summary='Consultar todas centros de treinamento', 
    status_code=status.HTTP_200_OK,
    response_model=list[CentroOut],
)
async def query(db_session: DatabaseDependency) -> list[CentroOut]:
    centro_out: list[CentroOut] = (
        await db_session.execute(select(CentroModel))
        ).scalars().all()
    return centro_out

@router.get(
    '/{id}', 
    summary='Consultar a centro de treinamento pelo ID', 
    status_code=status.HTTP_200_OK,
    response_model=CentroOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> CentroOut:
    centro_out: CentroOut = (
        await db_session.execute(select(CentroModel).filter_by(id=id))
        ).scalars().first()
    
    if not centro_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Centro de treinamento não encontrada'
            )
    return centro_out