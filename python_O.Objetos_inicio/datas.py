class Data:

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    #f de format d de digito
    def formatar(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}")