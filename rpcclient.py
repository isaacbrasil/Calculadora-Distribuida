import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:12345/")
    
    operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if operacao == "soma":
        resultado = proxy.soma(a, b)
    elif operacao == "subtracao":
        resultado = proxy.subtracao(a, b)
    elif operacao == "multiplicacao":
        resultado = proxy.multiplicacao(a, b)
    elif operacao == "divisao":
        resultado = proxy.divisao(a, b)
    else:
        resultado = "Operação inválida."

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
