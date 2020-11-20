import os
from PIL import Image, ImageDraw, ImageFont
import time


def localizarImagens():
    lista_de_hoteis = ['SAIR', 'PESQUISAR NOVAMENTE']

    for _, _, templates in os.walk('templates'):
        for temp in templates:
            lista_de_hoteis.append(temp.upper())
    [print(f'[{index}] - {opcao}') for index, opcao in enumerate(lista_de_hoteis)]

    try:
        op = int(input('Opção: '))
        if op == 0:
            print()
            print('*********** BYE! ***********')
            time.sleep(2)
            exit()
        elif op == 1:
            print()
            print('*********** REFRESH ***********')
            print()
            return localizarImagens()
        else:
            return lista_de_hoteis[op], os.path.join(os.path.abspath('templates'), lista_de_hoteis[op])
    except ValueError:
        print('\n*********** Insira apenas números ***********\n')
        return localizarImagens()
    except IndexError:
        print('\n*********** Insira apenas números que apareçam na lista ***********\n')
        return localizarImagens()


class DadoImagem:
    texto = str(None)
    fonteNome = str(None)
    cor = (int, int, int)
    coordenada = ()

    def __init__(self, texto, fonteNome, cor, coordenda):
        self.texto = texto
        self.fonteNome = fonteNome
        self.cor = cor
        self.coordenada = coordenda


class BandeiraHoteis:
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

    def formato_fonte(self, nomeFonte, tamanhoFonte):
        self.nomeFonte = nomeFonte
        self.tamanhoFonte = tamanhoFonte
        return ImageFont.truetype(f'{self.nomeFonte}', tamanhoFonte)

    def golden(self, nome, func, funcING, nomeHotel, ender, cidade, email, telefone):
        self.iniciar(nome, func, funcING, nomeHotel, email, telefone, ender, cidade)
        self.cor = (29, 54, 73)
        self.dados.append(DadoImagem(self.nome, self.formato_fonte("DalaFloda-Roman", 16), self.cor, (40, 20)))
        self.dados.append(DadoImagem(self.func, self.formato_fonte("Metric-Regular", 12), self.cor, (40, 34)))
        self.dados.append(DadoImagem(self.funcING, self.formato_fonte("Metric-Light", 11), self.cor, (40, 43)))
        self.dados.append(DadoImagem(self.nomeHotel, self.formato_fonte("Metric-Bold", 11), self.cor, (40, 60)))
        self.dados.append(DadoImagem(self.ender, self.formato_fonte("Metric-Regular", 11), self.cor, (40, 70)))
        self.dados.append(DadoImagem(self.cidade, self.formato_fonte("Metric-Regular", 11), self.cor, (40, 80)))
        self.dados.append(DadoImagem(self.email, self.formato_fonte("Metric-Regular", 11), self.cor, (40, 95)))
        self.dados.append(DadoImagem(self.telefone, self.formato_fonte("Metric-Bold", 10), self.cor, (40, 105)))

    def royal(self, nome, func, email, telefone):
        self.iniciar(nome, func, None, None, email, telefone, None, None)
        self.cor = (20, 50, 45)
        self.dados.append(DadoImagem(self.nome, self.formato_fonte("Poppins-Regular", 15), self.cor, (180, 15)))
        self.dados.append(DadoImagem(self.func, self.formato_fonte("Poppins-LightItalic", 13), self.cor, (180, 34)))
        self.dados.append(DadoImagem(self.email, self.formato_fonte("Poppins-ExtraLightItalic", 13), self.cor, (180, 65)))
        self.dados.append(DadoImagem(self.telefone, self.formato_fonte("Poppins-MediumItalic", 12), self.cor, (180, 82)))

    def tulipinn(self, nome, func, email, telefone):
        self.iniciar(nome, func, None, None, email, telefone, None, None)
        self.cor = (0, 0, 0)
        self.dados.append(DadoImagem(self.nome, self.formato_fonte("overpass-bold", 14), self.cor, (180, 15)))
        self.dados.append(DadoImagem(self.func, self.formato_fonte("overpass-regular", 12), self.cor, (180, 34)))
        self.dados.append(DadoImagem(self.email, self.formato_fonte("overpass-regular", 12), self.cor, (180, 65)))
        self.dados.append(DadoImagem(self.telefone, self.formato_fonte("overpass-regular", 12), self.cor, (180, 82)))

    def softinn(self, nome, func, funcING, email, telefone, ender, cidade):
        self.iniciar(nome, func, funcING, None, email, telefone, ender, cidade)
        self.cor = (255, 255, 255)
        self.dados.append(DadoImagem(self.nome, self.formato_fonte("CoText_Std", 16), self.cor, (34, 8)))
        self.dados.append(DadoImagem(self.func, self.formato_fonte("CoText_Std_Lt", 12), self.cor, (34, 27)))
        self.dados.append(DadoImagem(self.funcING, self.formato_fonte("CoText_Std_Lt", 10), self.cor, (34, 41)))
        self.dados.append(DadoImagem(self.email, self.formato_fonte("CoText_Std_Lt", 12), self.cor, (34, 59)))
        self.dados.append(DadoImagem(self.telefone, self.formato_fonte("CoText_Std_Lt", 12), self.cor, (34, 80)))
        self.dados.append(DadoImagem(self.ender, self.formato_fonte("CoText_Std_Lt", 12), self.cor, (34, 110)))
        self.dados.append(DadoImagem(self.cidade, self.formato_fonte("CoText_Std_Lt", 12), self.cor, (34, 121)))

    def desenho(self, work):
        imagem = ImageDraw.Draw(work)
        for indice in range(0, len(self.dados)):
            imagem.text(self.dados[indice].coordenada, self.dados[indice].texto, self.dados[indice].cor, self.dados[indice].fonteNome)
        self.dados.clear()


