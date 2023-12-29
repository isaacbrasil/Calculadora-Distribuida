import socket

def enviar_requisicao(servidor, port, operacao, num1, num2):
    s = socket.socket()
    s.connect((servidor, port))
    s.send(f"{operacao},{num1},{num2}".encode('utf-8'))
    resultado = s.recv(1024).decode('utf-8')
    s.close()
    return resultado

if __name__ == '__main__':
    servidor = 'localhost'
    port = 12345
    operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = enviar_requisicao(servidor, port, operacao, num1, num2)
    print(f"Resultado: {resultado}")
