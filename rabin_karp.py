def buscar(texto, padrao):
    n, m = len(texto), len(padrao)
    
    ocorrencias, comparacoes = [], 0
    
    if m == 0 or m > n: return [], 0
    
    d, q = 256, 101 # d: alfabeto, q: primo para modulo
    h = pow(d, m-1) % q # Valor usado para remover o caractere que sai da janela
    p_hash = 0 
    t_hash = 0
    
    # --- PRÉ-PROCESSAMENTO ---
    # Hash inicial do padrao e da primeira janela
    for i in range(m):
        p_hash = (d * p_hash + ord(padrao[i])) % q
        t_hash = (d * t_hash + ord(texto[i])) % q
    
    # --- BUSCA ---  
    for i in range(n - m + 1):
        comparacoes += 1 
        if p_hash == t_hash:
            if texto[i : i+m] == padrao:
                ocorrencias.append(i)
                
        # Atualiza hash (Rolling Hash)
        if i < n - m:
            t_hash = (d * (t_hash - ord(texto[i]) * h) + ord(texto[i+m])) % q
            if t_hash < 0: t_hash += q 
    return ocorrencias, comparacoes