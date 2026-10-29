tentativas = 0
while tentativas < 3:
    print (f"Tentativa de conexão número {tentativas +1}... ")
    tentativas += 1
    print (f"Tentativa de conexão {tentativas +1}...")
    print (f"Tentativa de conexão {tentativas +2}...")
    print (f"Tentativa {tentativas}: Conectando ao Servidor...")
    tentativas += 2
    tentativas += 3


servidores = ["web-01", "db-01", "cache-01"]
for servidor in servidores:
    print (f"Verificando status de conexão com servidor: {servidor}")
    if servidor == "db-01":
        print (f"Servidor {servidor} está com problemas de conexão, reiniciando...")
    if servidor == "cache-01":
        print (f"Servidor {servidor} está com problemas de conexão, reiniciando...")    
    if servidor == "web-01":
        print (f"Servidor {servidor} Conexão estabelecida com sucesso!") 
    if servidor == "db-01":
        print (f"Servidor {servidor} Conexão estabelecida com sucesso!")
    if servidor == "cache-01":
        print (f"Servidor {servidor} Conexão estabelecida com sucesso!")
    if servidor == "web-01":
        print (f"Servidor {servidor} Conexão estabelecida com sucesso!")
                    