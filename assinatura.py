import glob, os, time
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
    [lista_de_hoteis.append(file.upper()) for file in glob.glob('*') if file.endswith(('.jpeg', '.png', '.jpg', '.tiff'))]
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


class dado_imagem:
    texto = str(None)
    fonteNome = str(None)
    cor = (int, int, int)
    coordenada = ()

    def __init__(self, texto, fonteNome, cor, coordenda):
        self.texto = texto
        self.fonteNome = fonteNome
        self.cor = cor
        self.coordenada = coordenda


class bandeira_hoteis:
    nome = str(None)
    func = str(None)
    funcING = str(None)
    nomeHotel = str(None)
    email = str(None)
    telefone = str(None)
    ender = str(None)
    cidade = str(None)
    dados = []
    tipo = None

    def iniciar(self, nome, func, funcING, nomeHotel, email, telefone, ender, cidade):
        self.nome = nome
        self.func = func
        self.funcING = funcING
        self.nomeHotel = nomeHotel
        self.ender = ender
        self.email = email
        self.telefone = telefone
        self.cidade = cidade

    def formatoFonte(self, nomeFonte, tamanhoFonte):
        self.nomeFonte = nomeFonte
        self.tamanhoFonte = tamanhoFonte
        return ImageFont.truetype(f'{self.nomeFonte}', tamanhoFonte)

    # Classe para hotéis bandeira Golden
    # Golden(nome, func, funcIng, nomeHotel, ender, email, telefone)
    def Golden(self, nome, func, funcING, nomeHotel, ender, cidade, email, telefone):
        # dados
        self.iniciar(nome, func, funcING, nomeHotel, email, telefone, ender, cidade)
        # formato RGB
        self.cor = (29, 54, 73)
        # formato geral do dado
        self.dados.append(dado_imagem(self.nome, self.formatoFonte("DalaFloda-Roman", 15), self.cor, (40, 20)))
        self.dados.append(dado_imagem(self.func, self.formatoFonte("Metric-Regular", 11), self.cor, (40, 34)))
        self.dados.append(dado_imagem(self.funcING, self.formatoFonte("Metric-Light", 10), self.cor, (40, 43)))
        self.dados.append(dado_imagem(self.nomeHotel, self.formatoFonte("Metric-Bold", 11), self.cor, (40, 60)))
        self.dados.append(dado_imagem(self.ender, self.formatoFonte("Metric-Regular", 11), self.cor, (40, 70)))
        self.dados.append(dado_imagem(self.cidade, self.formatoFonte("Metric-Regular", 11), self.cor, (40, 80)))
        self.dados.append(dado_imagem(self.email, self.formatoFonte("Metric-Regular", 11), self.cor, (40, 95)))
        self.dados.append(dado_imagem(self.telefone, self.formatoFonte("Metric-Bold", 10), self.cor, (40, 105)))

    # Classe para hotéis bandeira Royal
    def Royal(self, nome, func, email, telefone):
        # dados
        self.iniciar(nome, func, None, None, email, telefone, None, None)
        # formato RGB
        self.cor = (20, 50, 45)
        # formato geral do dado
        self.dados.append(dado_imagem(self.nome, self.formatoFonte("Poppins-Regular", 15), self.cor, (180, 15)))
        self.dados.append(dado_imagem(self.func, self.formatoFonte("Poppins-LightItalic", 13), self.cor, (180, 34)))
        self.dados.append(dado_imagem(self.email, self.formatoFonte("Poppins-ExtraLightItalic", 13), self.cor, (180, 65)))
        self.dados.append(dado_imagem(self.telefone, self.formatoFonte("Poppins-MediumItalic", 12), self.cor, (180, 82)))

    # Classe para hotéis bandeira TulipInn
    def TulipInn(self, nome, func, email, telefone):
        # dados
        self.iniciar(nome, func, None, None, email, telefone, None, None)
        # formato RGB
        self.cor = (0, 0, 0)
        # formato geral do dado
        self.dados.append(dado_imagem(self.nome, self.formatoFonte("overpass-bold", 14), self.cor, (180, 15)))
        self.dados.append(dado_imagem(self.func, self.formatoFonte("overpass-regular", 12), self.cor, (180, 34)))
        self.dados.append(dado_imagem(self.email, self.formatoFonte("overpass-regular", 12), self.cor, (180, 65)))
        self.dados.append(dado_imagem(self.telefone, self.formatoFonte("overpass-regular", 12), self.cor, (180, 82)))

    # Classe para hotéis bandeira SoftInn
    def SoftInn(self, nome, func, funcING, email, telefone, ender, cidade):
        # dados
        self.iniciar(nome, func, funcING, None, email, telefone, ender, cidade)
        # formato RGB
        self.cor = (255, 255, 255)
        # formato geral do dado
        self.dados.append(dado_imagem(self.nome, self.formatoFonte("CoText_Std", 16), self.cor, (34, 8)))
        self.dados.append(dado_imagem(self.func, self.formatoFonte("CoText_Std_Lt", 12), self.cor, (34, 27)))
        self.dados.append(dado_imagem(self.funcING, self.formatoFonte("CoText_Std_Lt", 10), self.cor, (34, 41)))
        self.dados.append(dado_imagem(self.email, self.formatoFonte("CoText_Std_Lt", 12), self.cor, (34, 59)))
        self.dados.append(dado_imagem(self.telefone, self.formatoFonte("CoText_Std_Lt", 12), self.cor, (34, 80)))
        self.dados.append(dado_imagem(self.ender, self.formatoFonte("CoText_Std_Lt", 12), self.cor, (34, 110)))
        self.dados.append(dado_imagem(self.cidade, self.formatoFonte("CoText_Std_Lt", 12), self.cor, (34, 121)))

    # função que imprime na imagem os dados desejados.
    def desenho(self, work):
        imagem = ImageDraw.Draw(work)
        for indice in range(0, len(self.dados)):
            imagem.text(self.dados[indice].coordenada, self.dados[indice].texto, self.dados[indice].cor,
                        self.dados[indice].fonteNome)
        self.dados.clear()


# Função p/ colher dados e distinguir qual fluxo o programa seguirá (bandeira do hotel)
def Criar_assinatura(work):
    nome = str(input('Nome: '))
    func = str(input('Função: '))
    email = str(input('Email: '))
    telefone = str('Fone: ' + input('Telefone: '))
    hotel = bandeira_hoteis()

    if 'GOLDEN' in bandeira:
        funcIng = str(input('Função em inglês: '))
        nomeHotel = str(input('Nome do hotel: '))
        ender = str(input('Endereço: '))
        cidade = str(input('Cidade: '))
        try:
            # Instancia classe do hote
            hotel.Golden(nome, func, funcIng, nomeHotel, ender, cidade, email, telefone)
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
        return personalizado()

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
    while True:
        try:
            # Muda a aplicação para o diretório passado e inicia as funções de edição
            os.chdir(input('Pasta da imagem(ex: C:\PJA\Origem): '))
            #os.chdir(os.getcwd())
            Imagem()

        # Caso seja passado qualquer dado que não seja uma pasta, a aplicação reiniciará
        except FileNotFoundError:
            print('Pasta inserida não encontrada, insira um caminho existente')
            main()
        except WindowsError:
            print('Pasta inserida não encontrada, insira um caminho existente')
            main()


# Instancia programa principal
main()
