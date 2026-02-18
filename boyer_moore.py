def buscar(texto, padrao):
    n, m = len(texto), len(padrao)
    
    ocorrencias, comparacoes = [], 0
    
    if m == 0: return [], 0

    # --- PRÉ-PROCESSAMENTO 1: Regra do Mau Caractere ---
    bad_char = {padrao[i]: i for i in range(m)}

    # --- PRÉ-PROCESSAMENTO 2: Regra do Bom Sufixo ---
    suffix = [0] * m
    f = 0
    g = m - 1
    for i in range(m - 2, -1, -1):
        if i > g and suffix[i + m - 1 - f] < i - g:
            suffix[i] = suffix[i + m - 1 - f]
        else:
            if i < g: g = i
            f = i
            while g >= 0 and padrao[g] == padrao[g + m - 1 - f]:
                g -= 1
            suffix[i] = f - g

    good_suffix = [m] * m
    j = 0
    for i in range(m - 1, -1, -1):
        if suffix[i] == i + 1:
            while j < m - 1 - i:
                if good_suffix[j] == m:
                    good_suffix[j] = m - 1 - i
                j += 1
    for i in range(m - 1):
        good_suffix[m - 1 - suffix[i]] = m - 1 - i

    # --- BUSCA ---
    i = 0
    while i <= n - m:
        j = m - 1
        # Compara da direita para a esquerda
        while j >= 0:
            comparacoes += 1
            if padrao[j] == texto[i + j]:
                j -= 1
            else:
                break
        
        if j < 0:
            ocorrencias.append(i)
            i += good_suffix[0]
        else:
            # O pulo é o máximo entre as duas regras
            pulo_bad_char = j - bad_char.get(texto[i + j], -1)
            pulo_good_suffix = good_suffix[j]
            i += max(pulo_bad_char, pulo_good_suffix)
            
    return ocorrencias, comparacoes