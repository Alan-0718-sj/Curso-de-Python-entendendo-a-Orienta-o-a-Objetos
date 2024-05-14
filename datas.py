class Data:

    def escreva(msg):
        tam = len(msg) + 4
        print('-' * tam)
        print(f' {msg}')
        print('-' * tam)

    escreva('BEM VINDO(A)! AO FORMATO DE DATAS')

    def __init__(self) -> None:
        self.dia = int(input('Digite o dia: '))
        self.mes = int(input('Digite o mês: '))
        self.ano = int(input('Digite o ano: '))

    def data_formatada(self):
        formato = int(input('Qual formato de Data deseja? \n 1.dd/mm/aaaa\n 2. mm-dd-aaaa\n 3. aaaa-mm-dd\nDigite a oção correspondente: '))
        separador = input('digite o separador de data desejado: ')
        if formato == 1:
            print('{0}{3}{1}{3}{2}'.format(self.dia,self.mes,self.ano,separador))
        elif formato == 2:
            print('{0}{3}{1}{3}{2}'.format(self.mes,self.dia,self.ano,separador))
        elif formato ==3:
            print('{0}{3}{1}{3}{2}'.format(self.ano,self.mes,self.dia,separador))
        else:
            print('Digite uma opção valida')