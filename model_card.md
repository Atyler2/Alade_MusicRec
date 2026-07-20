# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

MusicRec 1.0

---

## 2. Intended Use

## The recommenders scores songs by checking three features, genre, mood and energy. It combines these three features into one score using weight-genre and mood that are woth one point if they match. Energy is worth up to 2 points depending on how close the song's energy is to yours. It then gives you the top 5 songs.

## 3. How the Model Works

The program uses a three step scoring system, checking if the grenre matches and giving one point if it dows. Then, if the mood matches it gets another point and songs with energy levels close to the users get 2 points.

---

## 4. Data

The dataset contains 18 songs across a diverse range of genres and moods.

**Genres represented:** pop, lofi, rock, ambient, jazz, synthwave, indie pop, reggae, classical, house, country, folk, metal, reggaeton, gospel

**Moods represented:** happy, chill, intense, relaxed, moody, focused, carefree, nostalgic, energetic, melancholy, dreamy, triumphant, romantic, serene

**Energy levels:** Range from 0.28 (low energy, calm songs like _Spacewalk Thoughts_) to 0.95 (high energy, intense songs like _Fire in the Distance_)

**Data changes:** No modifications were made to the original dataset; it was used as provided.

---

## 5. Strengths

- The system works well for users with clear, straightforward preferences.

- The energy similarity metric is works as a stable fallback.

- Every recommendation includes a clear breakdown (genre match, mood match, energy similarity score) that lets users understand why a song was recommended.

---

## 6. Limitations and Bias

- The logic favors users with single label tastes, users who like multiple genres are less likely to get good recommendations.
- It can underrepresent users that have preferences that conflict with each other.
- The recommender can repeatedly surface the same kind of songs, relying on a small set of features.

---

## 7. Evaluation

I tested five user profiles to observe how the scoring logic behaves under different preference conditions:

- **Balanced profile**: genre = pop, mood = happy, target energy = 0.7. Baseline case.
- **Conflicting profile**: genre = pop, mood = sad, target energy = 0.9. Adversarial case with internally contradictory preferences.
- **Sparse-match profile**: genre = jazz, mood = energetic, target energy = 0.2. Tests fallback behavior when genre matches are rare.
- **Neutral profile**: genre = "", mood = "", target energy = 0.5. Tests whether the system handles incomplete profiles.
- **Acoustic-heavy profile**: genre = indie, mood = calm, target energy = 0.4. Tests stability when preferences are offset from the default.

### Profile Comparisons

**Balanced vs. Conflicting:** Both want pop genre, but differ in mood and energy. Balanced got _Sunrise City_ (genre match + mood match) at the top. Conflicting got _Gym Hero_ (genre match + high energy match at 0.97) at the top instead. This makes sense because energy is weighted heavily (2.0), so even though Conflicting has the emotionally contradictory "sad + high energy" profile, the high energy target (0.9) pulls high-energy songs to the top regardless of mood.

**Balanced vs. Sparse-match:** Balanced prefers pop (abundant in catalog) and got immediate genre matches. Sparse-match prefers jazz (only a few songs) and got _Coffee Shop Stories_ first due to genre match, but then the next recommendations (_Spacewalk Thoughts_, _Velvet Snowfall_) are energy-based fallbacks because there are few jazz+energetic songs. This shows the system does rely on genre matches when available but degrades gracefully to energy similarity when genre is scarce.

**Conflicting vs. Neutral:** Conflicting has strong opposing signals (sad mood but high energy) and still got confident top recommendations due to the high energy weight. Neutral has no genre or mood, so all recommendations are based purely on energy similarity around the 0.5 target. Neutral's results (_Moonlit Echoes_, _Midnight Coding_) are all within ±0.1 energy of 0.5, showing the system is perfectly stable without explicit genre/mood signals—it just becomes an energy filter.

**Sparse-match vs. Acoustic-heavy:** Both are off-genre profiles, but differ in energy targets. Sparse-match (energy = 0.2) got low-energy songs like _Library Rain_ (energy similarity +1.70). Acoustic-heavy (energy = 0.4) got _Focus Flow_ (energy similarity +2.00 because energy = 1.0 - |0.4 - 0.4|). This is correct: the energy gap drives the ranking when genre is not a strong match.

### What Surprised Me

The system produced stable, sensible output even for the Conflicting profile, which was designed to be contradictory. This is actually concerning—the recommender can look confident and justified (genre match, high energy match) even though it is recommending upbeat, energetic sad music, which may not reflect the user's true intent. The formula does not know that "sad" and "energetic 0.9" may be in conflict; it just scores them independently. That is a reminder that a simple, interpretable formula can mask deeper biases or failures to understand user intent.

---

## 8. Future Work
- allow users to list preferences or confidence scores.
- Use additional song features
- Expanding the song catalog

---

## 9. Personal Reflection
Recommender systems are extremely complecated, making trade offs between accuracy and simplicity for the best recommendations. A formula like mine works well but misses the users intent instead ranking sonds by independent features. Real world reccomender systems probably increase the amount of features and factors to determine a more accurate ranking.


---
