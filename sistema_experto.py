def diagnostico():
    print("🩺 Bienvenido al sistema experto de diagnóstico médico")
    print("Responde con 'sí' o 'no' a las siguientes preguntas.")

    fiebre = input("¿Tienes fiebre? (sí/no): ").strip().lower()
    tos = input("¿Tienes tos? (sí/no): ").strip().lower()
    dolor_garganta = input("¿Tienes dolor de garganta? (sí/no): ").strip().lower()
    dolor_cabeza = input("¿Tienes dolor de cabeza? (sí/no): ").strip().lower()
    cansancio = input("¿Te sientes muy cansado? (sí/no): ").strip().lower()

    if fiebre == "sí" and tos == "sí" and dolor_garganta == "sí":
        print("📋 Posible diagnóstico: Gripe o resfriado común.")
    elif fiebre == "sí" and cansancio == "sí" and dolor_cabeza == "sí":
        print("📋 Posible diagnóstico: Infección viral o COVID-19. Consulta a un médico.")
    elif fiebre == "no" and tos == "sí" and dolor_garganta == "sí":
        print("📋 Posible diagnóstico: Faringitis.")
    elif fiebre == "sí" and dolor_cabeza == "sí" and cansancio == "sí":
        print("📋 Posible diagnóstico: Posible dengue. Consulta a un médico.")
    else:
        print("⚠️ No se pudo determinar un diagnóstico claro. Consulta a un médico.")

if __name__ == "__main__":
    diagnostico()
