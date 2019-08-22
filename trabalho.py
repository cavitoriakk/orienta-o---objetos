class Hospital:
    def __init__(self, nome, endereco, telefone, hora_funcionamento, public_private ):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.hora_funcionamento = hora_funcionamento
        self.public_private = public_private

    def Imprimir(self):
        print(Hospital)


class Paciente(Hospital):

    def __init__(self, infermidade, sintomas, nivel_de_risco):
        super().__init__(infermidade, sintomas)
        self.nivel_de_risco = nivel_de_risco

    def Imprimir2(self):
        print(Paciente)

class Pessoa (Hospital):
    def __init__(self, nome, idade, RG, nacionalidade, CPF):
        super().__init__(Pessoa)
        self.Imprimir()


Hospital = Hospital('San Diego', 'Caieiras', '1170707070', '24 horas', 'publico e privado')
Paciente = Paciente('AIDS', 'dores', 'infectavel')
Pessoa = Pessoa ('Lidiane', '16 anos', '578347952204', 'brasileira', '895379275932')

print(Paciente.Pessoas)