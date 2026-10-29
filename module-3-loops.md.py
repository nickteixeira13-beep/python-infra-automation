# APOSTILA VIVA - MÓDULO 3: Laços de Repetição (Loops)

## 1. O Conceito
Loops permitem que um bloco de código seja executado repetidamente até que uma condição seja satisfeita ou que uma lista de elementos se esgote.

## 2. O Laço `while` (Enquanto)
* **Comportamento:** Repete um bloco de código **enquanto** uma condição lógica for verdadeira (`True`).
* **Cuidado de Infra:** Se a condição nunca se tornar falsa, você cria um **Loop Infinito** (*Infinite Loop*), equivalente a um processo travado consumindo 100% de CPU.
* **Exemplo conceitual:**
  ```python
  tentativas = 0
  while tentativas < 3:
      print(f"Tentativa de conexão número {tentativas + 1}...")
      tentativas = tentativas + 1

      servidores = ["web-01", "db-01", "cache-01"]
for servidor in servidores:
    print(f"Verificando status do servidor: {servidor}")

    