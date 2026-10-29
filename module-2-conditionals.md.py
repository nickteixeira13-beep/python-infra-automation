# APOSTILA VIVA - MÓDULO 2: Condicionais e Tomada de Decisão (Control Flow)

## 1. O Conceito
Em programação, o código precisa tomar decisões com base em dados. O Python usa a indentação (espaços no início da linha) para saber quais blocos de código pertencem a cada condição.

## 2. Operadores de Comparação
* `==` : Igual a
* `!=` : Diferente de
* `>`  : Maior que
* `<`  : Menor que
* `>=` : Maior ou igual a
* `<=` : Menor ou igual a

## 3. A Estrutura Básica (`if`, `elif`, `else`)
* **`if` (Se):** Executa o bloco se a condição for verdadeira (`True`).
* **`elif` (Senão se):** Testa uma nova condição caso a anterior seja falsa.
* **`else` (Senão):** O "padrão" (*fallback*); executa se nenhuma das condições anteriores for atendida.

Exemplo conceitual:
```python
status_servidor = "ativo"

if status_servidor == "ativo":
    print("O sistema está operando normalmente.")
elif status_servidor == "manutencao":
    print("O sistema está em janela de manutenção.")
else:
    print("ALERTA: Servidor inacessível!")