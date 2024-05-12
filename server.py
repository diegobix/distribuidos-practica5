import Pyro5.core
import Pyro5.server

@Pyro5.server.expose
class Calculadora:
    def sumar(self, n1, n2):
        return n1 + n2
    
    def restar(self, n1, n2):
        return n1 - n2
    
    def multiplicar(self, n1, n2):
        return n1 * n2
    
    def dividir(self, n1, n2):
        if n2 == 0:
            return None
        return n1 / n2
    
daemon = Pyro5.server.Daemon()
uri = daemon.register(Calculadora)

nameserver = Pyro5.core.locate_ns()
nameserver.register("Calculadora", uri)

daemon.requestLoop()