from pydantic import UUID4, Field
from typing import Annotated

from workout_api.contrib.schemas import BaseSchema

class CentroIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='Campo Cotia', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco', example='Rua 1', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do Proprietario', example='Lucas', max_length=30)]
    
class CentroAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Centro de treinamento', example='CT KING', max_length=20)]

class CentroOut(CentroIn):
    id: Annotated[UUID4, Field(description='Identificador da Centro de treinamento')]