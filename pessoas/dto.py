from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class PessoaDTO:
    id: Optional[int] = None
    nome: Optional[str] = None
    data_nascimento: Optional[date] = None  
    cpf: Optional[str] = None
    sexo: Optional[str] = None
    altura: Optional[float] = None
    peso: Optional[float] = None
