from typing import Union


from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, retorna_estatistica: Classes) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)

    # def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
    #     estatistica: Dict[str, Union[List[str], str, int]] = {}
    #     if flag != 'detail':
    #         estatistica[f'{agencia}-{dia}'] = len(self.clientes_atendidos)
    #     else:
    #         estatistica['dia'] = dia
    #         estatistica['agencia'] = agencia
    #         estatistica['clientes_atendidos'] = self.clientes_atendidos
    #         estatistica['quantidade_clientes_atendidos'] = (
    #             len(self.clientes_atendidos)
    #         )
    #
    #     return estatistica
