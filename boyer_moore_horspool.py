def buscar(texto, padrao):
    n, m = len(texto), len(padrao)
    
    ocorrencias, comparacoes = [], 0
    
    if m > n: return [], 0
    
    # Tabela de saltos (Bad Character Rule simplificada)
    tabela_pulos = {padrao[i]: m - 1 - i for i in range(m - 1)}
    
    i = 0
    while i <= n - m:
        j = m - 1
        # Comparacao direita para esquerda
        while j >= 0:
            comparacoes += 1
            if texto[i + j] == padrao[j]:
                j -= 1
            else:
                break
        if j < 0:
            ocorrencias.append(i)
        
        # Pulo baseado no último caractere da janela atual
        caractere_fim = texto[i + m - 1]
        i += tabela_pulos.get(caractere_fim, m)
    return ocorrencias, comparacoes