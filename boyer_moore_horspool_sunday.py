def buscar(texto, padrao):
    n, m = len(texto), len(padrao)
    
    ocorrencias, comparacoes = [], 0
    
    # Tabela de saltos (Next Char)
    tabela_pulos = {padrao[i]: m - i for i in range(m)}
    
    i = 0
    while i <= n - m:
        j = 0
        while j < m:
            comparacoes += 1
            if texto[i + j] == padrao[j]:
                j += 1
            else:
                break
        if j == m:
            ocorrencias.append(i)
        
        # Pulo baseado no caractere IMEDIATAMENTE APÓS a janela
        if i + m < n:
            caractere_proximo = texto[i + m]
            i += tabela_pulos.get(caractere_proximo, m + 1)
        else:
            break
    return ocorrencias, comparacoes