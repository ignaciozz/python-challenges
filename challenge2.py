acuracias = [0.82, 0.79, 0.91, 0.85, 0.88]

avg = sum(acuracias) / len(acuracias)
print(f"Média: {avg * 100}%")

print(f"Melhor acurácia: {max(acuracias) * 100}%")
print(f"Pior acurácia: {min(acuracias) * 100}%")

rodada = 1

for a in acuracias:
    print(f"Rodada {rodada}: {(a * 100)}%")
    if a >= avg:
        print("✅")
    else:
        print("❌")
   
    rodada = rodada + 1