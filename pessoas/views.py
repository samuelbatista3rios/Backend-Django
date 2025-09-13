from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pessoa 
from .services import PessoaService
from .serializers import PessoaSerializer

@api_view(['POST'])
def incluir(request):
    pessoa = PessoaService.incluir(request.data)
    return Response(PessoaSerializer(pessoa).data)

@api_view(['PUT'])
def alterar(request):
    pessoa = PessoaService.alterar(request.data)
    return Response(PessoaSerializer(pessoa).data)

@api_view(['DELETE'])
def excluir(request, id):
    res = PessoaService.excluir(id)
    return Response(res)

@api_view(['GET'])
def listar(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pesquisar(request, id):
    pessoa = PessoaService.pesquisar(id)
    return Response(PessoaSerializer(pessoa).data)

@api_view(['POST'])
def peso_ideal(request):
    valor = PessoaService.calcular_peso_ideal(request.data)
    return Response({"peso_ideal": round(valor, 3)})
