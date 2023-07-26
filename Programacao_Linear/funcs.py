# Funcao responsável por rodar biblioteca que vai resolver o sistema
import mip

def solve(model):
    status = model.optimize()

    print("Status = ", status)
    print(f"Solution value  = {model.objective_value:.2f}\n")
    
    print("Solution:")
    for v in model.vars:
        print(f"{v.name} = {v.x:.2f}")

