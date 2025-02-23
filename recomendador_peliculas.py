import random

def recomendar_pelicula():
    # Diccionario que almacena listas de películas por género
    peliculas = {
        "acción": ["Mad Max: Fury Road", "John Wick", "Gladiador", "Misión Imposible", "The Dark Knight"],
        "comedia": ["Superbad", "Dumb and Dumber", "Step Brothers", "The Hangover", "Ace Ventura"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "The Green Mile", "Fight Club", "Titanic"],
        "terror": ["The Conjuring", "A Nightmare on Elm Street", "It", "Halloween", "The Exorcist"],
        "ciencia ficción": ["Interstellar", "Inception", "Blade Runner 2049", "The Matrix", "Star Wars"],
        "animación": ["Toy Story", "Shrek", "Finding Nemo", "The Lion King", "Spider-Man: Into the Spider-Verse"]
    }

    print("🎬 Bienvenido al agente de recomendación de películas")
    print("Géneros disponibles: acción, comedia, drama, terror, ciencia ficción, animación")

    # Solicita al usuario el género favorito
    genero = input("¿Cuál es tu género favorito? ").strip().lower()

    # Verifica si el género ingresado está en el diccionario
    if genero in peliculas:
        # Selecciona una película aleatoria del género elegido
        pelicula_recomendada = random.choice(peliculas[genero])
        print(f"🎥 Te recomendamos ver: {pelicula_recomendada}")
    else:
        # Si el género no es válido, muestra un mensaje de error
        print("❌ Género no encontrado. Intenta de nuevo con una opción válida.")

if __name__ == "__main__":
    recomendar_pelicula()
