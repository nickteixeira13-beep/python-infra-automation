# ==========================================
# SCRIPT INTEGRADOR DE INFRAESTRUTURA - NOC
# ==========================================

# 1. Função de Retry (Módulo 3 + Módulo 4)
def testar_conexao_rede(host):
    print(f"\n[+] Iniciando handshake de rede com: {host}")
    tentativas = 0
    limite_tentativas = 3
    
    while tentativas < limite_tentativas:
        tentativas += 1
        print(f"    -> Tentativa {tentativas} de {limite_tentativas}...")
        
        # Simulamos que na 2ª tentativa a conexão estabilizou
        if tentativas == 2:
            print(f"    [Sucesso] Conexão estabelecida com {host}!")
            return True
            
    print(f"    [Falha Critica] Host {host} inalcançável após {limite_tentativas} tentativas.")
    return False


# 2. Função de Diagnóstico e Regras de Firewall/ACL (Módulo 2 + Módulo 4)
def diagnosticar_servidor(servidor):
    if servidor == "web-01":
        return "Status: Operacional (Carga web balanceada)"
    elif servidor == "db-01":
        return "Status: Alerta - Conexão de banco instável (Latência alta)"
    elif servidor == "cache-01":
        return "Status: Operacional (Cluster Redis ativo)"
    else:
        return "Status: Desconhecido (Host não catalogado na ACL)"


# 3. Bloco Principal de Execução
if __name__ == "__main__":
    print("==========================================")
    print(" INICIANDO VARREDURA AUTOMATIZADA DE FROTA")
    print("==========================================")
    
    # Inventário de servidores da infraestrutura
    inventario_servidores = ["web-01", "db-01", "cache-01"]
    
    # Laço for varrendo a infraestrutura (Módulo 3)
    for host in inventario_servidores:
        print(f"\n------------------------------------------")
        print(f"Analisando ativo: {host}")
        
        # Chamando a função de testes de rede
        conectado = testar_conexao_rede(host)
        
        # Se conectou, aplicamos o diagnóstico de regras
        if conectado:
            diagnostico = diagnosticar_servidor(host)
            print(f"    {diagnostico}")
        else:
            print(f"    Ação de segurança: Isolando o host {host} da rede.")

    print("\n==========================================")
    print(" VARREDURA CONCLUÍDA COM SUCESSO.")
    print("==========================================")