__author__ = 'carlosginestradiaz'


class HolaMundo():

    def __init__(self,str_out="hola que ase"):
        self.str_out = str_out

        self.print_str()



    def print_str(self):
        print self.str_out




if __name__ == "__main__":
    a=HolaMundo()
