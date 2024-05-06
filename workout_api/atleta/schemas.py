from pydantic import Field, PositiveFloat
from typing import Annotated, Optional

from workout_api.categoria.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Lucas', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='12345678912', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=12)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.72)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroAtleta, Field(description='Centro de treinamento do atleta')]


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(description='Nome do Atleta', example='Lucas', max_length=50)]
    cpf: Annotated[Optional[str], Field(description='CPF do Atleta', example='12345678912', max_length=11)]
    idade: Annotated[Optional[int], Field(description='Idade do Atleta', example=12)]
    peso: Annotated[Optional[PositiveFloat], Field(description='Peso do Atleta', example=75.5)]