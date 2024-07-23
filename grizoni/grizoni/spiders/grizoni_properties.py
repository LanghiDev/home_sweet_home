from typing import Iterable

import scrapy
from scrapy import FormRequest, Request
from scrapy.http import HtmlResponse

from grizoni.grizoni.supplier import headers
from grizoni.grizoni.supplier.payload_builder import PayloadBuilder
from grizoni.grizoni.supplier.routes import Routes


class GrizoniPropertiesSpider(scrapy.Spider):
    name = "grizoni_properties"

    def __init__(self):
        super(GrizoniPropertiesSpider, self).__init__()
        self.supplier_routes = Routes()
        self.payload_builder = PayloadBuilder()

    def start_requests(self) -> Iterable[Request]:
        yield Request(
            url=self.supplier_routes.grizoni_url,
            callback=self.parse_grizoni
        )

    def parse_grizoni(self, _):
        get_properties_payload = self.payload_builder.properties(data_to_get_properties={
            'purpose': 'venda',
            'property_type_id': '1',
            'property_type': 'casa',
            'city': 'bauru',
            'rooms': '2-quartos'
        })

        yield FormRequest(
            url=self.supplier_routes.get_properties,
            formdata=get_properties_payload,
            headers=headers.default_headers(),
            cookies=self.payload_builder.phpsessid(),
            callback=self.get_properties
        )

    def get_properties(self, response: HtmlResponse):
        try:
            properties_json: dict = response.json()
            quantity: int = int(properties_json['quantidade'])
            properties: list = properties_json['lista']

            self.logger.info(f"{quantity} properties has found!")

            for immobile in properties:
                self.logger.info(f"{immobile['titulo']}\n"
                                 f"Purpose: {immobile['finalidade']}\n"
                                 f"Type: {immobile['tipo']}\n"
                                 f"Price: {immobile['valor']}  |   "
                                 f"{immobile['valorminimo']} - {immobile['valormaximo']}\n"
                                 f"Neighborhood: {immobile['bairro']}\n"
                                 f"Address: {immobile['endereco']}\n"
                                 f"{immobile['cep']}")

        except Exception:
            self.logger.exception("Error to get properties.")
