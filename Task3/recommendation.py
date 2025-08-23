import numpy as np

movies = {
    # Hollywood Movies
    "THE MATRIX":            [1, 1, 0, 0, 0, 0, 0, 0],
    "JOHN WICK":             [1, 0, 1, 0, 0, 0, 0, 0],
    "INTERSTELLAR":          [0, 1, 0, 1, 0, 0, 0, 0],
    "INCEPTION":             [0, 1, 1, 0, 0, 0, 0, 0],

    # DC Movies
    "THE DARK KNIGHT":       [1, 0, 0, 1, 1, 0, 0, 0],
    "MAN OF STEEL":          [1, 1, 0, 0, 0, 0, 0, 0],
    "BATMAN V SUPERMAN":     [1, 1, 0, 0, 0, 0, 0, 0],
    "JUSTICE LEAGUE":        [1, 1, 0, 0, 0, 1, 0, 0],
    "AQUAMAN":               [1, 1, 0, 0, 0, 1, 0, 0],

    # Marvel Movies
    "AVENGERS ENDGAME":     [1, 1, 0, 0, 0, 1, 0, 0],
    "AVENGERS INFINITY WAR":[1, 1, 0, 0, 0, 1, 0, 0],
    "IRON MAN":              [1, 1, 0, 0, 0, 1, 0, 0],
    "CAPTAIN AMERICA CIVIL WAR": [1, 1, 0, 0, 0, 1, 0, 0],
    "DOCTOR STRANGE":        [1, 0, 0, 0, 0, 0, 1, 0],
    "BLACK PANTHER":         [1, 1, 0, 0, 0, 1, 0, 0],
    "THOR: RAGNAROK":        [1, 1, 1, 0, 0, 1, 0, 0],
    "GUARDIANS OF THE GALAXY":[1, 1, 0, 0, 0, 1, 0, 0],

    # Anime Movies
    "YOUR NAME":             [0, 1, 0, 1, 0, 0, 0, 1],
    "SPIRITED AWAY":         [0, 1, 0, 1, 0, 0, 0, 1],
    "DEMON SLAYER: MUGEN TRAIN": [1, 1, 1, 0, 0, 0, 0, 1],
    "NARUTO THE LAST":       [1, 1, 0, 1, 0, 0, 0, 1],

    # Anime Series
    "NARUTO SHIPPUDEN":      [1, 1, 1, 0, 0, 0, 0, 1],
    "ATTACK ON TITAN":       [1, 1, 1, 1, 0, 0, 0, 1],
    "DEATH NOTE":            [0, 0, 1, 1, 0, 0, 0, 1],
    "ONE PIECE":             [1, 1, 0, 0, 0, 1, 0, 1],
    "DRAGON BALL Z":         [1, 1, 0, 0, 0, 1, 0, 1],
    "JUJUTSU KAISEN":        [1, 1, 1, 0, 0, 0, 0, 1],
 
    # TV/Web Series
    "DARK":                  [0, 1, 1, 1, 0, 0, 0, 1],
    "GAME OF THRONES":       [1, 1, 1, 1, 0, 0, 0, 0],
    "BREAKING BAD":          [1, 0, 1, 1, 0, 0, 0, 0],
    "STRANGER THINGS":       [1, 1, 1, 0, 0, 0, 0, 1],
    "MONEY HEIST":           [1, 0, 1, 1, 1, 0, 0, 0],
    "PEAKY BLINDERS":        [1, 0, 1, 1, 1, 0, 0, 0]
}

movie_names = list(movies.keys())
movie_vectors = np.array(list(movies.values()))

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot / (norm1 * norm2)

def recommend(movie_name, top_n=5):
    movie_name = movie_name.upper()
    if movie_name not in movie_names:
        print("\nMOVIE/SERIES NOT FOUND IN OUR LIST. TRY ANOTHER ONE!")
        return

    idx = movie_names.index(movie_name)
    target_vector = movie_vectors[idx]

    similarities = []
    for i, vec in enumerate(movie_vectors):
        if i != idx:
            sim = cosine_similarity(target_vector, vec)
            similarities.append((movie_names[i], sim))

    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

    print(f"\nBECAUSE YOU LIKED '{movie_name}', YOU MIGHT ALSO ENJOY:")
    for movie, score in similarities[:top_n]:
        print(f" - {movie}")

print("HERE ARE THE OPTIONS (MOVIES + ANIME + SERIES):\n")
for name in movie_names:
    print("-", name)

choice = input("\nWHICH ONE DO YOU LIKE? TYPE THE EXACT NAME: ")
recommend(choice)
