
# Learning how logic gates in code work
class logica:
    def logic_or(A:bool,B:bool):
        return A | B 

    def logic_and(A:bool,B:bool):
        return A & B

    def logic_xor(A:bool,B:bool):
        return A ^ B

    def logic_not(A:bool):
        return not A

    def logic_nand(A:bool,B:bool):
        return logica.logic_not(logica.logic_and(A,B))

    def logic_nor(A:bool, B:bool):
        return logica.logic_not(logica.logic_or(A, B))

    def XNOR(A, B):
        return logica.logic_not(logica.logic_xor(A, B))
