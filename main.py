import teste

def main():
    
    # --- CENÁRIOS DE TEXTO ---
    # Pequeno: 100 caracteres | Médio: 10.000 | Grande: 500.000
    texto_p = "algoritmo de busca " * 5
    texto_m = "algoritmo de busca " * 500
    texto_g = "algoritmo de busca " * 25000

    # --- CENÁRIOS DE PADRÃO ---
    padrao_curto = "busca"
    padrao_longo = "algoritmo de busca muito especifico para este tepytste"
    
    # 0. Teste: Teste básico com palavras simples
    teste.testar_corretude_com_metricas()

    # 1. Teste: Tamanho do Texto (Alfabeto Grande)
    teste.testar("Texto Pequeno / Padrão Curto", texto_p, padrao_curto)
    teste.testar("Texto Médio / Padrão Curto", texto_m, padrao_curto)
    teste.testar("Texto Grande / Padrão Curto", texto_g, padrao_curto)

    # 2. Teste: Comprimento do Padrão
    teste.testar("Texto Grande / Padrão Longo", texto_g, padrao_longo)

    # 3. Teste: Alfabeto Pequeno (DNA)
    texto_dna = "ATGC" * 25000 # Grande
    teste.testar("DNA Grande / Padrão Curto", texto_dna, "ATGC")
    teste.testar("DNA Grande / Padrão Longo", texto_dna, "ATGC" * 5)

    # 4. Teste: Muitas vs Poucas Ocorrências
    txt_muitas = "X" * 10000 # O padrão 'X' ocorre 10.000 vezes
    teste.testar("Muitas Ocorrências", txt_muitas, "X")
    
    txt_poucas = "A" * 10000 + "B" # O padrão 'B' ocorre 1 vez
    teste.testar("Poucas Ocorrências", txt_poucas, "B")

if __name__ == "__main__":
    main()