# Programa en Python3 para evaluar una determinada
# expresión de una operación que el usuario
# ingrese

# Función para encontrar precedencia
# de operadores.
def precedence(op):
	
	if op == '+' or op == '-':
		return 1
	if op == '*' or op == '/':
		return 2
	return 0

# Función para realizar aritmética
# de operaciones
def applyOp(a, b, op):
	
	if op == '+': return a + b
	if op == '-': return a - b
	if op == '*': return a * b
	if op == '/': return a / b

# Función que devuelve el valor de
# la expresión después de la evaluación.
def evaluate(tokens):
	
	# Pila para almacenar los valores enteros.
	values = []
	
	# Pila para almacenar los operadores.
	ops = []
	i = 0
	
	while i < len(tokens):
		
		# El token actual es un espacio en blanco,
		# Saltarlo.
		if tokens[i] == ' ':
			i += 1
			continue
		
		# El token actual es una apertura
		# brace, empújelo a 'ops'
		elif tokens[i] == '(':
			ops.append(tokens[i])
		
		# El token actual es un número, presione
		# para apilar números.
		elif tokens[i].isdigit():
			val = 0
			
			# Puede haber más de un
			# dígito en el número.
			while (i < len(tokens) and
				tokens[i].isdigit()):
			
				val = (val * 10) + int(tokens[i])
				i += 1
			
			values.append(val)
			
			# ahora mismo la i apunta a
			# el carácter al lado del dígito,
			# ya que el bucle for también aumenta
			# la yo, omitiríamos una
			# posición del token; Necesitamos que
			# disminuir el valor de i en 1 para
			# corregir el desplazamiento.
			i-=1
		
		# Abrazadera de cierre encontrada,
		# resuelve el corsé completo.
		elif tokens[i] == ')':
		
			while len(ops) != 0 and ops[-1] != '(':
			
				val2 = values.pop()
				val1 = values.pop()
				op = ops.pop()
				
				values.append(applyOp(val1, val2, op))
			
			# corsé de apertura pop.
			ops.pop()
		
		# El token actual es un operador.
		else:
		
			# Mientras que la parte superior de 'operaciones' tiene la misma o
			# mayor precedencia a la actual
			# token, que es un operador.
			# Aplicar operador encima de 'operaciones'
			# para encabezar dos elementos en la pila de valores.
			while (len(ops) != 0 and
				precedence(ops[-1]) >=
				precedence(tokens[i])):
						
				val2 = values.pop()
				val1 = values.pop()
				op = ops.pop()
				
				values.append(applyOp(val1, val2, op))
			
			# Empuje el token actual a 'operaciones'.
			ops.append(tokens[i])
		
		i += 1
	
	# Se ha analizado toda la expresión
	# en este punto, aplique las operaciones restantes
	# a los valores restantes.
	while len(ops) != 0:
		
		val2 = values.pop()
		val1 = values.pop()
		op = ops.pop()
				
		values.append(applyOp(val1, val2, op))
	
	# La parte superior de los 'valores' contiene el resultado,
	# devolverlo.
	return values[-1]

# Código del conductor
if __name__ == "__main__":
	op=input("Ingrese la operación a resolver: ")
	print(evaluate(op))
