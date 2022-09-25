from config.wsgi import *
from core.erp.models import Type, Employee

# Listar

# # select * from tabla
# query = Type.objects.all()
#
# print(query)

# # Insercion
# t = Type()
# t.name = 'Prueba'
# t.save()

# # Edicion
# try:
#     t = Type.objects.get(id=3)
#     t.name = 'Presidente'
#     t.save()
# except Exception as e:
#     print(e)

# # Eliminacion
# t = Type.objects.get(pk=3)
# t.delete()

# contains funciona como un like, icontains funciona de forma similar solo
# que no toma en cuenta si está en mayuscula o minuscula
# obj = Type.objects.filter(name__icontains='pre')

# las que empiezan con
# obj = Type.objects.filter(name__startswith='P')

# las que terminan con
# obj = Type.objects.filter(name__endswith='a')


# se crea un vector solicitando esos datos exactos a la bd
# obj = Type.objects.filter(name__in=['viba', 'hola'])

# .count() permite devolver la cantidad de los elementos
# obj = Type.objects.filter(name__in=['viba', 'hola']).count()


# .query devuelve la consulta SQL que está realizando el comando
# obj = Type.objects.filter(name__icontains='pre').query


# si se quiere excluir un elemento exacto se debe colocar .exclude()
# obj = Type.objects.filter(name__endswith='a').exclude(id = 5)

# si se quiere iterar los valores se debe utilizar un for
# for i in Type.objects.filter(name__endswith='a'):
#     print(i.name)


# Ejemplo con tablas relacionadas
obj = Employee.objects.filter(type_id = 1) # de esta manera se realizaría la consulta
# del empleado con respecto al tipo
