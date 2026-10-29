servidores = ["web_01", "db_01", "cache_01"]

def verificar_status(servidor):
    if servidor =="web_01":
        return "Operacional com carga web"
    elif servidor == "db_01":
        return "Alerta: Conexão de banco instável"
    else:
        return "Status desconhecido"

    #2. Bloco principal de execução
if __name__ == "__main__":
    #Definimos a lista de ativos de infraestrutura
    servidores = ["web_01", "db_01", "cache_01"]
    #Usamos o laço "for" para varrer a lista e chamar a função modularizada
    for host in servidores:
        print(f"Verificando status de conexão com servidor: {host}")
        #Invocamos a função passando o host atual como argumento
        resultado = verificar_status(host)

        print(f"-> Resposta do host {resultado}\n")
