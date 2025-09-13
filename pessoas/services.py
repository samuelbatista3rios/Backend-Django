from .dto import PessoaDTO
from .tasks import PessoaTask
from datetime import datetime

class PessoaService:
    @staticmethod
    def _parse_date(d):
        if isinstance(d, str):
            return datetime.fromisoformat(d).date()
        return d

    @staticmethod
    def incluir(data: dict):
        dto = PessoaDTO(
            nome=data.get('nome'),
            data_nascimento=PessoaService._parse_date(data.get('data_nascimento')),
            cpf=data.get('cpf'),
            sexo=data.get('sexo'),
            altura=float(data.get('altura')) if data.get('altura') is not None else None,
            peso=float(data.get('peso')) if data.get('peso') is not None else None
        )
        return PessoaTask.incluir(dto)

    @staticmethod
    def alterar(data: dict):
        dto = PessoaDTO(
            id=int(data.get('id')),
            nome=data.get('nome'),
            data_nascimento=PessoaService._parse_date(data.get('data_nascimento')),
            cpf=data.get('cpf'),
            sexo=data.get('sexo'),
            altura=float(data.get('altura')) if data.get('altura') is not None else None,
            peso=float(data.get('peso')) if data.get('peso') is not None else None
        )
        return PessoaTask.alterar(dto)

    @staticmethod
    def excluir(id: int):
        return PessoaTask.excluir(id)

    @staticmethod
    def pesquisar(id: int):
        return PessoaTask.pesquisar(id)

    @staticmethod
    def calcular_peso_ideal(data: dict):
        sexo = data.get('sexo')
        altura = float(data.get('altura'))
        if sexo == 'M':
            return (72.7 * altura) - 58
        else:
            return (62.1 * altura) - 44.7
