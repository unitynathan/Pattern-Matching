def buscar(texto, padrao): 
    n, m = len(texto), len(padrao)
    
    ocorrencias, comparacoes = [], 0
    
    
    for i in range(n - m + 1): # i percorre cada posição possível do texto onde o padrão ainda cabe
        j = 0
        
        while j < m: # Compara caracteres da esquerda para a direita
            comparacoes += 1
            if texto[i + j] == padrao[j]:
                j += 1
            else:
                break # Se falhar, o loop interno para e o i avança apenas 1 posição
        
        
        if j == m: # Se j percorreu todo o padrão, uma ocorrência foi encontrada
            ocorrencias.append(i)
            
    return ocorrencias, comparacoes