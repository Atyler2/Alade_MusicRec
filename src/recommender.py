from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    from pathlib import Path

    print(f"Loading songs from {csv_path}...")

    path = Path(csv_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parent.parent / path

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        songs = []
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    genre_pref = user_prefs.get(
        "genre") or user_prefs.get("favorite_genre", "")
    mood_pref = user_prefs.get("mood") or user_prefs.get("favorite_mood", "")
    target_energy = user_prefs.get("energy")
    if target_energy is None:
        target_energy = user_prefs.get("target_energy", 0.0)

    genre_weight = 1.0
    mood_weight = 1.0
    energy_weight = 2.0

    genre_match = 1.0 if song.get("genre") == genre_pref else 0.0
    mood_match = 1.0 if song.get("mood") == mood_pref else 0.0
    energy_similarity = max(
        0.0, 1.0 - abs(float(song.get("energy", 0.0)) - float(target_energy)))

    score = (genre_weight * genre_match) + (mood_weight * mood_match) + (
        energy_weight * energy_similarity)

    reasons: List[str] = []
    if genre_match:
        reasons.append(f"genre match (+{genre_weight:.1f})")
    else:
        reasons.append("genre mismatch")

    if mood_match:
        reasons.append(f"mood match (+{mood_weight:.1f})")
    else:
        reasons.append("mood mismatch")

    reasons.append(
        f"energy similarity (+{energy_weight * energy_similarity:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    return sorted(scored_songs, key=lambda item: item[1], reverse=True)[:k]
