import socket

def realizar_operacao(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        return num1 / num2
    else:
        return "Operação desconhecida"

def iniciar_servidor():
    host = 'localhost'
    port = 12345
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print(f"Servidor ouvindo em {host}:{port}")

    conn, addr = s.accept()
    print(f"Conexão de: {addr}")

    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        operacao, num1, num2 = data.split(',')
        resultado = realizar_operacao(operacao, float(num1), float(num2))
        conn.send(str(resultado).encode('utf-8'))
    conn.close()

if __name__ == '__main__':
    iniciar_servidor()
