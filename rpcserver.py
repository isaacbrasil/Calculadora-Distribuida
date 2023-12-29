from xmlrpc.server import SimpleXMLRPCServer

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def iniciar_servidor():
    servidor = SimpleXMLRPCServer(("localhost", 12345))
    print("Escutando na porta 12345...")
    
    servidor.register_function(soma, "soma")
    servidor.register_function(subtracao, "subtracao")
    servidor.register_function(multiplicacao, "multiplicacao")
    servidor.register_function(divisao, "divisao")

    servidor.serve_forever()

if __name__ == "__main__":
    iniciar_servidor()
