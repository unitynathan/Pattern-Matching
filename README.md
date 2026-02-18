# Algoritmos de Busca de Padrões em Strings

Este projeto consiste na implementação e estudo comparativo de diversos algoritmos de casamento de cadeias (*string matching*). O objetivo é entender o funcionamento e analisar a eficiência de cada abordagem em diferentes cenários, mensurando tempo de execução, número de comparações e consumo de memória.

## 🚀 Algoritmos Implementados

O projeto contempla os seguintes algoritmos, organizados de forma modular:

* **Força Bruta (Naive):** Abordagem direta que compara o padrão em todas as janelas possíveis do texto.
* **Rabin-Karp:** Utiliza técnica de *rolling hash* para filtrar candidatos antes da comparação real.
* **Knuth-Morris-Pratt (KMP):** Otimiza a busca evitando retrocessos através da tabela de prefixos (LPS).
* **Boyer-Moore:** Utiliza as regras do "Mau Caractere" e "Bom Sufixo" para realizar saltos eficientes da direita para a esquerda.
* **BMH (Boyer-Moore-Horspool):** Versão simplificada do Boyer-Moore baseada na regra do caractere ruim.
* **Sunday:** Variante do BMH que utiliza o caractere imediatamente após a janela para maximizar o tamanho dos saltos.

---

## 📂 Estrutura do Projeto

```text
.
├── brute_force.py                  # Implementação da Força Bruta
├── rabin_karp.py                   # Implementação do Rabin-Karp
├── knuth_morris_pratt.py           # Implementação do KMP
├── boyer_moore.py                  # Implementação do Boyer-Moore Completo
├── boyer_moore_horspool.py         # Implementação do BMH
├── boyer_moore_horspool_sunday.py  # Implementação do Sunday
└── teste.py                        # Script de benchmark 
└── main.py                         # Testes de cenários

```
---

## 📊 Metodologia de Testes

* **Variação de Tamanho:** Testes com textos pequenos, médios e grandes.
* **Variação de Padrão:** Comparação entre padrões curtos e padrões longos.
* **DNA (Bioinformática):** Alfabeto reduzido {A, C, T, G} com alta taxa de repetição.
* **Linguagem Natural:** Alfabeto grande (ASCII) com textos em português.
* **Densidade de Ocorrências:** Casos com múltiplos casamentos vs. nenhuma ocorrência.

### Métricas Coletadas:

* **Tempo de Execução (ms):** Medido através de time.perf_counter().

* **Número de Comparações:** Contagem de operações de igualdade entre caracteres.

* **Consumo de Memória (KB):** Rastreamento de pico de alocação de memória via tracemalloc.

## 🛠️ Como Executar

``` text

    python main.py
    
```