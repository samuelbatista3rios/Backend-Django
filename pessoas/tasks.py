from .models import Pessoa
from .dto import PessoaDTO

class PessoaTask:
    @staticmethod
    def incluir(dto: PessoaDTO) -> Pessoa:
        pessoa = Pessoa.objects.create(
            nome=dto.nome,
            data_nascimento=dto.data_nascimento,
            cpf=dto.cpf,
            sexo=dto.sexo,
            altura=dto.altura,
            peso=dto.peso
            
        )
        return pessoa

    @staticmethod
    def alterar(dto: PessoaDTO) -> Pessoa:
        pessoa = Pessoa.objects.get(id=dto.id)
        pessoa.nome = dto.nome
        pessoa.data_nascimento = dto.data_nascimento
        pessoa.cpf = dto.cpf
        pessoa.sexo = dto.sexo
        pessoa.altura = dto.altura
        pessoa.peso = dto.peso
        pessoa.save()
        return pessoa

    @staticmethod
    def excluir(id: int):
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return {"deleted": True}

    @staticmethod
    def pesquisar(id: int) -> Pessoa:
        return Pessoa.objects.get(id=id)