def Criar_assinatura(imagem, name_imagem):
    nome = str(input('Nome: '))
    func = str(input('Função: '))
    email = str(input('Email: '))
    telefone = str('Fone: ' + input('Telefone: '))
    hotel = BandeiraHoteis()

    def hora():
        return time.strftime("%H_%M_%S", time.localtime())

    if 'GOLDEN' in name_imagem:
        funcIng = str(input('Função em inglês: '))
        nomeHotel = str(input('Nome do hotel: '))
        ender = str(input('Endereço: '))
        cidade = str(input('Cidade: '))
        try:
            hotel.golden(nome, func, funcIng, nomeHotel, ender, cidade, email, telefone)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    elif 'ROYAL' in name_imagem:
        try:
            hotel.royal(nome, func, email, telefone)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    elif 'TULIP_INN' in name_imagem:
        try:
            hotel.tulipinn(nome, func, email, telefone)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    elif 'SOFT_INN' in name_imagem:
        funcIng = str(input('Função em inglês: '))
        ender = str(input('Endereço(rua): '))
        cidade = str(input('Cidade(nº, cidade, estado): '))
        try:
            hotel.softinn(nome, func, funcIng, email, telefone, ender, cidade)
        except OSError:
            print('Fonte não encontrada, instale as fontes')
            time.sleep(2)

    hotel.desenho(imagem)

    save_file_folder = os.path.join(os.getcwd(), 'destino')

    if os.path.isdir(save_file_folder) == False:
        os.mkdir(save_file_folder)
        print('\nFoi criada uma pasta de destino: {}'.format(save_file_folder))

    name_image_save = str(input('\nNome para salvar: ')) + '_'

    imagem.save(os.path.join(save_file_folder, (name_image_save + hora() + '.png')))

    print('Imagem salva em: {}'.format(save_file_folder))

    saida = input('Para sair digite "sair", caso contrário, pressione qualquer tecla: ')

    if saida.lower() == 'sair':
        print()
        print('*********** BYE! ***********')
        time.sleep(2)
        exit()
    else:
        time.sleep(1)
    main()


def visual():
    print('***********************************************')
    print('***** PROJETO ASSINATURA DE E-MAIL LOUVRE *****')
    print('*********** ESCOLHA DENTRE AS OPÇÕES **********')
    print('****** A ASSINATURA DE E-MAIL QUE DESEJA ******')
    print('***********************************************')
    print()


def main():
    while True:
        visual()
        name_imagem, path_imagem = localizarImagens()
        imagem = Image.open(path_imagem)
        Criar_assinatura(imagem, name_imagem)

main()
