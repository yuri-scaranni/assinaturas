import glob, os, sys, time
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

###################################################################
# Um projeto desenvolvido por Yuri Scaranni - Louvre Hotels Group #
###################################################################

# Gerador de nome da imagem baseado no dia/hora
def Hora():
    return str(datetime.now()).replace(':', '_').replace(' ', '-H-')[:-7]

# Variável global para distinguir bandeira
bandeira = ""

# função para buscar imagens na pasta passada, retorna o caminho completo da imagem escolhida
def LocalizarImagens():
    lista_de_hoteis = ['Sair', 'Pesquisar novamente']
    # Insere na lista arquivos de formato "jpg", "jpeg" e "png"
    [lista_de_hoteis.append(file.upper()) for file in glob.glob('*') if file.endswith(('.jpeg', '.png', '.jpg'))]
    [print(f'[{index}] - {opcao}') for index, opcao in enumerate(lista_de_hoteis)]

    # Testa a opção, caso seja inválida retorna opções anteriores
    try:
        op = int(input('Opção: '))
        if op == 0:
            exit()
        if op == 1:
            return main()
    except ValueError:
        print('\nInsira apenas números que apareçam na lista.\n')
        return LocalizarImagens()

    global bandeira
    bandeira = lista_de_hoteis[op]
    return os.getcwd() + '\\' + lista_de_hoteis[op]


class bandeira_hoteis:
    # Classe para hotéis bandeira Golden
    def Golden(self, nome, func, funcIng, nomeHotel, ender, email, telefone):
        # dados
        self.nome = nome
        self.func = func
        self.funcing = funcIng
        self.nomehotel = nomeHotel
        self.ender = ender
        self.email = email
        self.tele = telefone
        self.dados = [self.nome, self.func, self.funcing, self.nomehotel, self.ender, self.email, self.tele]

        # formato geral do dado
        self.FonteNome = ImageFont.truetype("DalaFloda-Roman", 18)  # 25
        self.FonteFuncao = ImageFont.truetype("Metric-Regular", 12)  # 16
        self.FonteFuncaoIngles = ImageFont.truetype("Metric-Light", 12)
        self.FonteNomedoHotel = ImageFont.truetype("Metric-Bold", 12)
        self.FonteEndereco = ImageFont.truetype("Metric-Regular", 12)
        self.FonteEmail = ImageFont.truetype("Metric-Regular", 12)
        self.FonteTelefone = ImageFont.truetype("Metric-Bold", 12)
        self.fontes = [self.FonteNome, self.FonteFuncao, self.FonteFuncaoIngles, self.FonteNomedoHotel,
                       self.FonteEndereco, self.FonteEmail, self.FonteTelefone]

        # formato RGB
        self.cor = (29, 54, 73)
        # Tupla de coordenada X, Y de cada um dos atributos da classe
        self.coordenada = [(25, 9), (25, 26), (25, 37), (25, 52), (25, 65), (25, 79), (25, 100)]

    # Classe para hotéis bandeira Royal
    def Royal(self, nome, func, email, telefone):
        # dados
        self.nome = nome
        self.func = func
        self.email = email
        self.tele = telefone
        self.dados = [self.nome, self.func, self.email, self.tele]

        # formato geral do dado
        self.FonteNome = ImageFont.truetype("Poppins-Regular", 15)
        self.FonteFunc = ImageFont.truetype("Poppins-LightItalic", 13)
        self.FonteEmail = ImageFont.truetype("Poppins-ExtraLightItalic", 13)
        self.FonteTele = ImageFont.truetype("Poppins-MediumItalic", 12)
        self.fontes = [self.FonteNome, self.FonteFunc, self.FonteEmail, self.FonteTele]

        # formato RGB
        self.cor = (20, 50, 45)
        # Tupla de coordenada X, Y de cada um dos atributos da classe
        self.coordenada = [(180, 15), (180, 34), (180, 65), (180, 82)]

    # Classe para hotéis bandeira TulipInn
    def TulipInn(self, nome, func, email, telefone):
        # dados
        self.nome = nome
        self.func = func
        self.email = email
        self.tele = telefone
        self.dados = [self.nome, self.func, self.email, self.tele]

        # formato geral do dado
        self.FonteNome = ImageFont.truetype("overpass-bold", 14)
        self.FonteFunc = ImageFont.truetype("overpass-regular", 12)
        self.FonteEmail = ImageFont.truetype("overpass-regular", 12)
        self.FonteTele = ImageFont.truetype("overpass-regular", 12)
        self.fontes = [self.FonteNome, self.FonteFunc, self.FonteEmail, self.FonteTele]

        # formato RGB
        self.cor = (0, 0, 0)
        # Tupla de coordenada X, Y de cada um dos atributos da classe
        self.coordenada = [(180, 15), (180, 34), (180, 65), (180, 82)]

    # Classe para hotéis bandeira SoftInn
    def SoftInn(self, nome, func, funcIng, email, telefone, ender, cidade):
        # dados
        self.nome = nome
        self.func = func
        self.funcing = funcIng
        self.email = email
        self.tele = telefone
        self.ender = ender
        self.cidade = cidade
        self.dados = [self.nome, self.func, self.funcing, self.email, self.tele, self.ender, self.cidade]

        # formato geral do dado
        self.FonteNome = ImageFont.truetype("CoText_Std", 16)
        self.FonteFuncao = ImageFont.truetype("CoText_Std_Lt", 12)
        self.FonteFuncaoIngles = ImageFont.truetype("CoText_Std_Lt", 10)
        self.FonteEmail = ImageFont.truetype("CoText_Std_Lt", 12)
        self.FonteTelefone = ImageFont.truetype("CoText_Std_Lt", 12)
        self.FonteRua = ImageFont.truetype("CoText_Std_Lt", 12)
        self.FonteCidade = ImageFont.truetype("CoText_Std_Lt", 12)
        self.fontes = [self.FonteNome, self.FonteFuncao, self.FonteFuncaoIngles, self.FonteEmail,
                       self.FonteTelefone, self.FonteRua, self.FonteCidade]

        # formato RGB
        self.cor = (255, 255, 255)
        # Tupla de coordenada X, Y de cada um dos atributos da classe
        self.coordenada = [(34, 8), (34, 27), (34, 41), (34, 59), (34, 80), (34, 110), (34, 121)]

    # função que imprime na imagem os dados desejados.
    def desenho(self, work):
        imagem = ImageDraw.Draw(work)
        for indice in range(0, len(self.fontes)):
            imagem.text(self.coordenada[indice], self.dados[indice], self.cor, self.fontes[indice])


