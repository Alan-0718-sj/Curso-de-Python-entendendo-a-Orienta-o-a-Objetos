class Data:

    def __init__(self, dia, mes, ano):
        print("Constuindo objeto... {}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def data_formatada (self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))

        