class Routes:
    def __init__(self):
        self._grizoni_url = 'https://www.imobiliariagrizoni.com.br'

    @property
    def grizoni_url(self):
        return self._grizoni_url

    @property
    def get_properties(self):
        return f'{self._grizoni_url}/imoveis/ajax/'
