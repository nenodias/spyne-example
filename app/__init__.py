from pdb import set_trace
from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import ServiceBase

from spyne.model.complex import ComplexModel
from spyne.model.complex import Array
from spyne.model.primitive import Integer
from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String


class Resposta(ComplexModel):
   __namespace__ = "response"
   mensagem = String()
   sucesso = Integer()

class Endereco(ComplexModel):
    __namespace__ = "address"
    cidade = String
    numero = Integer
    rua = String

class Usuario(ComplexModel):
   __namespace__ = "user"

   nome = String
   endereco = Array(Endereco)

class Agenda(ComplexModel):
   __namespace__ = "agenda"
   usuario = Usuario

class AppService(ServiceBase):

    @rpc(String, UnsignedInteger, _returns=Iterable(String))
    def dizer_ola(ctx, name, times=1):
        for i in range(times):
            yield 'Olá, %s' % name

    @rpc(Agenda, _returns=Resposta)
    def receber_usuario(ctx, agenda):
        response = Resposta()
        if agenda and agenda.usuario:
          response.mensagem = 'Serviço executado com sucesso por %s'%(agenda.usuario.nome)
        response.sucesso = 1
        return response

from spyne.protocol.soap.soap11 import Soap11

app = Application([AppService], 'br.org.nenodias',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )
