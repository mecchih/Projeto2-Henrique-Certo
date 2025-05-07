import funcoes
cartela_de_pontos = {'regra_simples':  {'1':-1,'2':-1,'3':-1,'4':-1,'5':-1,'6':-1},'regra_avancada' : {'sem_combinacao':-1,'quadra':-1,'full_house': -1,'sequencia_baixa': -1, 'sequencia_alta':-1,'cinco_iguais': -1}}
for r in range(12):
    funcoes.imprime_cartela(cartela_de_pontos)
    dados_rolados = funcoes.rolar_dados(5)
    dados_guardados = []
    rolagem = 0
    
    while True:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados Guardados: {dados_guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ')

        acao = int(input('Qual ação deseja realizar?  '))
        acoes_possiveis = [0,1,2,3,4]

        while acao not in acoes_possiveis:
            print("Opção inválida. Tente novamente.")
            acao = int(input('Qual acão deseja realizar?: '))

        if acao == 1:
            print ('Digite o índice do dado a ser guardado (0 a 4): ')
            numero_dado = int(input())
            for j in range(len(dados_rolados)):
                if numero_dado == j:
                    dados_rolados,dados_guardados = funcoes.guardar_dado(dados_rolados,dados_guardados,numero_dado)
                
        elif acao == 2:
            print('Digite o índice do dado a ser removido (0 a 4): ')
            numero_dado = int(input())
            for p in range(len(dados_rolados)):
                if numero_dado == p:
                    dados_rolados,dados_guardados = funcoes.remover_dado(dados_rolados,dados_guardados,numero_dado)
        
        elif acao == 3:
            if rolagem == 2:
                print("Você já usou todas as rerrolagens.")

            else:
                rolagem += 1
                dados_rolados = funcoes.rolar_dados(5-len(dados_guardados))
        
        elif acao == 4:
            funcoes.imprime_cartela(cartela_de_pontos)
            
        
        elif acao == 0:
            print("Digite a combinação desejada: ")
            combinacao = input()
            
            lista_dados = dados_guardados + dados_rolados

            if combinacao not in cartela_de_pontos['regra_simples'] and combinacao not in cartela_de_pontos['regra_avancada']:
                print( "Combinação inválida. Tente novamente.")

            if combinacao in cartela_de_pontos['regra_simples']:
                if cartela_de_pontos['regra_simples'][combinacao] == -1:
                    funcoes.faz_jogada(lista_dados,combinacao,cartela_de_pontos)

                else:
                    print("Essa combinação já foi utilizada.")

            if combinacao in cartela_de_pontos['regra_avancada']:
                if cartela_de_pontos['regra_avancada'][combinacao] == -1:
                    funcoes.faz_jogada(lista_dados,combinacao,cartela_de_pontos)

                else:
                    print("Essa combinação já foi utilizada.")
            
funcoes.imprime_cartela(cartela_de_pontos)
pontuacao = 0
soma = 0

for pontos in cartela_de_pontos['regra_simples'].values():
    if pontos != 0:
        soma += pontos
        pontuacao += pontos 
    
for pontos in cartela_de_pontos['regra_avancada'].values():
    if pontos != 0:
        pontuacao += pontos

if soma >= 63:
    pontuacao +=35

print(f'"Pontuação total: {pontuacao}"')
