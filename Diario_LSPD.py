def cadete():
    quantidade_cadete=int(input('Quantos cadetes serão admitidos? '))
    nome_cadete=0
    distintivo_cadete=0
    cnomes=[]
    cdistintivos=[]
    for i in range(quantidade_cadete):
      nome_cadete=str(input("Qual o nome do cadete? "))
      cnomes.append(nome_cadete)
      distintivo_cadete=str(input("Qual o distintivo? "))
      cdistintivos.append(distintivo_cadete)
    x=1
    i=0
    print('\n\n```diff\n+ Admissão de cadetes\n')
    while x<=quantidade_cadete:
      print('Oficial: #',cdistintivos[i],' ',cnomes[i],sep='')
      i=i+1
      x=x+1
    print('```')
def desligamento():
    quantidade_deslig=int(input('Quantos oficiais serão desligados? '))
    dnomes=[]
    ddistintivos=[]
    for i in range(quantidade_deslig):
      nome_desligamento=str(input('Qual o nome do oficial? '))
      dnomes.append(nome_desligamento)
      dist_deslig=str(input('Qual o distintivo do oficial? '))
      ddistintivos.append(dist_deslig)
    motivo_desligamento=str(input('Qual o motivo do desligamento? '))
    x=1
    i=0
    print('\n\n```diff\n- Desligamento\n')
    while x<=quantidade_deslig:
      print('Oficial: #',ddistintivos[i],' ',dnomes[i],sep='')
      i=i+1
      x=x+1        
    print('\nMotivo: ',motivo_desligamento,'\n```',sep='')
def readmissão():
    quantidade_readmissão=int(input('Quantos oficiais serão readmitidos? '))
    rnomes=[]
    rdistintivos=[]
    for i in range(quantidade_readmissão):
      nome_readmissão=str(input("Qual o nome do Oficial? "))
      rnomes.append(nome_readmissão)
      distintivo_readmissão=str(input("Qual o distintivo? "))
      rdistintivos.append(distintivo_readmissão)
    x=1
    i=0
    print('\n\n```diff\n+ Readmissão de oficial\n')
    while x<=quantidade_readmissão:
      print('Oficial: #',rdistintivos[i],' ',rnomes[i],sep='')
      i=i+1
      x=x+1
    print('```')

def transferêcia():
    nome_transferêcia=str(input('Qual o nome do oficial? '))
    distintivo_transferência=str(input("Qual o distintivo? " ))
    antigo_dept=str(input("Qual a sigla do antigo Departamento?" ))
    novo_dept=str(input("Qual a sigla do novo Departamento? "))
    print('\n\n```diff\n+ Transferência\n\nOficial: #',distintivo_transferência,' ',nome_transferêcia,'\n\nAntigo Departamento ',antigo_dept,'\n\nNovo Departamento: ',novo_dept,'\n```',sep='')

def cf():
    nome_curso=str(input('Qual o nome do curso? '))
    nome_cfoficial=str(input('Qual o nome do oficial? '))
    dist_cf=str(input('Qual o distintivo do oficial? '))
    situação=str(input('Ele foi aprovado ou reprovado? '))
    print('\n\n```diff\n+ Curso de formação de ',nome_curso,'\n\nOficial: #',dist_cf,' ',nome_cfoficial,'\n\nSituação: ',situação,'\n```',sep='')

def afastamento():
    nome_afast=str(input('Qual o nome do oficial? '))
    dist_afast=str(input('Qual o distintivo do oficial? '))
    motivo_afast=str(input('Qual o motivo do afastamento? '))
    print('\n\n```diff\n- Afastamento\n\nOficial: #',dist_afast,' ',nome_afast,'\n\nMotivo: ',motivo_afast,'\n```',sep='')

def diario(escolha):
  escolha=0 
  escolha=int(input('Escolha uma das opções escrevendo um número '))
  if escolha==1:
    cadete()
    
  elif escolha==2:
    desligamento()

  elif escolha==3:
    readmissão()

  elif escolha==4:
    transferêcia()

  elif escolha==5:
    cf()

  elif escolha==6:
    afastamento()

  else:
    print('Escolhe um trem certo pf?')

print('[ 1 ] Admissão de cadete\n[ 2 ] Desligamento\n[ 3 ] Readmissão de oficial\n[ 4 ] Transferência\n[ 5 ] Curso de forção de...\n[ 6 ] Afastamento\n')
escolha=0
diario(escolha)