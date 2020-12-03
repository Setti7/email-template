import sys
from itertools import zip_longest

from jinja2 import FileSystemLoader, Environment


def get_date_from_sheets() -> dict:
    """
    Aqui você faria alguma lógica pra pegar os dados de uma linha específica de uma
    planilha do sheets ou algo parecido.
    """

    data = {
        "name": "Savenagno-alguma coisa",
        "background_color": "#fff",
        "base_href": "https://www.savegnago.com.br/",
        "items": [
            {
                "name": "Costela bovina ripa kg",
                "description": "R$ 29.90",
                "img_src": "http://imagens.savegnagoonline.com.br/Logo_savegnago.png",
            },
            {
                "name": "Fraldinha Friboi peça inteira a vácuo kg bovina ripa kg",
                "description": "No Save Ganhe pague - R$ 29.90",
                "img_src": "http://imagens.savegnagoonline.com.br/1_QB_03.dez.png",
                "img_href": "https://www.savegnago.com.br/fraldinha-bovina-1500kg-peca-vacuo/p?idsku=19392",
            },
            {
                "name": "Patinho kg",
                "description": "Pagando com nosso cartão - R$ 29.90",
                "img_src": "http://imagens.savegnagoonline.com.br/1_QB_03.dez.png",
            },
        ],
    }

    # A lista de items precisa ser, na verdade, uma lista de dupla de items
    data['items'] = grouper(data['items'], 2)

    return data


def apply_template(data: dict, template_filename: str) -> str:
    """
    Em https://palletsprojects.com/p/jinja/ tem instruções de como usar o sistema de templates do Jinja2.
    Você pode usar hierarquia de templates se quiser.
    """

    # Carregando os templates Jinja2
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template(template_filename)

    # Renderizando o documento final
    return template.render(**data)


# https://stackoverflow.com/a/16789869
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def main():

    # Você pode passar o nome do template como argumento pela linha de comando
    # (se não, usa template.mjml por padrão)
    template_filename: str
    if sys.argv[1] is None:
        template_filename = "template.mjml"
    else:
        template_filename= sys.argv[1]

    data = get_date_from_sheets()
    generated_email = apply_template(data, template_filename)

    print(f"Aqui está o email gerado:\n\n{generated_email}")

if __name__ == '__main__':
    main()
