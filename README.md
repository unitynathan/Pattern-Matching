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
## 🛠️ Saída Esperada

``` text
===============================================================================================
                           TESTE DE CORRETUDE E MÉTRICAS DE ENTRADA
===============================================================================================

>> Cenário: Início e Fim | Texto: 'abracadabra' | Padrão: 'abra'
Algoritmo       | Índices Achados    | Comps    | Tempo (ms)   | Mem (KB)
-----------------------------------------------------------------------------------------------
Força Bruta     | [0, 7]             | 16       | 0.023100     | 0.031
Rabin-Karp      | [0, 7]             | 8        | 0.030600     | 0.075
KMP             | [0, 7]             | 15       | 0.011400     | 0.062
BMH             | [0, 7]             | 9        | 0.010600     | 0.094
Sunday          | [0, 7]             | 10       | 0.010300     | 0.031
Boyer-Moore     | [0, 7]             | 9        | 0.019200     | 0.094

>> Cenário: Repetido | Texto: 'banana' | Padrão: 'na'
Algoritmo       | Índices Achados    | Comps    | Tempo (ms)   | Mem (KB)
-----------------------------------------------------------------------------------------------
Força Bruta     | [2, 4]             | 7        | 0.005400     | 0.031
Rabin-Karp      | [2, 4]             | 5        | 0.009400     | 0.073
KMP             | [2, 4]             | 7        | 0.009600     | 0.047
BMH             | [2, 4]             | 6        | 0.015900     | 0.031
Sunday          | [2, 4]             | 5        | 0.005900     | 0.031
Boyer-Moore     | [2, 4]             | 6        | 0.012800     | 0.062

>> Cenário: Meio | Texto: 'python' | Padrão: 'th'
Algoritmo       | Índices Achados    | Comps    | Tempo (ms)   | Mem (KB)
-----------------------------------------------------------------------------------------------
Força Bruta     | [2]                | 6        | 0.004500     | 0.031
Rabin-Karp      | [2]                | 5        | 0.007900     | 0.042
KMP             | [2]                | 7        | 0.004700     | 0.047
BMH             | [2]                | 4        | 0.006000     | 0.031
Sunday          | [2]                | 3        | 0.008100     | 0.031
Boyer-Moore     | [2]                | 4        | 0.012400     | 0.062

>> Cenário: Inexistente | Texto: 'computador' | Padrão: 'java'
Algoritmo       | Índices Achados    | Comps    | Tempo (ms)   | Mem (KB)
-----------------------------------------------------------------------------------------------
Força Bruta     | []                 | 7        | 0.003600     | 0.000
Rabin-Karp      | []                 | 7        | 0.008300     | 0.000
KMP             | []                 | 13       | 0.005900     | 0.039
BMH             | []                 | 2        | 0.004200     | 0.000
Sunday          | []                 | 2        | 0.004200     | 0.000
Boyer-Moore     | []                 | 2        | 0.011200     | 0.070

>> Cenário: Sobreposição | Texto: 'aaaaa' | Padrão: 'aa'
Algoritmo       | Índices Achados    | Comps    | Tempo (ms)   | Mem (KB)
-----------------------------------------------------------------------------------------------
Força Bruta     | [0, 1, 2, 3]       | 8        | 0.005000     | 0.031
Rabin-Karp      | [0, 1, 2, 3]       | 4        | 0.011000     | 0.073
KMP             | [0, 1, 2, 3]       | 6        | 0.007300     | 0.047
BMH             | [0, 1, 2, 3]       | 8        | 0.006900     | 0.031
Sunday          | [0, 1, 2, 3]       | 8        | 0.006100     | 0.031
Boyer-Moore     | [0, 1, 2, 3]       | 8        | 0.012000     | 0.062

--- Cenário: Texto Pequeno / Padrão Curto ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 111          | 0.0156     | 0.2109       | OK
Rabin-Karp      | 91           | 0.0262     | 0.1699       | OK
KMP             | 99           | 0.0131     | 0.1953       | OK
BMH             | 40           | 0.0070     | 0.1562       | OK
Sunday          | 40           | 0.0067     | 0.1562       | OK
Boyer-Moore     | 40           | 0.0109     | 0.2344       | OK

--- Cenário: Texto Médio / Padrão Curto ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 11496        | 4.4112     | 38.7500      | OK
Rabin-Karp      | 9496         | 16.8654    | 38.7949      | OK
KMP             | 9504         | 5.7533     | 38.7891      | OK
BMH             | 4000         | 3.0809     | 38.7500      | OK
Sunday          | 4000         | 3.3089     | 38.7500      | OK
Boyer-Moore     | 4000         | 6.3995     | 38.8281      | OK

--- Cenário: Texto Grande / Padrão Curto ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 574996       | 237.7797   | 1989.6250    | OK
Rabin-Karp      | 474996       | 918.2342   | 1989.6699    | OK
KMP             | 475004       | 299.4602   | 1989.6641    | OK
BMH             | 200000       | 163.0668   | 1989.6250    | OK
Sunday          | 200000       | 171.2099   | 1989.6250    | OK
Boyer-Moore     | 200000       | 353.6579   | 1989.7031    | OK

--- Cenário: Texto Grande / Padrão Longo ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 974906       | 103.8678   | 0.0625       | N/A
Rabin-Karp      | 474947       | 129.6391   | 0.1914       | N/A
KMP             | 475056       | 67.1126    | 0.4609       | N/A
BMH             | 24999        | 6.1620     | 0.6250       | N/A
Sunday          | 37515        | 9.5485     | 0.6250       | N/A
Boyer-Moore     | 24999        | 6.5915     | 1.2734       | N/A

--- Cenário: DNA Grande / Padrão Curto ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 174997       | 70.6093    | 1986.3438    | OK
Rabin-Karp      | 99997        | 216.3175   | 1986.4189    | OK
KMP             | 100003       | 69.7465    | 1986.3750    | OK
BMH             | 100000       | 59.4487    | 1986.3750    | OK
Sunday          | 100000       | 60.8769    | 1986.3438    | OK
Boyer-Moore     | 100000       | 118.5872   | 1986.4375    | OK

--- Cenário: DNA Grande / Padrão Longo ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 574905       | 183.9991   | 1986.0938    | OK
Rabin-Karp      | 99981        | 216.8929   | 1986.1846    | OK
KMP             | 100019       | 68.7690    | 1986.2500    | OK
BMH             | 499920       | 170.4159   | 1986.1250    | OK
Sunday          | 499920       | 177.9864   | 1986.0938    | OK
Boyer-Moore     | 499920       | 438.6310   | 1986.4375    | OK

--- Cenário: Muitas Ocorrências ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 10000        | 6.8524     | 775.3438     | OK
Rabin-Karp      | 10000        | 17.3313    | 775.3438     | OK
KMP             | 10000        | 11.2576    | 775.3516     | OK
BMH             | 10000        | 14.8968    | 775.3750     | OK
Sunday          | 10000        | 15.1240    | 775.3438     | OK
Boyer-Moore     | 10000        | 24.5882    | 775.3906     | OK

--- Cenário: Poucas Ocorrências ---
Algoritmo       | Comparações  | Tempo (ms) | Memória (KB) | Status
---------------------------------------------------------------------------
Força Bruta     | 10001        | 1.2012     | 0.0938       | OK
Rabin-Karp      | 10001        | 2.1197     | 0.0938       | OK
KMP             | 10001        | 1.4525     | 0.1016       | OK
BMH             | 10001        | 2.4415     | 0.0938       | OK
Sunday          | 5001         | 1.2309     | 0.0938       | OK
Boyer-Moore     | 10001        | 2.8001     | 0.1094       | OK
```