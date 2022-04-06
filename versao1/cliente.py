import urllib.request, json, time

URL_SERVICO = "http://localhost:1024/"
IS_ALIVE = URL_SERVICO + "isalive/"
INFO = URL_SERVICO + "info/"
JOGATINA = URL_SERVICO + "jogatina/"
SISTEMAS = URL_SERVICO + "sistemas/"

def acessar_url(url):
    resposta = urllib.request.urlopen(url)
    dado = resposta.read()

    return dado.decode("utf-8")

def is_alive():
    alive = False

    if acessar_url(IS_ALIVE) == "yes":
        alive = True

    return alive

def get_info():
    pass

def get_jogatina():
    noticias = acessar_url(JOGATINA)
    return json.loads(noticias)

    # return noticias

def get_sistemas():
    noticias = acessar_url(SISTEMAS)
    return json.loads(noticias)

def imprimir(tipo_noticias, noticias):
    print(f"****** Últimas notícias sobre {tipo_noticias} *******")
    for noticia in noticias:
        print(f"data: {noticia['data']}. Notícia: {noticia['titulo']}")

if __name__ == "__main__":
    while True:
        # 1, verificar se o servico esta ativo
        if is_alive():
        # 2, se o servico estiver ativo...

            # 3, acessar as noticias sobre os jogos
            noticias = get_jogatina()
            imprimir("jogos eletrônicos", noticias)
            # 4, acessar as noticias sobre os sistemas
            noticias = get_sistemas()
            imprimir("sistemas operacionais", noticias)
        # 5, do contrario...
        else:
            # 6, avisar que o servico esta indisponivel
            print("Serviço de notícias está indisponível")
        time.sleep(5)
