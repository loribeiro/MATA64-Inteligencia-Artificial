import random

class Ambiente:
    """
        Classe responsável por manter armazenar
        o estado atual do ambiente em que o agente está
        inserido.
    """
    def __init__(self):
        self.posicao_atual = "A" if random.randint(0,1) else "B" # posicao atual do aspirador de pó
        self.situacao_atual = None # armazena a ultima leitura do sensor
        self.estavel = 0 # soma a quantidade de estados limpos seguidos para evitar se movimentar desnecessariamente

    def definir_situacao(self, nova_situacao):
        """
            checa se a situacao atual é igual ou diferente da acao anterior
            e atualiza a variavel que calcula as rodadas estaveis
        """
        if self.situacao_atual == nova_situacao and nova_situacao != "Sujo":
            self.estavel += 1
        else:
            self.estavel = 0
            self.situacao_atual = nova_situacao
    
    def ambiente_estavel(self):
        """
            Retorna se o ambiente é estável ou não 
        """
        if self.estavel>=2:
            return True
        else:
            return False

class Percepcao:
    """
        Classe responsável por simular a ação de um sensor.
        Verifica qual o estado do ambiente através da entrada do usuário
    """
    def __init__(self):
        self.situacao = None # situação do ambiente

    def recuperar_situacao(self):
        return self.situacao

    def verificar_ambiente(self):
        """
            Se o usuário digitar o número 0, o sensor entenderá o ambiente como sujo.
            Do contrario, o ambiente será entendido como limpo
        """
        entrada_sensor = int(input("Estado do Ambiente (0-Sujo,1-Limpo):"))
        if entrada_sensor == 0:
            self.situacao = "Sujo"
        else:
            self.situacao = "Limpo"

        return self.situacao

class Agente:
    """
        Classe responsável por representar o agente,
        detem uma instancia do sensor e do ambiente.
        Determina qual a ação a ser tomada de acordo com o estado do sensor e do ambiente.
        Retorna ao usuário a ação escolhida 
    """
    def __init__(self):
        self.sensor =  Percepcao()
        self.ambiente = Ambiente()

    def __saida_terminal(self):
        print("Posição Atual: ", self.ambiente.posicao_atual)

    def interagir_com_ambiente(self):
        self.__saida_terminal()
        self.ambiente.situacao_atual = self.sensor.verificar_ambiente()
        acao = self.__executar_acao()
        print("Ação executada: ",acao, "\n\n")

    def __executar_acao(self):
        if self.sensor.recuperar_situacao() == "Sujo":
            self.ambiente.definir_situacao(self.sensor.situacao)
            return "Sugar"
        if self.ambiente.ambiente_estavel():
            return "Permanecer"

        return self.__decidir_direcao() 
    
    def __decidir_direcao(self):
        if self.ambiente.posicao_atual == "A":
            self.ambiente.posicao_atual = "B"
            self.ambiente.definir_situacao(self.sensor.situacao)
            return "ir para direita"
        else:
            self.ambiente.posicao_atual = "A"
            self.ambiente.definir_situacao(self.sensor.situacao)
            return "ir para esquerda"


def main():
    reflex_agente = Agente() 
    while True:
        reflex_agente.interagir_com_ambiente()

if __name__ == "__main__":
    main()       