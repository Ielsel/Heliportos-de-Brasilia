# -*- coding: utf-8 -*-
"""
**Tema:** Heliportos de Brasília

# Construção do DataFrame
"""

# Criando DataFrame com localização e nome dos 16 heliportos de Brasília

# Importando a biblioteca pandas
import pandas as pd

# Criando lista "heliporto" com o nome dos heliportos de Brasília
heliporto = ['Heliponto - Hospital Regional de Brazlândia',
             'Heliponto - Hospital Anchieta - SJDF',
             'Heliponto HRG',
             'Heliponto - Parkway - SJWY',
             'Heliponto Parque Cidade',
             'Heliporto da Granja do Torto',
             'Heliponto - HFA',
             'Heliponto - PCDF - SWSW',
             'Heliponto - Águas Claras',
             'Heliponto - Autódromo Internacional de Brasília',
             'Heliponto - Brasil XXI',
             'Heliponto Santa Monica',
             'Heliponto São Sebastião',
             'Heliponto Palacio da Alvorada']

# Criando lista "localizacao" com as respectivas localizações dos heliportos de Brasília
localizacao = ['Brazlândia, Brasília - DF',
               'St. C Norte QNC AE - Taguatinga, Brasília - DF',
               'St. Central EQ 47/49 - Gama, Brasília - DF',
               'Park Way Q 26 Conj. 1 - Núcleo Bandeirante, Brasília - DF',
               'SCS Q. 6 BL A - Asa Sul, Brasília - DF',
               'Lago Norte, Brasília - DF',
               'St. Sudoeste - Cruzeiro / Sudoeste / Octogonal, Brasília - DF',
               'SGO - Brasília',
               'Águas Claras, Brasília - DF',
               'SRPN Trecho 1 - Brasília - DF',
               '752, Q. St. Hoteleiro - Águas Claras, Brasília - DF',
               'St. Comercial Condomínio Residência Santa Monica - Santa Maria, Brasília - DF',
               'Saída da Papuda - São Sebastião, Brasília - DF',
               'Unnamed Road, Zona Cívico-Administrativa Palacio da Alvorada, Brasília - DF']

# Criando lista "CEP" com as respectivas CEP's dos heliportos de Brasília
cep = ['73.740-793',
       '72.115-700',
       '72.405-610',
       '71.745-601',
       '70.740-610',
       '71.551-400',
       '70.655-775',
       '70.655-775',
       '70.297-400',
       '70.655-775',
       '72.405-600',
       '72.596-825',
       '70.297-400',
       '70.150-903']

# Criando lista "Categoria" com as respectivas categoria dos heliportos de Brasília
categoria = ['Privado',
             'Privado',
             'Privado',
             'Privado',
             'Privado',
             'Privado',
             'Público',
             'Privado',
             'Privado',
             'Privado',
             'Privado',
             'Privado',
             'Privado',
             'Público']

# Criando lista "horario_pico" com os respectivos horários de pico dos heliportos de Brasília
horario_pico = ['04:00',
                '18:00',
                '18:00',
                '11:00',
                '07:00',
                '22:00',
                '15:00',
                '12:00',
                '02:00',
                '21:00',
                '10:00',
                '11:00',
                '20:00',
                '17:00']

# Implementando as listas em um dicionário chamado "dados_heli"
dados_heli = {
    'Heliporto': heliporto,
    'Localização': localizacao,
    'CEP': cep,
    'Categoria': categoria,
    'Horário de pico': horario_pico
}

# Transformando o dicionário "dados_heli" em um DataFrame chamado "df_heliportos"
df_heliportos = pd.DataFrame(data = dados_heli)

"""# Apresente em tela (output) toda a base de dados."""

# Método display para a apresentação dos gerais do DataFrame
print("A seguir, a presentação do DataFrame:\n")
display(df_heliportos)

"""# Apresente o tamanho do seu dataframe (quantas colunas x linhas)."""

# Printando na tela utilizando a formatação para apresentar as linhas e colunas entre uma String
print(f"Apresentando a proporção do DataFrame usando método 'shape':\nO DataFrame tem {df_heliportos.shape[0]} linhas e {df_heliportos.shape[1]} colunas.")

