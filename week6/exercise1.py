songs = []
genre_count = {}

Music_library = []
print("\nWelcome to Music Library Manager")

for i in range(5):
    song_name = input(f"Enter song {i + 1} name: ")
    genre = input("Enter genre: ")
    songs.append((song_name, genre))
    genre_count[genre] = genre_count.get(genre, 0) + 1

print("\n=== YOUR MUSIC LIBRARY ===")
for index, (song, genre) in enumerate(songs, start=1):
    print(f"{index}. {song} ({genre})")

print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} songs")

most_popular = max(genre_count, key=genre_count.get)
print(f"Most popular genre: {most_popular}")
