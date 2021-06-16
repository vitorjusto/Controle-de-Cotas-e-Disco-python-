#https://wiki.python.org.br/ListaDeExerciciosProjetos
import datetime
def escrever(espaco, total, media, pessoa):
      y = datetime.datetime.now()
      
      x = str(y.strftime("%d")) + " - " + y.strftime("%m") + " - " + y.strftime("%Y")
      f = open(x, "w")

      f.write("ACME.inc\t\tuso de espaço dos usuarios\n")
      f.write("\n-------------------------------------------------------------------------\n")
      f.write("Nº\tNome\t\tespaço utilizado\t\t %\n")
      i = 0
      while i<len(pessoa):
            f.write("\n" + str(pessoa[i].numero))
            f.write("\t")
            f.write(format(pessoa[i].nome, ".50s"))
            f.write("\t\t" + str(format(pessoa[i].espaco, ".2f")))
            f.write("MB\t")
            f.write("\t\t")
            f.write(format(porcentagem[i], ".2f"))
            f.write("%")
            i +=1
      
      f.write("\n-------------------------------------------------------------------------\n")
      f.write("Soma Total é: " + str(format(total, ".2f")))
      f.write("\nA média é: " + str(format(media, ".2f")))
      
      f = open(x, "r")
      print(f.read())

def soma(espaco):
      i = 0
      for x in espaco:
            i += converter(x)
      return i

def med(espaco):
      
      i = soma(espaco)
      
      return i/len(espaco)

def converter(espaco):
      
      return espaco/1048576

def porcent(espaco):
      
      aux = []
      x = soma(espaco)

      
      for i in  espaco:
            aux.append((converter(i)/x)*100)
      
      return aux

class Person:
      def __init__(self, nome, espaco, numero):
            self.nome = nome
            self.espaco = converter(espaco[numero-1])
            self.numero = numero
            

numero = 0
a = 1
nome = 0
espaco = []
pessoa = []
total = 0
media = 0
porcentagem = []


while a:
      numero +=1
      nome = (input("Digite o nome do usuário:\n"))
      i = 1
      while i:
            try:
                  espaco.append(int(input("\nDigite o espaço utilisado:\n")))
                  i = 0
            except:
                  print("digite um numero\n")
                  i=1
      
      pessoa.append(Person(nome, espaco, numero))
      
      a = int(input("\nDigite 1 para contiuar ou 0 para sair:\n"))

porcentagem = porcent(espaco)
total = soma(espaco)
media = med(espaco)




a = 0


while a < len(pessoa):
      b = a + 1
      while b < len(pessoa):
      
      
            if pessoa[a].espaco > pessoa[b].espaco:
                  aux = pessoa[b]
                  pessoa[b] = pessoa[a]
                  pessoa[a] = aux
                  
                  aux = porcentagem[b]
                  porcentagem[b]=porcentagem[a]
                  porcentagem[a]=aux
            b +=1
      a +=1

n = int(input("Quais primeiros voce deseja ver\n\n"))
n = len(pessoa) - n

while n > 0:
      pessoa.pop()
      n-=1
      
escrever(espaco, total, media, pessoa)




