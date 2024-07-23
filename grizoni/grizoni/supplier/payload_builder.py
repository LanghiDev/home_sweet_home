"""
module to payloads
"""
from uuid import uuid4


class PayloadBuilder:
    """ Complete with payloads necessary for the process """

    @staticmethod
    def properties(data_to_get_properties: dict) -> dict:
        return {
            'imovel[finalidade]': data_to_get_properties['purpose'],
            'imovel[codigoTipo][codigo][]': data_to_get_properties['property_type_id'],
            'imovel[codigoTipo][nome][]': data_to_get_properties['property_type'],
            'imovel[codigocidade]': data_to_get_properties['city'],
            'imovel[codigoregiao]': '0',
            'imovel[codigosbairros]': '0',
            'imovel[endereco]': '0',
            'imovel[numeroquartos]': data_to_get_properties['rooms'],
            'imovel[numerovagas]': '0-vaga-ou-mais',
            'imovel[numerobanhos]': '0-banheiro-ou-mais',
            'imovel[numerosuite]': '0-suite-ou-mais',
            'imovel[numerovaranda]': '0',
            'imovel[numeroelevador]': '0',
            'imovel[valorde]': '0',
            'imovel[valorate]': '0',
            'imovel[areade]': '0',
            'imovel[areaate]': '0',
            'imovel[extras]': '0',
            'imovel[extends]': 'false',
            'imovel[mobiliado]': 'false',
            'imovel[dce]': 'false',
            'imovel[piscina]': 'false',
            'imovel[sauna]': 'false',
            'imovel[salaofestas]': 'false',
            'imovel[academia]': 'false',
            'imovel[boxDespejo]': 'false',
            'imovel[portaria24h]': 'false',
            'imovel[aceitafinanciamento]': 'false',
            'imovel[arealazer]': 'false',
            'imovel[quartoqtdeexata]': 'false',
            'imovel[vagaqtdexata]': 'false',
            'imovel[destaque]': '0',
            'imovel[opcaoimovel]': '4',
            'imovel[retornomapa]': 'false',
            'imovel[retornomapaapp]': 'false',
            'imovel[numeropagina]': '1',
            'imovel[numeroregistros]': '20',
            'imovel[ordenacao]': 'valordesc',
            'imovel[pagina]': '1',
            'imovel[codigocondominio]': '0',
            'imovel[condominio][]': ['todos-os-condominios', 'valorminimo=0&valormaximo=0&pagina=1']
        }

    @staticmethod
    def phpsessid() -> dict:
        return {
            'PHPSESSID': '63f58f97e25f1630f67b58b5963d3087'
        }
