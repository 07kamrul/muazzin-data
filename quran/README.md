Offline Quran asset folder

Purpose:
Store a full local Quran snapshot so the app can fall back to bundled assets
when the remote Quran API is unavailable.

Required files:
- `assets/quran/surah_list.json`
- `assets/quran/surahs/1.json` through `assets/quran/surahs/114.json`

Expected `surah_list.json` format:
```json
[
  {
    "number": 1,
    "name_arabic": "الفاتحة",
    "name_bangla": "আল-ফাতিহা",
    "name_english": "Al-Faatiha",
    "name_meaning": "The Opening",
    "ayah_count": 7,
    "juz_start": 1,
    "revelation_type": "meccan"
  }
]
```

Expected `surahs/<n>.json` format:
```json
{
  "surah": {
    "number": 1,
    "name_arabic": "الفاتحة",
    "name_bangla": "আল-ফাতিহা",
    "name_english": "Al-Faatiha",
    "name_meaning": "The Opening",
    "ayah_count": 7,
    "juz_start": 1,
    "revelation_type": "meccan"
  },
  "ayahs": [
    {
      "surah_number": 1,
      "ayah_number": 1,
      "arabic_text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
      "bangla_translation": "শুরু করছি আল্লাহর নামে...",
      "english_translation": "In the name of Allah...",
      "juz_number": 1,
      "page_number": 1
    }
  ]
}
```

How the app uses this:
- It tries the API first.
- If the API fails, it loads from these asset files.
