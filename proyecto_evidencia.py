import datetime
from logging import exception
import random 
fechaactual=datetime.datetime.now()
fechaactal2=datetime.datetime.strftime(fechaactual,'%d/%m/%y')
idreservacion= 0
idsala=0
mi_lista=[]
mi_lista2=[]
lista_reservaciones= []
while True :
   print( "")
   print("(1) Registrar la reservación de una sala")
   print("(2) Editar el nombre del evento de una reservación ya hecha.")
   print("(3) Consultar las reservaciones existentes para una fecha específica.")
   print("(4) Registrar a un nuevo cliente.")
   print("(5) Registrar una sala.")
   print("(6) Salir")
   menu = int(input(f'¿Que opcion realizara?: '))
   if menu == 1:
        nomreservacion=input(f'¿Cual es nombre de la rerservacion?: ')
        cliente=input(f'¿Cual es el nombre del cliente?: ')
        sala= input(f'¿Cual sala desea reservar?: ')
        turno= input("¿Que turno deseas?: ") 
        fecha=input(f'¿Que fecha deseas reservarla (dd/mm/aaaa)?: ')
        lista_reservaciones.append(sala)
        lista_reservaciones.append(cliente)
        lista_reservaciones.append(nomreservacion)
        lista_reservaciones.append(turno)
        lista_reservaciones.append(fecha)
   elif menu == 2:
        nomreservacion=input(f'¿Cual nombre de preservacion desear cambiar?')
        nomreser=input(f'¿Cual seria el nuevo nombre?: ')
        nomreservacion = nomreser
        lista_reservaciones.append(nomreser)
   elif menu == 3:
        print(f'*' * 10)
        print(f'**',' ' * 5, 'REPORTE DE RESERVACIONES DEL DIA', fechaactal2 , ' ' * 5,'**')
        print(f'*' * 10)
        print(f'*' * 4, ' '* 5, 'SALA',' '* 5,'*' * 4,' '* 5,'CLIENTE' ,' '* 5,'*' * 4,' '* 5,'EVENTO',' '* 5,'*' * 4,' '* 5,'TURNO')
        print(f'*' * 10)
        print(lista_reservaciones[0:4])
        print(f'*' * 10, 'FIN DE REPORTE','*' * 10 )
   elif menu == 4:
        for contar in range(1,1):
            mi_lista.append (random.randint(0,1))
            lista_reservaciones(dict.fromkeys(mi_lista))
        cliente= input("¿Cual es el nombre de tu cliente?: ")
        lista_reservaciones.append (cliente)
   elif menu == 5:
        for contar in range(1,1):
            mi_lista2.append (random.randint(0,1))
            lista_reservaciones(dict.fromkeys(mi_lista2))
        nomsala=input("¿Cual es el nombre de la sala?: ")
        cuposala=int(input("¿Cual es el cupo de la sala?: "))
        lista_reservaciones.append(nomsala)
        lista_reservaciones.append(cuposala)
   elif menu == 6:
        break
#if turno == lista_reservaciones.index(""):
#            print('Se ha guardado con exito')
#        elif turno == lista_reservaciones.index(""): 
#           print('Se ha guardado con exito')  
#       else:
#           print("no se puede guardar la informacion ingrese de nuevo el turno")
#            turno= input("¿Que turno deseas?: ")
#         try:
#           lista_reservaciones.index(turno) == ""
#        except ValueError:
#            print("Se ha guardado con exito") 
#        except Exception:
#            print("se ha presentado una exepcion")
#            print(exception)
