startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}
solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

print("CyberPulse Tech:", startup)
print("Segmento:", startup["segmento"])
print("Firewall:", solucoes_ativas[0])

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_1 = arquivo.readline()
    linha_2 = arquivo.readline()
    linha_3 = arquivo.readline()
    linha_4 = arquivo.readline()

print(cabecalho, end="")
print(linha_1, end="")
print(linha_2, end="")
print(linha_3, end="")
print(linha_4, end="")

valor_1 = float(linha_1.strip().split(",")[1])
valor_2 = float(linha_2.strip().split(",")[1])
valor_3 = float(linha_3.strip().split(",")[1])
valor_4 = float(linha_4.strip().split(",")[1])

total = valor_1 + valor_2 + valor_3 + valor_4

print("\n=== Painel Final ===")
print(f"Startup: {startup['nome']}")
print("Bancada: Bancada N1")
print(f"Total de infraestrutura Cloud: R$ {total:.2f}")