"""# Acesse a linha (x) e apresente em tela todas as características do item."""

print("Acessando e apresentando em tala todas as informações da linha (x):\n")

# "indecs" vai salvar um valor digitado pelo usuário referente à linha de informação desejada
indecs = int(input('Digite o número da linha que deseja ler as informações (0 a 15): '))

# Se o valor digitado for maior que as instâncias do DataFrame ou menor que 0
if indecs < 0 or indecs > len(df_heliportos):

  # Indica erro por estar fora do intervalo
  print("\nO índice está fora do intervalo!")

# Se não
else:

  print(f"\nAcessando informações da linha {indecs}...\n")

  # Extraindo as informações da linha desejada e alocando na variável "linha_desejada"
  linha_desejada = df_heliportos.iloc[indecs]

  # Para cada coluna, imprime o nome da coluna e o valor correspondente da linha selecionada
  # Isto permite exibir todas as informações da linha de forma organizada e legível
  for coluna, valor in linha_desejada.items():

    # Apresentando os valores da instância do DataFrame
    print(f"{coluna}: {valor}")

# Indicando o fim da pesquisa
print("\nEncerrando pesquisa...")

"""# Verifique se o dataframe está vazio."""

# Se o DataFrame não estiver vazio...
if (df_heliportos.empty) == False:
    print('Não está vazia') # ...informa ao usuário que não está vazio
# Se não...
else:
  print('Está vazia') # ...informa ao usuário que está vazio

"""# Apresente em tela os 5 primeiros registros da base de dados."""

print("Apresentando os 5 primeiras linhas do DataFrame usando método 'head':\n")
# Usando o método head para apresentar um cabeçalho das cinco primeiras linhas de dado
display(df_heliportos.head(5))

"""# Exclua um item (linha) de sua base de dados."""

# Deletando a quinta linha do DataFrame
df_heliportos=df_heliportos.drop(4)

print("Linha 4 deletada usando o método 'drop():'\n")
# Apresentando o DataFrame sem a linha de index 4
display(df_heliportos)

"""# Adicione um item (linha) na sua base de dados."""

# Adicionando novos dados no index 4 do DataFrame
df_heliportos.loc[4] = ['Heliponto Parque Cidade', 'SCS Q. 6 BL A - Asa Sul, Brasília - DF', '70.740-610', 'Privado', '07:00']
print("DataFrame com as informações da linha 4 deletada adicionada novamente:\n")

# Apresentando na tela o DataFrame atualizado
display(df_heliportos)

"""# Transponha a coluna para a linha em sua base de dados."""

print("DataFrame com transposição usando o método 'transpose()':\n")
# Apresentando o DataFrame transposto
display(df_heliportos.transpose())

"""# Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados."""

print("Apresentando apenas até a 2º coluna do DataFrame usando o código 'iloc' e definindo o limite de colunas:\n")
# Usando método iloc para definir o limite de amostragem das colunas, definida como 2
display(df_heliportos.iloc[: ,:2])

