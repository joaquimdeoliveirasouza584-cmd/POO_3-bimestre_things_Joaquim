"IFRO - Instituto Federal de Educação, Ciência e Tecnologia de Rondônia"
"Grupo:Matheus Guimarães, Murilo Araujo, Joaquim de Oliveira, Felipe Claudino, Dalila Uchoa"
class Usuário:
    def __init__ (self, Nome:str, Idade:int, CPF:int, Endereço:str, Telefone:int, Senha:str):
#ATRIBUTOS
        self.nome=Nome
        self.idade=Idade
        self.cpf=CPF
        self.endereco=Endereço
        self.telefone=Telefone
        self.senha=Senha

#MÉTODOS
    def EfetuarCadastro(self):
            self.nome = str(input("Insira seu nome: "))
            self.idade = int(input("Insira sua idade: "))
            self.cpf = float(input("Insira seu CPF: "))
            self.senha = str(input("Defina a senha: "))

    def EfetuarLogin(self):
        print("Realizando Login: ")
        Nome2 = str(input("Insira seu nome: "))
        Idade2 = int(input("Insira sua idade: "))
        CPF2 = float(input("Insira seu CPF: "))
        Senha2 = str(input("Insira a senha: "))

        print("Realizando Login...")

        if Nome2 == self.nome and Idade2 == self.idade and CPF2 == self.cpf and Senha2 == self.senha:
            print("Login sucedido!")
        else:
            print("Falha ao realizar Login")


    def AutenticarUsuário(self):
        print("Autenticando Usuario",self.nome,"ao sistema")

    def RecuperarAcesso(self):
        forma = int(input("forma de recuperação: \n1)CPF 2)Nome"))
        if forma == 1:
            cpf = str("Insira o CPF cadastrado: ")
            if cpf == self.cpf:
                print("Acesso recuperado! ")
        elif forma == 2:
            nome = str("Insira o nome cadastrado: ")
            if nome == self.nome:
                print("Acesso recuperado! ")
        else:
            print("Opção invalida!")

class Victim(Usuário):
    def __init__ (self, MedidaProtetiva:str):
#ATRIBUTOS
        self.medidaprotetiva=MedidaProtetiva

#MÉTODOS    
    def AcionarEmergência(self):
            print("acionando emergencia! ")
    def SolicitarAtendimento(self):
        telefone = int(input("digite o numero do serviço desejado: "))
        if telefone == 190:
            print("Alô, Capitão Nascimento na escuta! Qual a sua denúncia?")
        elif telefone == 192:
            print("Alô, serviço do SAMU, qual a emergência? ")
        elif telefone == 193:
            print("Alô, corpo de bombeiros na escuta, qual seria a situação?")
        else:
            print("Número errado ou inexistente")

    def AtivarLocalização(self):
        print(f"Localização ativada: {Usuário.endereco}")

    def __init__(self, Nome:str, Idade:int, CPF:int, Endereço:str, Telefone:int, Senha:str):
        super().__init__(Nome, Idade, CPF, Endereço, Telefone, Senha)
#HERANÇA DA SUPER CLASSE - USUARIO


class Polícia(Usuário):
    def __init__ (self, Mandato:str, Patente:str, Status:str, Departamento:int):
#ATRIBUTOS
        self.mandato=Mandato
        self.patente=Patente
        self.status=Status
        self.departamento=Departamento

#MÉTODOS

    def __init__(self):
        self.Delegacia = Delegacia()
    def RecebendoSOS():
        print(f"Recebendo ligação do usuario registrado: {Victim.nome}")

    def MandarViatura(self):
        return Viatura
    def RegistrarDenúncia(self):
        print(f"Registrando denuncia do agente: {Polícia.nome}")

    def __init__(self, Nome:str, Idade:int, CPF:int, Endereço:str, Telefone:int, Senha:str):
        super().__init__(Nome, Idade, CPF, Endereço, Telefone, Senha)
#HERANÇA DA SUPER CLASSE - USUARIO

class Serviço:
    def __init__ (self, Número:int, Nome:str, Endereço:str):
#ATRIBUTOS
        self.numero=Número
        self.nome=Nome
        self.endereco=Endereço

#MÉTODOS
    def ReceberAtendimento(self):
        print("atendendo o chamado de emergência da vitima....")
    def EnviarVeículo(self):
        print(f"Veículo a caminho do local informado:{self.endereco} *efeito sonoro de carro ligando*")

class Viatura:
    def __Init__ (self, Modelo:str, Marca:str, Placa:str, Camburao:str):
#ATRIBUTOS
        self.modelo=Modelo
        self.marca=Marca
        self.placa=Placa
        self.camburao=Camburao

#MÉTODOS
    def AcionarSirene(self):
        print("Acionando sirene de alerta *barulho da sírene*")
    def ChecarLocalização(self):
        print(f"Calculando rota...\nEndereco utilizado para o calculo: {Usuário.endereco} ")
    def ComunicarDelegacia(self):
        print("Chegando no local da denuncia, câmbio!")


class Delegacia:
    def __init__ (self, Endereço:str, Contato:str, Nome:str):
#ATRIBUTOS
        self.endereco=Endereço
        self.contato=Contato
        self.nome=Nome

#MÉTODOS
    def ReceberSOS(self):
        print(f"Recebendo ligação do usuario registrado: {Victim.nome}")
    def MandarViatura(self):
        return Viatura
    def RegistrarDenúncia(self):
        print(f"Registrando denuncia do agente: {Polícia.nome}")

class Bombeiros(Serviço):
    def __init__ (self, Equipamentos:list, Especialidade:str, Expediente:int):
#ATRIBUTOS
        self.equipamentos=Equipamentos
        self.especialidade=Especialidade
        self.expediente=Expediente

#MÉTODOS
    def Prestar_socorro():
        print("Salvando vidas...")
    def Checar_denúncia():
        print(f"Verificando denuncia: {Polícia.mandato}")
    def Arrombamento():
        print("Arrombando fechadura...")
    def Extinguir_incêndio():
        print("Resgatando pessoas do fogo ")
    def __init__(self, Número:int, Nome:str, Endereço:str):
        super().__init__(Número, Nome, Endereço)
#HERANÇA DA SUPER CLASSE - SERVIÇO


class SAMU(Serviço):
    def __init__ (self, Equipamento_médico:list, Equipe:str, Ambulância:str):
#ATRIBUTOS
        self.equipamento_medico=Equipamento_médico
        self.equipe=Equipe
        self.ambulancia=Ambulância

#MÉTODOS
    def Alocar_ambulância():
        print(f"Enviando ambulancia: {SAMU.ambulancia}")
    def Realizar_primeirosSocorros():
        print("Prestando socorros urgentes...")
    def Comunicar_central():
        print("Relatando emergencia á central")
    def Contatar_equipe():
        print(f"Equipe {SAMU.equipe} necessitando de reforços no local: {Victim.endereco}")
    def __init__(self, Número:int, Nome:str, Endereço:str):
        super().__init__(Número, Nome, Endereço)
#HERANÇA DA SUPER CLASSE - SERVIÇO