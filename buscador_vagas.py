import requests
from bs4 import BeautifulSoup
import pandas as pd # Importamos o pandas com o apelido 'pd'

url = "https://realpython.github.io/fake-jobs/"
resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, "html.parser")

vagas = soup.find_all("div", class_="card-content")

# criar uma lista de vagas vazia
lista_vagas = []

for vaga in vagas:
    # Capturamos os elementos primeiro
    titulo_elemento = vaga.find("h2", class_="title is-5")
    empresa_elemento = vaga.find("h3", class_="subtitle is-6 company")
    local_elemento = vaga.find("p", class_="location")
    
    # AGORA O PULO DO GATO: Extrair apenas o texto (.text) e limpar (.strip())
    # Se não fizermos isso, ele salva o HTML com <h2> etc.
    titulo = titulo_elemento.text.strip() if titulo_elemento else "N/A"
    empresa = empresa_elemento.text.strip() if empresa_elemento else "N/A"
    local = local_elemento.text.strip() if local_elemento else "N/A"
    
    # 4 Extrair o link da vaga
    links = vaga.find_all("a", class_="card-footer-item")
    link_vaga = links[1]["href"]

    # Didionario de dados
    dados_vaga = {
        "Cargo": titulo,
        "Empresa": empresa,
        "Local": local,
        "Link": link_vaga
    }

    # Adicionamos a "ficha" da vaga na nossa lista
    lista_vagas.append(dados_vaga)

# Fora do loop, salvamos o arquivo
df = pd.DataFrame(lista_vagas) # Transforma a lista em tabela
df.to_csv("vagas_extraidas.csv", index=False, sep=';', encoding="utf-8-sig")

print("Sucesso! O arquivo 'vagas_extraidas.csv' foi criado na sua pasta.")