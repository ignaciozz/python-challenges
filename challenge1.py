acuracias = [0.82, 0.79, 0.91]

print(f"Primeira acurácia: {acuracias[0]}")
print(f"Última acurácia: {acuracias[-1]}")
print(f"Total de acurácias: {len(acuracias)}")

avg = (acuracias[0] + acuracias[1] + acuracias[2]) / len(acuracias)
print(f"Média: {avg}")
