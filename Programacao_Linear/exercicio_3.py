# instalação e importação do pacote mip
from mip import *
from funcs import solve

# composição de cada ingrediente
a = {
    'l': {'c': 0.005, 's': 0.14},
    'g': {'c': 0.9,   's': 0.0},
    's': {'c': 0.09,  's': 0.27},
}

# custo
c = {'l': 90, 'g': 180, 's': 25} # (l = lingotes, g = grafites e s = sucata)

# composições mínimas e máximas dos componentes
n = {'c': 0.0, 's': 0.19}  # min (c = carbono e s = silicio)
m = {'c': 0.095, 's': 0.2} # max

# quantidade desejada da liga em toneladas
Q = 10

# implementa modelo
modelo = Model(sense=MINIMIZE, solver_name=CBC)

# Criação da variável liga 1: x_0 = lingotes / x_1 = grafite / x_2 = sucata / liga 2: x_3 = lingote / x_4 = grafite/ x_4 = sucata
x = [modelo.add_var(var_type=CONTINUOUS, name=f"x_{i}", lb=0.0) for i in range(6)] 

# Função objetivo = minimizar custo total
modelo.objective = 90*x[0] + 180*x[1] + 25*x[2]

# Restrição: quantidade minína de carbono liga 1
modelo += 0.005*x[0] + 0.9*x[1] + 0.09*x[2] >= 0 

# Restrição: quantidade máxima de carbono liga 1
modelo += 0.005*x[0] + 0.9*x[1] + 0.09*x[2] <= 0.95

# Restrição: quantidade minína de silicio liga 1
modelo += 0.14*x[0] + 0*x[1] + 0.27*x[2] >= 1.9

# Restrição: quantidade máxima de silicio liga 1
modelo += 0.14*x[0] + 0*x[1] + 0.27*x[2] <= 2

# Restrição: quantidade máxima em toneladas de cada ingrediente na liga 1
modelo += x[0] + x[1] + x[2] == 10

modelo += x[0] <= 5

modelo += x[1] <= 5

modelo += x[2] <= 12

# Restrição: quantidade minína de carbono liga 2
modelo += 0.005*x[3] + 0.9*x[4] + 0.09*x[5] >= 0 

# Restrição: quantidade máxima de carbono liga 2
modelo += 0.005*x[3] + 0.9*x[4] + 0.09*x[5] <= 4

# Restrição: quantidade minína de silicio liga 2
modelo += 0.14*x[3] + 0*x[4] + 0.27*x[5] >= 1.2

# Restrição: quantidade máxima de silicio liga 2
modelo += 0.14*x[3] + 0*x[4] + 0.27*x[5] <= 1.9

# Restrição: quantidade máxima em toneladas de cada ingrediente na liga 2
modelo += x[3] + x[4] + x[5] == 6

modelo += x[3] <= 5

modelo += x[4] <= 5

modelo += x[5] <= 12

modelo.write("model.lp") # salva modelo em arquivo
with open("model.lp") as f: # lê e exibe conteúdo do arquivo
  print(f.read())
  
solve(modelo)
