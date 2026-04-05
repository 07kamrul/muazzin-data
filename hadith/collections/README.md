Offline Hadith asset folder

Purpose:
Store full Hadith snapshots per collection so the app can fall back to bundled
assets when the remote Hadith API is unavailable.

Supported file names:
- `assets/hadith/collections/bukhari.json`
- `assets/hadith/collections/muslim.json`
- `assets/hadith/collections/abu-dawud.json`
- `assets/hadith/collections/tirmidhi.json`
- `assets/hadith/collections/ibn-majah.json`

Supported file format:
Either a top-level list of hadith items or an object with a `hadiths` array.

Example:
```json
{
  "hadiths": [
    {
      "number": 1,
      "arab": "إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ",
      "text": "নিশ্চয়ই কাজের ফল নিয়তের উপর নির্ভরশীল।"
    }
  ]
}
```

How the app uses this:
- It tries the remote Hadith API first.
- If that fails, it tries these per-collection asset files.
- If those are missing too, it falls back to the existing
  `assets/hadith/hadiths.json`.
