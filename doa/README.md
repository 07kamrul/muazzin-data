Offline Dua asset folder

Purpose:
Store full dua snapshots per category so the app can fall back to bundled
assets when remote dua sources are unavailable.

Supported file names:
- `assets/doa/collections/akhirah.json`
- `assets/doa/collections/distress_relief.json`
- `assets/doa/collections/family_parents.json`
- `assets/doa/collections/forgiveness_repentance.json`
- `assets/doa/collections/general.json`
- `assets/doa/collections/guidance_faith.json`
- `assets/doa/collections/health.json`
- `assets/doa/collections/heart_inner_state.json`
- `assets/doa/collections/morning_evening.json`
- `assets/doa/collections/protection.json`
- `assets/doa/collections/rizq_finance.json`
- `assets/doa/collections/study_success.json`

Supported file format:
Either a top-level list of dua items or an object with a `duas` array.

Example:
```json
{
  "collection": "study_success",
  "collection_name": "Study & Success",
  "duas": [
    {
      "number": 1,
      "title": "Increase Me in Knowledge",
      "arabic": "رَبِّ زِدْنِي عِلْمًا",
      "english": "My Lord, increase me in knowledge.",
      "bangla": "হে আমার রব, আমার জ্ঞান বৃদ্ধি করুন।"
    }
  ]
}
```

Notes:
- Duplicate duas across the provided sources were merged by normalized Arabic text.
- Some source pages only exposed transliteration or partial formatting, so the Arabic text was normalized to standard wording before storage.
- Some Bangla translations were lightly normalized for consistency across files.
- The provided Google Play listing did not expose scrapeable dua text, so it is recorded in `index.json` but does not contribute unique dua entries.
- `doas.json` is the full fallback dataset, similar to `hadith/hadiths.json`.