"""# **Informe como foi desenvolvido o Projeto.**


Utilizando a linguagem de programação python, importei a biblioteca pandas e iniciei o dicionário 'dados_heli'. Adicionei informações existentes nas listas: heliporto, localizacao, CEP, categoria e horário de pico com informações referentes ao nome e localização dos heliportos. Após isso, criei um DataFrame a partir dos dados do dicionário;

**Questão 1:**

*   Utilizei o "display(df_heliportos)" para mostrar toda a tabela da base de dados de forma mais atrativa ao usuário.


**Questão 2:**
*   utilizei "df_heliportos.shape", função que mostra as proporções do DataFrame, printei na tela usando a formatação no código "print()" para uma melhor visualização para o usuário.


**Questão 3:**

*   Criei uma variável(indecs) que vai receber o valor convertido para inteiro de uma input onde o usuário vai digitar um determinado valor;
*   Usei as estruturas de decisão(if e else) para verificar se o valor inteiro digitado pelo usuário é menor que 0 ou se é maior que a quantidade de instâncias do DataFrame, o que indica um valor inválido;
*   Caso o valor digitado seja válido, o programa irá pegar os dados da linha desejada e vai alocar na variável "linha_desejada";
*   Após isso, fiz o uso do código for para imprimir as colunas(Heliporto, Localização e Categoria) na variável "Coluna" e os valores de cada coluna na variável "valores" para uma melhor visualização do usuário;
*   Por fim, pritei na tela as colunas e os valores de forma organizada.


**Questão 4:**
*   Fiz o uso dos comandos de decisão(if e else) para checar se o DataFrame está vazio ou não, a depender do resultado, o código pode apresentar pro usuário diferentes resultados da checagem. Nesse caso, como o DataFrame está populado de dados, vai apresentar que a tabela não está vazia;


**Questão 5:**

*   "df_heliportos.head(5)" código responsável por apresentar apenas as informações das 5 primeiras instâncias do DataFrame(indo da linha 0 até 4);


**Questão 6:**

*   "df_heliportos.drop(4)" para excluir a instância de index = 4 do DataFrame;


**Questão 7:**
*   "df_heliportosf.loc[4] = [informações a serem inseridas]" para adicionar os dados a serem inseridos no DataFrame especificamente no index 4, o mesmo que foi excluído na questão de número 6. Usei os mesmos dados da instância excluída;


**Questão 8:**
*   A função "df_heliportos.transpose()" já faz todo o trabalho de transposição das linhas e colunas, realizando a sua reorganização posicionando as colunas no lugar das linhas e as linhas no lugar das colunas;


**Questão 9:**
*   "df_heliportos.iloc[:, :2]" método iloc para selecionar o limite de amostragem das linhas e colunas do DataFrame. No caso atual, está configurado para mostrar todas as linhas e as duas primeiras colunas do DataFrame original.

**Bibliografia:**

São Bernardo do Campo. Hospital Anchieta: da construção aos tempos atuais. Disponível em: https://www.saobernardo.sp.gov.br/web/cultura/hospital-anchieta-da-construcao-aos-tempos-atuais#:~
=Nas%20imagens%2C%20vemos%20o%20hospital,ele%20em%20setembro%20de%201997. Acesso em: 27 maio 2024.

Agência Brasília. Hospital Regional do Gama terá novo reservatório de água e heliponto. Disponível em: https://agenciabrasilia.df.gov.br/2019/10/23/hospital-regional-do-gama-tera-novo-reservatorio-de-agua-e-heliponto/ Acesso em: 27 maio 2024.

Novacap. Hospital Regional de Brazlândia será reconstruído com R$ 208 milhões. Disponível em: https://www.novacap.df.gov.br/hospital-regional-de-brazlandia-sera-reconstruido-com-r-208-milhoes/#:~
=Datado%20da%20d%C3%A9cada%20de%201970,sexta%2Dfeira%20(1%C2%BA). Acesso em: 27 maio 2024.

Ache CEP. Lago Norte. Disponível em: https://www.achecep.com.br/Distrito-Federal/Brasilia/Lago-Norte/ Acesso em: 27 maio 2024.

Transparência C.C. SMPW, Quadra 26, Conjunto 1, Park Way - Brasília/DF. Disponível em: https://transparencia.cc/dados/cep/71745601-quadra-smpw-quadra-26-conjunto-1-bairro-park-way-brasilia-df/ Acesso em: 27 maio 2024.

Agência Nacional de Aviação Civil (ANAC). Aeródromos e Helipontos Públicos. Disponível em: https://www.anac.gov.br/acesso-a-informacao/dados-abertos/areas-de-atuacao/aerodromos/lista-de-aerodromos-publicos-v2. Acesso em: 27 maio 2024.

Agência Nacional de Aviação Civil (ANAC). Aeródromos e Helipontos Privados. Disponível em: https://www.anac.gov.br/acesso-a-informacao/dados-abertos/areas-de-atuacao/aerodromos/lista-de-aerodromos-privados-v2. Acesso em: 27 maio 2024.

Departamento de Controle do Espaço Aéreo (DECEA). Publicação de Informações Aeronáuticas (AIP) Brasil. Disponível em: [https://aisweb.decea.mil.br/?i=publicacoes&p=aip](https://aisweb.decea

"""