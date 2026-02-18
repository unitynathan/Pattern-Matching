def buscar(texto, padrao):
    n, m = len(texto), len(padrao)
    
    ocorrencias, comparacoes = [], 0
    
    # Pré-processamento (LPS) - Define o tamanho do maior prefixo que também é sufixo para cada parte do padrão
    lps = [0] * m
    j, i = 0, 1
    while i < m:
        comparacoes += 1
        if padrao[i] == padrao[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j != 0: j = lps[j-1] 
        else: lps[i] = 0; i += 1
        
    # Busca
    i = j = 0
    while i < n:
        comparacoes += 1
        if padrao[j] == texto[i]:
            i += 1; j += 1
        if j == m: # Padrão completo encontrado
            ocorrencias.append(i - j)
            j = lps[j-1]
        elif i < n and padrao[j] != texto[i]:
            if j != 0: j = lps[j-1]
            else: i += 1
    return ocorrencias, comparacoes