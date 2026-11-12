# Estruturas Sequenciais
# Listas
leitura_sensores = [25.3, 60.5]
print(leitura_sensores) #Lendo toda a lista

print(leitura_sensores[0]) #Lendo o primeiro elemento da lista
print(leitura_sensores[1]) #Lendo o segundo elemento da lista
print(leitura_sensores[-1]) #Lendo o último elemento da lista
print(leitura_sensores[-2]) #Lendo o penúltimo elemento da lista
leitura_sensores.append(100.0) #Adicionando um elemento na lista
print(leitura_sensores)

# Tuplas - não tem capacidade de alterar o que você já armazenou
coordenadas_gps = (25.3, 60.5)
print(coordenadas_gps) #Lendo toda a tupla

# 1. Criação e inicialização de uma lista para armazenar leituras de temperatura.
temperaturas = [25.1, 23.3, 26.4]
print(f"Leituras iniciais de temperatura: {temperaturas}")

temperaturas.append(99.1) #adicionando novas temperaturas
print(f"Leituras após a adição: {temperaturas}")


primeira_leitura = temperaturas[0]
ultima_leitura = temperaturas[-1]  # Acessando o último elemento
print(f"Primeira leitura registrada: {primeira_leitura}°C")
print(f"Última leitura registrada: {ultima_leitura}°C")

# Modificando uma leitura
# Modificar dados em tempo real é importante para controle de processos e correção de erros.
temperaturas[2] = 25.0  # Supondo que a terceira leitura (índice 2) foi corrigida
print(f"Leituras após correção: {temperaturas}")

#  Verificando o tamanho da lista
# Conhecer o tamanho da lista ajuda no gerenciamento de recursos e na lógica de controle.

print(f"Número total de leituras registradas: {len(temperaturas)}")

# Removendo uma leitura
# Em sistemas com memória limitada, gerenciar o tamanho das listas é vital.

temperaturas.pop(0)  # Remove o primeiro elemento (leitura mais antiga)
print(f"Leituras após remover a mais antiga: {temperaturas}")

# Verificando a existência de um valor
# A busca por elementos é comum para verificar estados ou condições.
if 26.2 in temperaturas:
    print("A temperatura de 26.2°C foi registrada.")

# Ordenando as leituras
# Ordenar dados é útil para identificar valores mínimos, máximos ou tendências.

temperaturas.sort()
print(f"Leituras ordenadas: {temperaturas}")
