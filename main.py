from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

class RestricaoDeHorario(Restricao):
  def __init__(self, estado1, estado2):
    super().__init__([estado1, estado2])
    self.estado1 = estado1
    self.estado2 = estado2

  def esta_satisfeita(self, atribuicao):
    # se nenhum dos estados está com analise no mesmo momento, então está satisfeito
    if self.estado1 not in atribuicao or self.estado2 not in atribuicao:
        return True
    return atribuicao[self.estado1] != atribuicao[self.estado2]

if __name__ == "__main__":

  #seta as listas necessárias
  variaveis = []
  dominios = {}
  equipamentosQuimicos = []

  #Define as analises existentes
  analises = {
    "A1": ["EUV", "CG"],
    "A2": ["CL", "EI"],
    "A3": ["MC", "BA"],
    "A4": ["EM"],
    "A5": ["AM", "EI"],
    "A6": ["CL", "EUV"],
    "A7": ["EUV", "MC"],
    "A8": ["CG"],
    "A9": ["EI", "BA"],
    "A10": ["EM", "CG"]
  }
  
  # contém as análises e os equipamentos químicos necessários para cada análise
  # há um dicionário onde as analises são as chaves e a lista de equipamento os valores
  # adiciona uma string formada pela nome da análise com o nome do equipamento à lista
  # Se o equipamento ainda não foi adicionado à lista de equipamentosQuimicos, então é adicionando
  for analise, listaEquipamento in analises.items():
    for equipamentoQuimico in listaEquipamento:
      variaveis.append(analise + "-" + equipamentoQuimico)
      if equipamentoQuimico not in equipamentosQuimicos:
        equipamentosQuimicos.append(equipamentoQuimico)

  # cria uma lista de variaveis contendo todas as combinações de análises e equipamentos químicos, e então define os domínios para cada variável na lista de variaveis
  # são 8 equipamentos, cada equipamento químico tem 8 possíveis estados diferentes
  for equipamento_Quimico in variaveis:
    dominios[equipamento_Quimico] = [1,2,3,4,5,6,7,8]
  
  problema = SatisfacaoRestricoes(variaveis, dominios)

  # Adiciona as restrições para cada caso
  # Cada equipamento tem uma capacidade máxima de uso diário e só pode ser usado para uma análise por vez
  # Uma análise não pode estar em 2 equipamentos ao mesmo tempo
  # Cada análise fica 1 hora em cada equipamento
  problema.adicionar_restricao(RestricaoDeHorario("A1-EUV", "A1-CG"))
  problema.adicionar_restricao(RestricaoDeHorario("A1-EUV", "A6-EUV"))
  problema.adicionar_restricao(RestricaoDeHorario("A1-EUV", "A7-EUV"))
  problema.adicionar_restricao(RestricaoDeHorario("A1-CG", "A8-CG"))
  problema.adicionar_restricao(RestricaoDeHorario("A1-CG", "A10-CG"))
  problema.adicionar_restricao(RestricaoDeHorario("A8-CG", "A10-CG"))
  problema.adicionar_restricao(RestricaoDeHorario("A6-EUV", "A7-EUV"))
  problema.adicionar_restricao(RestricaoDeHorario("A2-CL", "A2-EI"))
  problema.adicionar_restricao(RestricaoDeHorario("A2-CL", "A6-CL"))
  problema.adicionar_restricao(RestricaoDeHorario("A2-EI", "A9-EI"))
  problema.adicionar_restricao(RestricaoDeHorario("A2-EI", "A5-EI"))
  problema.adicionar_restricao(RestricaoDeHorario("A3-MC", "A3-BA"))
  problema.adicionar_restricao(RestricaoDeHorario("A3-MC", "A7-MC"))
  problema.adicionar_restricao(RestricaoDeHorario("A3-BA", "A9-BA"))
  problema.adicionar_restricao(RestricaoDeHorario("A4-EM", "A10-EM"))
  problema.adicionar_restricao(RestricaoDeHorario("A5-AM", "A5-EI"))
  problema.adicionar_restricao(RestricaoDeHorario("A5-EI", "A9-EI"))
  problema.adicionar_restricao(RestricaoDeHorario("A6-CL", "A6-EUV"))
  problema.adicionar_restricao(RestricaoDeHorario("A7-EUV", "A7-MC"))
  problema.adicionar_restricao(RestricaoDeHorario("A9-EI", "A9-BA"))
  problema.adicionar_restricao(RestricaoDeHorario("A10-EM", "A10-CG"))
  
  resposta = problema.busca_backtracking()

  print("Olá usuário, seja-bem vindo ao Laboratório de Química do SENAC :)\n")

  if resposta is None:
    print("Nenhuma resposta encontrada")
  else:
    print("Aqui estão os hórarios em quais os equipamentos podem ser útilizados para análise\n")
    for equipamentoQuimico, hora in resposta.items():
      print(f"Horário {hora}: {equipamentoQuimico}")
    