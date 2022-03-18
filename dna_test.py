# PYTHON TEST
# Owner: Paulo de Souza
# Description: Test part 1
# Date: 02-03-2022

#Displays a welcome message
print ('This is Paulo de Souza Python CODE\n')

#################
# PART0 
#PRINTING THE INFO TO BE CHECKED
print ('This is Part 0\nLets check a specific sequence\nSequence lenght:')
DNA_Test=["CTGAGA","CTGAGC","TATTGT","AGAGGG","CCCCTA","TCACTG"] #dna data
print (len(DNA_Test)) #info size

#printing the sequence using a loop
print ('\nThat is the complete sequence:')
i=0
while i < len(DNA_Test):
  print (DNA_Test[i])
  i=i+1

#######################
#PART1
#Imprimindo o DNA 
DNA=['CCCCTA']
print (DNA[0])

#Verificando o primeiro elemento e imprimindo os elements iguais a ele
print ('\nTeste 1')
DNA=['CCCCTA']
test=DNA[0][0]
print ('Elemento: ', test)
print ('Mesmo elemento nas posicoes:')
i=0
while i < len(DNA[0]):
  if test == DNA[0][i]:
    print(i)
  i=i+1


#Testando um loop para verificar todos os elementos, sem comparar com ele mesmo
print ('\nTeste 1A')
DNA=['CCCCTA']
c=0
testado=[]
for e in DNA[0]:
  i=0
  if e not in testado:
    print ('Elemento:', e, 'analisando na posicao: ', c)
    print ('Mesmo elemento nas posicoes:')
    while i < len(DNA[0]):
      if e == DNA[0][i] and i!=c:
        print(i)
      i=i+1
  c=c+1
  testado.append(e)
print('Lista de testados: ',testado)  

#Imprimindo se os elementos forem vizinhos
#>> inicializar o contador no elemento 00 e o primeiro nested loop no elemento 1
#>> condicao de negativa (nao encontrou elemento repetitivo) modifica o elemento e da continuidade ao for
print ('\nTeste 1B')
DNA=['TCCCCA']
c=0
for i in range (0, len(DNA[0])-1):
  t=DNA[0][i]
  if DNA[0][i+1] == t:
    c=c+1
if c == 3:
  print('Sequencia Simio.')
else:
  print('Sequencia humana.')
  
#####################
# PART2 
#ENTENRING THE DATA
#DNA input
n=int(input('\n\nThis is part 2\nINPUT\nHow many DNAs info do you want to enter?\n'))

#Loop for enter de DNA data
i=0
DNA=[]
while i < n:
  data=str(input('Enter with the sequence:\n'))
  DNA.append(data)
  i=i+1

#Printing the sequences
print ('\nYou entered with the sequence:')
i=0
while i < n:
  print (DNA[i])
  i=i+1
