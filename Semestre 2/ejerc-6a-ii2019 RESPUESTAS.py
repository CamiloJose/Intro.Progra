"""
Camilo Jose Solis Gonzalez

Tecnologico de Costa Rica

Trabajo de Programación
2/10/2019

"""
# Ejercicio 1
#E: reciba un vector
#S: retorne el vector inverso
#R: no se puede usat reverse

def vector_inver(v):
     if isinstance(v,list):   
          return vector_aux(v)
     else: return "Error"

def vector_aux(lista):
     if lista == []:     #caso base
          return 0
     else:
          return lista[::-1]

#Ejercicio 2
#E: ingresar escalar y vector 
#S: producto escalar multiplicado por el vector
#R: ---
     
def prod_escalar(e, v):
     if isinstance(e,int) and isinstance(v,list):
          return prod_escalar_aux(e,v,0,[])
     else: return "Error"

def prod_escalar_aux(e,v,i,new):
     if i == len(v):
          return new
     else:
          new.append(v[i]*e)
          return prod_escalar_aux(e, v,i+1,new)
     

#Ejercicio 3.
#E: dos vectores
#S: suma de la multiplicacion de los vectores de igual posicion  
#R: ---
     
def prod_vector(v, w):
     if isinstance(v,list) and isinstance(w,list):
          return prod_vector_aux(v,w,0)
     else:return "Error"

def prod_vector_aux(v,w,i):
     if i == 0:
          return 0
     else: return (v[i]*w[i]) + prod_vector_aux(v,w,i+1)
     
#Ejercicio 4
#E: vectores
#S: retornear si hay mas numeros ares (True) o no(False)
#R: ---
     
def tienemas_par(vector) :
     if isinstance(vector,list):
          return tienemas_par_aux(vector,0)
     else:return"Error"

def tienemas_par_aux(v,i):
     if i == len(v):
          return True
     elif v[i] %2 == 0:
          return tienemas_par_aux(v,i+1)
     else: return False

#Ejercicio 5
#E: vector
#S:comprobar su los elementos del primer vector estan en el segundo
#R: --- 
     
def inn(vector1, vector2):
     if isinstance(vector1,list) and isinstance(vector2,list):
          return inn_aux(vector1,vector2,0,0,0)
     else:return"Error"

def inn_aux(v1,v2,i,j,cont):
     if cont == len(v1):
          return True
     elif j == len(v2):
          return False
     elif v1[i] == v2[j]:
          return inn_aux(v1,v2,i+1,j,cont+1)
     else: return inn_aux(v1,v2,i,j+1,cont)
     

#Ejercicio 6
#E: lista
#S: esta en orden o no (booleano)
#R: --- 
     
def  ordenado(vector):
     if isinstance(vector,list):
          return ordenado_aux(vector,0)
     else: return "Error"

def ordenado_aux(v,i):
     if i == len(v)-1:
          return True
     elif v[i] < v[i+1]:
          return ordenado_aux(v,i+1)
     else: return False

#Ejercicio 7
#E: matriz n*m
#S: en consola usando print
#R: --- 
     
def muestreM(matriz):
     if isinstance(matriz,list):
         return muestreM_aux(matriz,0)
     else: return "Error"

def muestreM_aux(m,i):
     if i == len(m)-1:
          print (m[i], "]")
     elif i ==0:
          print("[",m[i],"\n")
          return muestreM_aux(m,i+1)
     else:
          print(m[i],"\n")
          return muestreM_aux(m,i+1)

#Ejercicio 8
#E: matriz
#S: promedio de los numeros de la matriz
#R: --- 
     
def  promedio(mat) :
     if isinstance(mat,list):
          return promedio_aux(mat,0,0,0,0)
     else: return "Error"

def promedio_aux(m,i,j,cont,result):
     if i == len(m):
          result /= cont
          return result
     elif (j == len(m[i])):
          return promedio_aux(m,i+1,0,cont+1,result)
     else:
          result += m[i][j]
          return promedio_aux(m,i,j+1,cont+1,result)

#Ejercicio 9
#E: matriz cuadrada o n*m
#S: la diagonal de la matriz
#R: ---
     
def diagonal(matriz):
     if isinstance(matriz,list):
          return diagonal_aux(matriz,0,0,[])
     else:return"Error"

def diagonal_aux(m,i,j,aux):
     if i == len(m):
          return aux
     else:
          aux.append(m[i][j])
          return diagonal_aux(m,i+1,j+1,aux)