# Função p/ colher dados e distinguir qual fluxo o programa seguirá (bandeira do hotel)
def Criar_assinatura(work):
    nome = str(input('Nome: '))
    func = str(input('Função: '))
    email = str(input('Email: '))
    telefone = str('Fone: ' + input('Telefone: '))
    hotel = bandeira_hoteis()

    # Bandeira Golden, seus dados
    if 'GOLDEN' in bandeira:
        funcIng = str(input('Função em inglês: '))
        nomeHotel = str(input('Nome do hotel: '))
        ender = str(input('Endereço: '))

        try:
            # Instancia classe do hotel
            hotel.Golden(nome, func, funcIng, nomeHotel, ender, email, telefone)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    # Bandeira royal, seus dados
    elif 'ROYAL' in bandeira:
        try:
            # Instancia classe do hotel
            hotel.Royal(nome, func, email, telefone)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    # Bandeira TulipInn, seus dados
    elif 'TULIP_INN' in bandeira:
        try:
            # Instancia classe do hotel
            hotel.TulipInn(nome, func, email, telefone)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    # Bandeira SoftInn, seus dados
    elif 'SOFT_INN' in bandeira:
        funcIng = str(input('Função em inglês: '))
        ender = str(input('Endereço(rua): '))
        cidade = str(input('Cidade(nº, cidade, estado): '))

        try:
            # Instancia classe do hotel
            hotel.SoftInn(nome, func, funcIng, email, telefone, ender, cidade)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    # Instanciando o método desenho da classe 'bandeira_hoteis'
    hotel.desenho(work)


# Cria o dado, cor, fonte, posição e texto de forma personalizada para ser impresso em alguma assinatura
def personalizado(work):
    try:
        print('Coordenadas:')
        coordenada = (int(input('X: ')), int(input('Y: ')))
        print('Cor:')
        cor = (int(input('R: ')), int(input('G: ')), int(input('B: ')))
        tamanho = int(input('Tamanho da fonte: '))
        mensagem = str(input('Texto: '))
        fonte = str(input('Fonte: '))
        letra = ImageFont.truetype(fonte, tamanho)
    except ValueError:
        print('Valor incorreto, insira somente valores inteiros')
        quit()
    except OSError:
        print('Fonte não encontrada, digite uma fonte válida')
        quit()

    dado_personalizado = ImageDraw.Draw(work)
    dado_personalizado.text((coordenada), mensagem, (cor), letra)


# Função que constrói a imagem
def Imagem():
    # Abre imagem e instancia a mesma
    try:
        work = Image.open(LocalizarImagens())
        # Loop p/ decidir tipo de edição.
        while True:
            op_edicao = (input('[1] - Criar nova assinatura\n[2] - Personalizar\n[3] - Voltar\n:: '))
            if op_edicao == '1':
                Criar_assinatura(work)
                break
            elif op_edicao == '2':
                personalizado(work)
                break
            elif op_edicao == '3':
                return Imagem()

        # Cria variavel que armazena nome da imagem
        nome_imagem_criada = str(input('\nnome para salvar: ')) + '_'

        # Cria pasta destino caso não exista, pasta criada dentro do diretório onde se encontra
        # a imagem
        if os.path.isdir(os.getcwd() + '\\Destino') == False:
            os.mkdir(os.getcwd() + '\\Destino')
            print('\nFoi criada uma pasta de destino: {}'.format(os.getcwd() + '\\Destino'))
        # Salva imagem em formato PNG, na pasta destino.
        work.save(os.getcwd() + '\\Destino\\' + nome_imagem_criada + Hora() + '.png')

        # Mostra o caminho da imagem e seu nome
        print('Imagem salva em:', os.getcwd() + '\\Destino\\' + nome_imagem_criada + Hora() + '.png')

        saida = input('Para sair digite "sair", caso contrário, pressione qualquer tecla: ')
        if saida.lower() == 'sair':
            exit()
        else:
            time.sleep(1)
            main()

    except IndexError:
        print('\nOpção não presente na lista, tente novamente.\n')
        LocalizarImagens()


# Programa principal
def main():
    # Insere diretório da imagem em branco
    try:
        while True:
            # Muda a aplicação para o diretório passado e inicia as funções de edição
            os.chdir(input('Pasta da imagem(ex: C:\PJA\Origem): '))
            Imagem()

    # Caso seja passado qualquer dado que não seja uma pasta, a aplicação reiniciará
    except FileNotFoundError:
        print('Pasta inserida não encontrada, insira um caminho existente')
        main()


# Instancia programa principal
main()