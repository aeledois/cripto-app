'''
Consulta Cripto
============

Versao 0.0.1
'''
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest

Builder.load_string("""
<Painel>:
    size_hint: .95, .95
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False
    TabbedPanelItem:
        text: 'Selecione'
        GridLayout: 
			id: glay
			rows: 4
			cols: 1
            padding: 10
			spacing: 5
            Image:
                source: 'cripto.png'
                size_hint: 0.3, 0.3
            Spinner:
				id: coin
				size_hint: 0.3, 0.3
				text: 'Bitcoin'
				values: 'Bitcoin','Cardano','Ethereum','xrp', 'dogecoin'
            Button:
			    id: consulta 
                size_hint: 0.3, 0.3
		        font_size: 36
                background_color: [0, 0, 1, 1]
                text: 'Consulte'
                on_release: root.button_press()
            RstDocument:
			    id: resultado 
		        font_size: 24
                text: '\\n'.join(("Moeda", "-----------","Selecione uma moeda para receber a cotação."))
    TabbedPanelItem:
        text: 'Digite'
        GridLayout:
            rows: 4
            cols: 1
            padding: 10
            spacing: 5
            Image:
                source: 'cripto.png'
                size_hint: 0.3, 0.3
            TextInput:
                size_hint: 1, 0.2
		        id: coint 
		        font_size: 36
		        multiline: False
            Button:
			    id: bconsultaT 
                size_hint: 0.3, 0.3
		        font_size: 36
                background_color: [0, 0, 1, 1]
                text: 'Consulte'
                on_release: root.buttont_press()
            RstDocument:
                id: resultadoT
	            font_size: 24
                text: '\\n'.join(("Cotacao", "-----------", "Digite a moeda."))
    TabbedPanelItem:
        text: 'Ajuda'
        GridLayout:
            rows: 3
            cols: 1
            padding: 10
            spacing: 5
            Image:
                source: 'cripto.png'
                size_hint: 0.3, 0.3
            Label:
                size_hint: 0.3, 0.3
                background_color: [0, 0, 1, 1]
                text: 'Al2 Software - 2021'
            RstDocument:
                font_size: 24
                text:
                    '\\n'.join(("=====","Ajuda", "=====", "-**Consulta a cotação da moeda:**","Escolha uma moeda para receber a cotação"))

""")

class Painel(TabbedPanel):
    urlT='https://api.coincap.io/v2/assets/{}'

    def __init__(self, **kwargs):
        super(Painel, self).__init__(**kwargs)

    def button_press(self):
        coin = self.ids.coin.text.lower()
        req = UrlRequest(self.urlT.format(coin), on_success=self.got_json, on_failure=self.got_erro, on_error=self.got_erro)

    def got_json(self, req, result):
        dicio = dict(result['data'])
        self.ids.resultado.text = "{}\n-----------\nUS$ {}".format(dicio['name'],dicio['priceUsd'])

    def buttont_press(self):
        coin = self.ids.coint.text.lower()
        req = UrlRequest(self.urlT.format(coin), on_success=self.got_jsonT, on_failure=self.got_erro, on_error=self.got_erro)

    def got_jsonT(self, req, result):
        dicio = dict(result['data'])
        self.ids.resultadoT.text = "{}\n-----------\nUS$ {}".format(dicio['name'],dicio['priceUsd'])

    def got_erro(self, *args):
        print("Failed to get api.", args)

class ConsultaCriptoApp(App):
    def build(self):
        return Painel()

if __name__ == '__main__':
    ConsultaCriptoApp().run()
