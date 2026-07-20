# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

My recommendation system will be much more simple when compared to real world systems utilized by programs such as Spotify or Youtube that find patterns in what users skip,save and listen to combined with genre and the context of the song. Using the users stated musical preferences, songs will be judged by energy, valence and acoustics so that the reccomendations can remain accurate but also simple

Recipe:

Genre match: +2.0 points
Mood match: +1.0 point
Energy similarity: add a value based on how close the song’s energy is to the user’s target

Energy Formula: similarity = 1 - |Eneregy(song) - Energy(target)|
total: S = 2.0 x genre_match + 1.0 x mood_match = similarity

Genre is the strongest signal so it has higher weight compared to mood but energy exists to break ties between similar songs.

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Loaded songs: 18

Top recommendations:

1. Sunrise City
   Score: 3.98
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

2. Gym Hero
   Score: 2.87
   Reasons: genre match (+2.0), mood mismatch, energy similarity (+0.87)

3. Rooftop Lights
   Score: 1.96
   Reasons: genre mismatch, mood match (+1.0), energy similarity (+0.96)

4. Night Drive Loop
   Score: 0.95
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.95)

5. Neon Skyline
   Score: 0.92
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.92)
   **Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

Loading songs from data/songs.csv...
=== Balanced ===

1. Sunrise City
   Score: 3.88
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.88)
2. Gym Hero
   Score: 2.77
   Reasons: genre match (+2.0), mood mismatch, energy similarity (+0.77)
3. Rooftop Lights
   Score: 1.94
   Reasons: genre mismatch, mood match (+1.0), energy similarity (+0.94)
4. Golden Harbor
   Score: 0.98
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.98)
5. Midnight Riviera
   Score: 0.98
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.98)

=== Conflicting ===

1. Gym Hero
   Score: 2.97
   Reasons: genre match (+2.0), mood mismatch, energy similarity (+0.97)
2. Sunrise City
   Score: 2.92
   Reasons: genre match (+2.0), mood mismatch, energy similarity (+0.92)
3. Storm Runner
   Score: 0.99
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.99)
4. Neon Skyline
   Score: 0.98
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.98)
5. Fire in the Distance
   Score: 0.95
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.95)

=== Sparse-match ===

1. Coffee Shop Stories
   Score: 2.83
   Reasons: genre match (+2.0), mood mismatch, energy similarity (+0.83)
2. Neon Skyline
   Score: 1.32
   Reasons: genre mismatch, mood match (+1.0), energy similarity (+0.32)
3. Spacewalk Thoughts
   Score: 0.92
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.92)
4. Velvet Snowfall
   Score: 0.89
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.89)
5. Library Rain
   Score: 0.85
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.85)

=== Neutral ===

1. Moonlit Echoes
   Score: 0.94
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.94)
2. Midnight Coding
   Score: 0.92
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.92)
3. Backroad Signals
   Score: 0.91
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.91)
4. Focus Flow
   Score: 0.90
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.90)
5. Coffee Shop Stories
   Score: 0.87
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.87)

=== Acoustic-heavy ===

1. Focus Flow
   Score: 1.00
   Reasons: genre mismatch, mood mismatch, energy similarity (+1.00)
2. Midnight Coding
   Score: 0.98
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.98)
3. Coffee Shop Stories
   Score: 0.97
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.97)
4. Moonlit Echoes
   Score: 0.96
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.96)
5. Quiet Cathedral
   Score: 0.96
   Reasons: genre mismatch, mood mismatch, energy similarity (+0.96)

---

## Experiments You Tried

I tested the recommender with several user profiles to see whether the scoring logic was stable and easy to explain.

- Baseline profile: pop, happy, target energy 0.7
- Adversarial profile: pop, sad, target energy 0.9 to check whether a conflicting mood and energy preference could produce strange recommendations
- Sparse-match profile: jazz, energetic, target energy 0.2 to see how the model behaves when few songs strongly match the user
- Neutral profile: empty genre and mood with a moderate energy target to test fallback behavior
- Acoustic-heavy profile: indie, calm, target energy 0.4 to see whether similar songs are separated in a sensible way

These tests helped reveal that the system can produce confident scores even when the user profile is internally inconsistent, which makes the evaluation of edge cases especially important.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Building this recommender system taught me that creating real recommendations uses an algorithm is a lot more difficult than it seems. Today, we have many apps and websites that use algorithms to reccomend and suggest content it's user migth want to see. However, we dont think much about how difficult it is to design these softwares. I understand why real programs rely on diversity and bias mitigation. Using the VS code copilot to help explain these concepts helped greatly, being able to point out flaws and underlying issues that might not be visible. 