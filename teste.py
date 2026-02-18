import time
import tracemalloc  # Biblioteca para medir consumo de memória
import brute_force, rabin_karp, knuth_morris_pratt, boyer_moore, boyer_moore_horspool, boyer_moore_horspool_sunday

def testar(nome_cenario, texto, padrao):
    algoritmos = [
        ("Força Bruta", brute_force.buscar),
        ("Rabin-Karp", rabin_karp.buscar),
        ("KMP", knuth_morris_pratt.buscar),
        ("BMH", boyer_moore_horspool.buscar),
        ("Sunday", boyer_moore_horspool_sunday.buscar),
        ("Boyer-Moore", boyer_moore.buscar)
    ]

    print(f"\n--- Cenário: {nome_cenario} ---")
    print(f"{'Algoritmo':<15} | {'Comparações':<12} | {'Tempo (ms)':<10} | {'Memória (KB)':<12} | {'Status'}")
    print("-" * 75)

    for nome, func in algoritmos:
        # Inicia o rastreamento de memória para este algoritmo específico
        tracemalloc.start()
        
        tempos = []
        # Tempo médio de 5 execuções
        for _ in range(5):
            inicio = time.perf_counter()
            posicoes, comps = func(texto, padrao)
            fim = time.perf_counter()
            tempos.append((fim - inicio) * 1000)
        
        # Captura o consumo de memória (current, peak)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop() # Para o rastreamento
        
        tempo_medio = sum(tempos) / len(tempos)
        memoria_kb = peak / 1024  # Converte bytes para Kilobytes
        status = "OK" if len(posicoes) > 0 else "N/A"
        
        # Print formatado
        print(f"{nome:<15} | {comps:<12} | {tempo_medio:<10.4f} | {memoria_kb:<12.4f} | {status}")

def testar_corretude_com_metricas():
    # Conjunto de entradas para validar a lógica
    casos = [
        {"texto": "abracadabra", "padrao": "abra", "desc": "Início e Fim"},
        {"texto": "banana", "padrao": "na", "desc": "Repetido"},
        {"texto": "python", "padrao": "th", "desc": "Meio"},
        {"texto": "computador", "padrao": "java", "desc": "Inexistente"},
        {"texto": "aaaaa", "padrao": "aa", "desc": "Sobreposição"}
    ]

    algoritmos = [
        ("Força Bruta", brute_force.buscar),
        ("Rabin-Karp", rabin_karp.buscar),
        ("KMP", knuth_morris_pratt.buscar),
        ("BMH", boyer_moore_horspool.buscar),
        ("Sunday", boyer_moore_horspool_sunday.buscar),
        ("Boyer-Moore", boyer_moore.buscar)
    ]

    print("\n" + "="*95)
    print(f"{'TESTE DE CORRETUDE E MÉTRICAS DE ENTRADA':^95}")
    print("="*95)

    for caso in casos:
        print(f"\n>> Cenário: {caso['desc']} | Texto: '{caso['texto']}' | Padrão: '{caso['padrao']}'")
        print(f"{'Algoritmo':<15} | {'Índices Achados':<18} | {'Comps':<8} | {'Tempo (ms)':<12} | {'Mem (KB)':<8}")
        print("-" * 95)

        for nome, func in algoritmos:
            # Inicia rastreio de memória
            tracemalloc.start()
            
            inicio = time.perf_counter()
            posicoes, comps = func(caso['texto'], caso['padrao'])
            fim = time.perf_counter()
            
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            tempo_ms = (fim - inicio) * 1000
            mem_kb = peak / 1024
            
            # Formatação dos índices para exibição
            res_indices = str(posicoes) if posicoes else "[]"

            print(f"{nome:<15} | {res_indices:<18} | {comps:<8} | {tempo_ms:<12.6f} | {mem_kb:<8.3f}")
