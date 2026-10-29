# APOSTILA VIVA - MÓDULO 4: Funções e Modularização

## 1. O Conceito
Uma função é um bloco de código nomeado e reutilizável que executa uma tarefa específica. Ela evita a duplicação de código (*princípio DRY - Don't Repeat Yourself*) e organiza scripts grandes em módulos fáceis de manter.

## 2. A Estrutura Básica (`def`)
* **`def`:** Palavra-chave usada para definir (criar) uma função.
* **Parâmetros:** Variáveis locais que a função recebe como entrada entre parênteses.
* **`return`:** O comando que devolve o resultado processado para o restante do script.

Exemplo conceitual:
```python
def reiniciar_servico(nome_servidor):
    print(f"Enviando comando de reinicialização para: {nome_servidor}")
    status = "Online"
    return status

# Chamando (invocando) a função:
resultado = reiniciar_servico("web-01")
print(f"Status atual do host: {resultado}")