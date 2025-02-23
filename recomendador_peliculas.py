import random

def recomendar_pelicula():
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

    genero = input("¿Cuál es tu género favorito? ").strip().lower()

    if genero in peliculas:
        pelicula_recomendada = random.choice(peliculas[genero])
        print(f"🎥 Te recomendamos ver: {pelicula_recomendada}")
    else:
        print("❌ Género no encontrado. Intenta de nuevo con una opción válida.")

if __name__ == "__main__":
    recomendar_pelicula()
