from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOA_DIR = ROOT / "doa"
COLLECTIONS_DIR = DOA_DIR / "collections"


SOURCES = {
    "muslimaid": "https://www.muslimaid.org/media-centre/blog/students-here-are-duas-for-studying/",
    "islamic_relief_canada": "https://www.islamicreliefcanada.org/resources/duas-and-dhikr",
    "mwa": "https://mwa.org.au/latest-articles/duas-for-distress-allahs-help-in-challenging-times/",
    "duas_org": "https://www.duas.org/mobile/dua-short-powerful.html",
    "kalbela": "https://www.kalbela.com/religion/92473",
    "dhakamail": "https://dhakamail.com/religion/54289",
    "teachers_gov_bd": "https://www.teachers.gov.bd/blog/details/742208",
    "play_store": "https://play.google.com/store/apps/details?id=com.muslim.hundred.small.dhoya&hl=bn",
    "celestialshiny": "https://celestialshiny.com/100-duas-from-quran-and-sunnah-for-success-and-happiness/",
}


def normalize_arabic(text: str) -> str:
    text = re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED]", "", text)
    text = re.sub(r"[^\u0600-\u06FF]+", "", text)
    return text


def entry(
    *,
    slug: str,
    title: str,
    arabic: str,
    transliteration: str,
    english: str,
    bangla: str,
    categories: list[str],
    source_keys: list[str],
    notes: str | None = None,
) -> dict:
    return {
        "slug": slug,
        "title": title,
        "arabic": arabic,
        "transliteration": transliteration,
        "english": english,
        "bangla": bangla,
        "categories": categories,
        "source_urls": [SOURCES[key] for key in source_keys],
        **({"notes": notes} if notes else {}),
    }


RAW = [
    entry(
        slug="rabbana-atina-fid-dunya",
        title="Good in This World and the Hereafter",
        arabic="رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
        transliteration="Rabbana atina fid-dunya hasanah wa fil-akhirati hasanah wa qina 'adhaban-nar.",
        english="Our Lord, give us good in this world and good in the Hereafter, and protect us from the punishment of the Fire.",
        bangla="হে আমাদের রব, আমাদেরকে দুনিয়ায় কল্যাণ দান করুন, আখিরাতেও কল্যাণ দান করুন এবং আমাদেরকে জাহান্নামের শাস্তি থেকে রক্ষা করুন।",
        categories=["general", "akhirah"],
        source_keys=["dhakamail", "kalbela", "celestialshiny"],
    ),
    entry(
        slug="allahumma-inni-asaluka-al-jannah",
        title="Ask for Paradise and Protection from Hell",
        arabic="اللَّهُمَّ إِنِّي أَسْأَلُكَ الْجَنَّةَ وَأَعُوذُ بِكَ مِنَ النَّارِ",
        transliteration="Allahumma inni as'alukal-jannah wa a'udhu bika minan-nar.",
        english="O Allah, I ask You for Paradise and seek refuge in You from the Fire.",
        bangla="হে আল্লাহ, আমি আপনার কাছে জান্নাত প্রার্থনা করছি এবং জাহান্নামের আগুন থেকে আপনার আশ্রয় চাইছি।",
        categories=["general", "akhirah"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="dua-yunus",
        title="Dua of Yunus",
        arabic="لَا إِلَٰهَ إِلَّا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ",
        transliteration="La ilaha illa anta subhanaka inni kuntu minaz-zalimin.",
        english="There is no god except You. Glory be to You. Indeed, I have been among the wrongdoers.",
        bangla="আপনি ছাড়া কোনো সত্য উপাস্য নেই। আপনি পবিত্র-মহিমান্বিত। নিশ্চয়ই আমি জালিমদের অন্তর্ভুক্ত ছিলাম।",
        categories=["distress_relief", "forgiveness_repentance"],
        source_keys=["dhakamail", "kalbela", "duas_org", "celestialshiny"],
    ),
    entry(
        slug="astaghfirullah-alladhi-la-ilaha-illa-huwa",
        title="Dua of Repentance",
        arabic="أَسْتَغْفِرُ اللَّهَ الَّذِي لَا إِلَهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ وَأَتُوبُ إِلَيْهِ",
        transliteration="Astaghfirullaha alladhi la ilaha illa huwa al-hayyul-qayyumu wa atubu ilayh.",
        english="I seek forgiveness from Allah, besides whom there is no god, the Ever-Living, the Sustainer, and I repent to Him.",
        bangla="আমি আল্লাহর কাছে ক্ষমা চাই, যিনি ছাড়া কোনো সত্য উপাস্য নেই, যিনি চিরঞ্জীব ও সবকিছুর ধারক; আর আমি তাঁর কাছেই তাওবা করছি।",
        categories=["forgiveness_repentance"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="allahummakfini-bihalalika",
        title="Freedom from Debt and Need",
        arabic="اللَّهُمَّ اكْفِنِي بِحَلَالِكَ عَنْ حَرَامِكَ وَأَغْنِنِي بِفَضْلِكَ عَمَّنْ سِوَاكَ",
        transliteration="Allahummakfini bihalalika 'an haramika wa aghnini bifadlika 'amman siwak.",
        english="O Allah, suffice me with what You made lawful instead of what You made unlawful, and enrich me by Your grace from dependence on anyone besides You.",
        bangla="হে আল্লাহ, আপনার হালাল দ্বারা আমাকে হারাম থেকে মুক্ত রাখুন এবং আপনার অনুগ্রহে আপনাকে ছাড়া অন্য কারও মুখাপেক্ষী না করেন।",
        categories=["rizq_finance", "distress_relief"],
        source_keys=["dhakamail", "kalbela", "teachers_gov_bd", "celestialshiny"],
    ),
    entry(
        slug="rabbana-hab-lana-min-azwajina",
        title="Righteous Spouse and Children",
        arabic="رَبَّنَا هَبْ لَنَا مِنْ أَزْوَاجِنَا وَذُرِّيَّاتِنَا قُرَّةَ أَعْيُنٍ وَاجْعَلْنَا لِلْمُتَّقِينَ إِمَامًا",
        transliteration="Rabbana hab lana min azwajina wa dhurriyyatina qurrata a'yunin waj'alna lil-muttaqina imama.",
        english="Our Lord, grant us from our spouses and children comfort to our eyes and make us leaders for the righteous.",
        bangla="হে আমাদের রব, আমাদের স্ত্রী-সন্তানদেরকে আমাদের চোখের শীতলতা বানিয়ে দিন এবং আমাদেরকে মুত্তাকিদের আদর্শ করুন।",
        categories=["family_parents"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="allahu-latifun-bi-ibadihi",
        title="For Increase in Provision",
        arabic="اللَّهُ لَطِيفٌ بِعِبَادِهِ يَرْزُقُ مَنْ يَشَاءُ وَهُوَ الْقَوِيُّ الْعَزِيزُ",
        transliteration="Allahu latifun bi'ibadihi yarzuqu man yasha'u wa huwa al-qawiyyul-'aziz.",
        english="Allah is Subtle with His servants. He provides for whom He wills, and He is the All-Strong, the Mighty.",
        bangla="আল্লাহ তাঁর বান্দাদের প্রতি অতি অনুগ্রহশীল। তিনি যাকে ইচ্ছা রিজিক দান করেন, আর তিনি সর্বশক্তিমান, পরাক্রমশালী।",
        categories=["rizq_finance"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="ya-hayyu-ya-qayyum",
        title="Seek Allah's Help in Hardship",
        arabic="يَا حَيُّ يَا قَيُّومُ بِرَحْمَتِكَ أَسْتَغِيثُ",
        transliteration="Ya Hayyu Ya Qayyumu birahmatika astaghith.",
        english="O Ever-Living, O Sustainer, I seek relief through Your mercy.",
        bangla="হে চিরঞ্জীব, হে সবকিছুর ধারক, আমি আপনার রহমতের মাধ্যমে সাহায্য প্রার্থনা করছি।",
        categories=["distress_relief", "morning_evening"],
        source_keys=["dhakamail", "kalbela", "celestialshiny"],
    ),
    entry(
        slug="allahumma-inni-asaluka-al-huda",
        title="For Guidance, Taqwa, Chastity and Sufficiency",
        arabic="اللَّهُمَّ إِنِّي أَسْأَلُكَ الْهُدَى وَالتُّقَى وَالْعَفَافَ وَالْغِنَى",
        transliteration="Allahumma inni as'alukal-huda wat-tuqa wal-'afafa wal-ghina.",
        english="O Allah, I ask You for guidance, piety, chastity and sufficiency.",
        bangla="হে আল্লাহ, আমি আপনার কাছে হেদায়াত, তাকওয়া, পবিত্রতা এবং অভাবমুক্তি প্রার্থনা করছি।",
        categories=["guidance_faith", "general"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="rabbi-zidni-ilma",
        title="Increase Me in Knowledge",
        arabic="رَبِّ زِدْنِي عِلْمًا",
        transliteration="Rabbi zidni 'ilma.",
        english="My Lord, increase me in knowledge.",
        bangla="হে আমার রব, আমার জ্ঞান বৃদ্ধি করুন।",
        categories=["study_success"],
        source_keys=["muslimaid", "dhakamail", "celestialshiny"],
    ),
    entry(
        slug="rabbi-yassir-wala-tuassir",
        title="Make It Easy and End It with Good",
        arabic="رَبِّ يَسِّرْ وَلَا تُعَسِّرْ وَتَمِّمْ بِالْخَيْرِ",
        transliteration="Rabbi yassir wa la tu'assir wa tammim bil-khayr.",
        english="My Lord, make it easy, do not make it difficult, and complete it with goodness.",
        bangla="হে আমার রব, সহজ করে দিন, কঠিন করবেন না, এবং কল্যাণের সঙ্গে তা পূর্ণতা দিন।",
        categories=["study_success", "distress_relief"],
        source_keys=["dhakamail"],
    ),
    entry(
        slug="allahumma-faqihni-fid-din",
        title="Grant Me Understanding of the Religion",
        arabic="اللَّهُمَّ فَقِّهْنِي فِي الدِّينِ",
        transliteration="Allahumma faqqihni fid-din.",
        english="O Allah, grant me understanding in the religion.",
        bangla="হে আল্লাহ, আমাকে দ্বীনের সঠিক জ্ঞান ও বোধ দান করুন।",
        categories=["study_success", "guidance_faith"],
        source_keys=["dhakamail"],
    ),
    entry(
        slug="rabbi-shrah-li-sadri",
        title="Confidence and Ease in Speech",
        arabic="رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي وَاحْلُلْ عُقْدَةً مِنْ لِسَانِي يَفْقَهُوا قَوْلِي",
        transliteration="Rabbi ishrah li sadri wa yassir li amri wahlul 'uqdatan min lisani yafqahu qawli.",
        english="My Lord, expand my chest for me, ease my task for me, and untie the knot from my tongue so they may understand my speech.",
        bangla="হে আমার রব, আমার বক্ষ প্রশস্ত করুন, আমার কাজ সহজ করুন, এবং আমার জিহ্বার জড়তা দূর করুন যাতে তারা আমার কথা বুঝতে পারে।",
        categories=["study_success", "guidance_faith"],
        source_keys=["muslimaid", "celestialshiny"],
    ),
    entry(
        slug="allahumma-anfani-bima-allamtani",
        title="Benefit Me with Useful Knowledge",
        arabic="اللَّهُمَّ انْفَعْنِي بِمَا عَلَّمْتَنِي وَعَلِّمْنِي مَا يَنْفَعُنِي",
        transliteration="Allahumma anfa'ni bima 'allamtani wa 'allimni ma yanfa'uni.",
        english="O Allah, benefit me through what You have taught me and teach me what benefits me.",
        bangla="হে আল্লাহ, আপনি আমাকে যা শিখিয়েছেন তা যেন আমার উপকারে আসে, আর আমাকে এমন জ্ঞান দিন যা উপকারী।",
        categories=["study_success"],
        source_keys=["muslimaid", "celestialshiny"],
    ),
    entry(
        slug="allahumma-la-sahla-illa-ma-jaltahu-sahla",
        title="Nothing Is Easy Except What You Make Easy",
        arabic="اللَّهُمَّ لَا سَهْلَ إِلَّا مَا جَعَلْتَهُ سَهْلًا وَأَنْتَ تَجْعَلُ الْحَزْنَ إِذَا شِئْتَ سَهْلًا",
        transliteration="Allahumma la sahla illa ma ja'altahu sahla wa anta taj'alul-hazna idha shi'ta sahla.",
        english="O Allah, there is no ease except in what You make easy, and You make difficulty easy if You will.",
        bangla="হে আল্লাহ, আপনি যা সহজ করে দেন তা ছাড়া কিছুই সহজ নয়; আর আপনি চাইলে কঠিনকেও সহজ করে দেন।",
        categories=["study_success", "distress_relief"],
        source_keys=["muslimaid", "celestialshiny"],
    ),
    entry(
        slug="allahumma-inni-asaluka-ilman-nafian",
        title="Beneficial Knowledge and Sound Understanding",
        arabic="اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْمًا نَافِعًا وَعَمَلًا صَالِحًا وَحِفْظًا قَوِيًّا وَفَهْمًا كَامِلًا وَعَقْلًا سَالِمًا",
        transliteration="Allahumma inni as'aluka 'ilman nafi'an wa 'amalan salihan wa hifzan qawiyyan wa fahman kamilan wa 'aqlan saliman.",
        english="O Allah, I ask You for beneficial knowledge, righteous deeds, strong memory, complete understanding and a sound mind.",
        bangla="হে আল্লাহ, আমি আপনার কাছে উপকারী জ্ঞান, নেক আমল, মজবুত স্মৃতি, পূর্ণ বুঝ এবং সুস্থ বিবেক প্রার্থনা করছি।",
        categories=["study_success"],
        source_keys=["muslimaid"],
        notes="This wording was taken from the provided source page as a studying dua.",
    ),
    entry(
        slug="allahumma-adhhib-ghayza-qalbi",
        title="Remove Anger from the Heart",
        arabic="اللَّهُمَّ أَذْهِبْ غَيْظَ قَلْبِي",
        transliteration="Allahumma adhhib ghayza qalbi.",
        english="O Allah, remove the anger from my heart.",
        bangla="হে আল্লাহ, আমার অন্তরের ক্রোধ দূর করে দিন।",
        categories=["heart_inner_state"],
        source_keys=["islamic_relief_canada"],
    ),
    entry(
        slug="allahumma-tahhir-qalbi",
        title="Purify the Heart",
        arabic="اللَّهُمَّ طَهِّرْ قَلْبِي مِنْ كُلِّ سُوءٍ وَاللَّهُمَّ طَهِّرْ قَلْبِي مِنْ كُلِّ مَا يُبْغِضُكَ وَاللَّهُمَّ طَهِّرْ قَلْبِي مِنْ كُلِّ غِلٍّ وَحِقْدٍ وَحَسَدٍ وَكِبْرٍ",
        transliteration="Allahumma tahhir qalbi min kulli su', Allahumma tahhir qalbi min kulli ma yubghiduka, Allahumma tahhir qalbi min kulli ghillin wa hiqdin wa hasadin wa kibr.",
        english="O Allah, cleanse my heart from every evil, from everything that displeases You, and from rancor, hatred, envy and arrogance.",
        bangla="হে আল্লাহ, আমার অন্তরকে সব অনিষ্ট, আপনার অপছন্দনীয় সবকিছু, এবং হিংসা-বিদ্বেষ-অহংকার থেকে পবিত্র করে দিন।",
        categories=["heart_inner_state", "guidance_faith"],
        source_keys=["islamic_relief_canada"],
    ),
    entry(
        slug="allahumma-inni-audhu-bika-minal-hammi",
        title="Relief from Anxiety and Sadness",
        arabic="اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ وَالْعَجْزِ وَالْكَسَلِ وَالْبُخْلِ وَالْجُبْنِ وَضَلَعِ الدَّيْنِ وَغَلَبَةِ الرِّجَالِ",
        transliteration="Allahumma inni a'udhu bika minal-hammi wal-hazan wal-'ajzi wal-kasal wal-bukhli wal-jubni wa dala'id-dayni wa ghalabatir-rijal.",
        english="O Allah, I seek refuge in You from worry and sadness, weakness and laziness, miserliness and cowardice, the burden of debt and being overpowered by people.",
        bangla="হে আল্লাহ, আমি আপনার কাছে উদ্বেগ ও দুঃখ, অক্ষমতা ও অলসতা, কৃপণতা ও ভীরুতা, ঋণের বোঝা এবং মানুষের প্রভাবের অধীন হয়ে পড়া থেকে আশ্রয় চাই।",
        categories=["distress_relief", "rizq_finance"],
        source_keys=["islamic_relief_canada", "mwa", "celestialshiny"],
    ),
    entry(
        slug="allahumma-ijal-fi-qalbi-nura",
        title="Light in the Heart",
        arabic="اللَّهُمَّ اجْعَلْ فِي قَلْبِي نُورًا وَفِي لِسَانِي نُورًا وَفِي سَمْعِي نُورًا وَفِي بَصَرِي نُورًا",
        transliteration="Allahumma ij'al fi qalbi nuran wa fi lisani nuran wa fi sam'i nuran wa fi basari nuran.",
        english="O Allah, place light in my heart, on my tongue, in my hearing and in my sight.",
        bangla="হে আল্লাহ, আমার অন্তরে, আমার জিহ্বায়, আমার শ্রবণে এবং আমার দৃষ্টিতে নূর দান করুন।",
        categories=["guidance_faith", "heart_inner_state"],
        source_keys=["islamic_relief_canada", "celestialshiny"],
    ),
    entry(
        slug="allahumma-inni-audhu-bika-min-sharri-sami",
        title="Protection from the Evil Within",
        arabic="اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ شَرِّ سَمْعِي وَمِنْ شَرِّ بَصَرِي وَمِنْ شَرِّ لِسَانِي وَمِنْ شَرِّ قَلْبِي وَمِنْ شَرِّ مَنِيِّي",
        transliteration="Allahumma inni a'udhu bika min sharri sam'i wa min sharri basari wa min sharri lisani wa min sharri qalbi wa min sharri maniyyi.",
        english="O Allah, I seek refuge in You from the evil of my hearing, my sight, my tongue, my heart and myself.",
        bangla="হে আল্লাহ, আমি আপনার কাছে আমার শ্রবণ, দৃষ্টি, জিহ্বা, অন্তর এবং নিজের অনিষ্ট থেকে আশ্রয় চাই।",
        categories=["protection", "guidance_faith"],
        source_keys=["islamic_relief_canada"],
    ),
    entry(
        slug="allahumma-akhrijni-min-az-zulumati-ila-an-nur",
        title="Bring Me from Darkness into Light",
        arabic="اللَّهُمَّ أَخْرِجْنِي مِنَ الظُّلُمَاتِ إِلَى النُّورِ",
        transliteration="Allahumma akhrijni minaz-zulumati ilan-nur.",
        english="O Allah, bring me out of darkness into light.",
        bangla="হে আল্লাহ, আমাকে অন্ধকার থেকে আলোতে বের করে আনুন।",
        categories=["guidance_faith", "heart_inner_state"],
        source_keys=["islamic_relief_canada"],
    ),
    entry(
        slug="allahumma-imla-qalbi-bihubbik",
        title="Fill My Heart with Your Love",
        arabic="اللَّهُمَّ امْلَأْ قَلْبِي بِحُبِّكَ",
        transliteration="Allahumma imla' qalbi bihubbik.",
        english="O Allah, fill my heart with Your love.",
        bangla="হে আল্লাহ, আমার অন্তরকে আপনার ভালোবাসায় পূর্ণ করে দিন।",
        categories=["guidance_faith", "heart_inner_state"],
        source_keys=["islamic_relief_canada"],
    ),
    entry(
        slug="allahumma-rahmataka-arju",
        title="Do Not Leave Me to Myself",
        arabic="اللَّهُمَّ رَحْمَتَكَ أَرْجُو فَلَا تَكِلْنِي إِلَى نَفْسِي طَرْفَةَ عَيْنٍ وَأَصْلِحْ لِي شَأْنِي كُلَّهُ لَا إِلَهَ إِلَّا أَنْتَ",
        transliteration="Allahumma rahmataka arju fala takilni ila nafsi tarfata 'aynin wa aslih li sha'ni kullahu la ilaha illa anta.",
        english="O Allah, I hope for Your mercy. Do not leave me to myself even for the blink of an eye. Set all my affairs right for me. There is no god except You.",
        bangla="হে আল্লাহ, আমি আপনার রহমতের আশাবাদী। এক পলকের জন্যও আমাকে আমার নিজের ওপর ছেড়ে দেবেন না, আমার সব কাজ সঠিক করে দিন। আপনি ছাড়া কোনো সত্য উপাস্য নেই।",
        categories=["morning_evening", "distress_relief"],
        source_keys=["mwa"],
    ),
    entry(
        slug="hasbiyallahu-la-ilaha-illa-huwa",
        title="Allah Is Sufficient for Me",
        arabic="حَسْبِيَ اللَّهُ لَا إِلَهَ إِلَّا هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيمِ",
        transliteration="Hasbiya Allahu la ilaha illa huwa 'alayhi tawakkaltu wa huwa rabbul-'arshil-'azim.",
        english="Allah is sufficient for me. There is no god except Him. In Him I place my trust, and He is the Lord of the Mighty Throne.",
        bangla="আল্লাহই আমার জন্য যথেষ্ট। তিনি ছাড়া কোনো সত্য উপাস্য নেই। আমি তাঁরই ওপর ভরসা করি, আর তিনি মহান আরশের অধিপতি।",
        categories=["distress_relief", "morning_evening", "guidance_faith"],
        source_keys=["mwa"],
    ),
    entry(
        slug="allahumma-inni-audhu-bika-minal-barasi",
        title="Protection from Severe Illness",
        arabic="اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْبَرَصِ وَالْجُنُونِ وَالْجُذَامِ وَمِنْ سَيِّئِ الْأَسْقَامِ",
        transliteration="Allahumma inni a'udhu bika minal-barasi wal-jununi wal-judhami wa min sayyi'il-asqam.",
        english="O Allah, I seek refuge in You from vitiligo, madness, leprosy and evil diseases.",
        bangla="হে আল্লাহ, আমি আপনার কাছে শ্বেত, উন্মাদনা, কুষ্ঠ এবং ভয়াবহ সব রোগ থেকে আশ্রয় চাই।",
        categories=["protection", "health"],
        source_keys=["mwa"],
    ),
    entry(
        slug="bismillahilladhi-la-yadurru",
        title="Protection from Harm",
        arabic="بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيعُ الْعَلِيمُ",
        transliteration="Bismillahil-ladhi la yadurru ma'asmihi shay'un fil-ardi wa la fis-sama'i wa huwas-sami'ul-'alim.",
        english="In the name of Allah, with whose name nothing on earth or in heaven can cause harm, and He is the All-Hearing, the All-Knowing.",
        bangla="আল্লাহর নামে শুরু করছি, যার নামের বরকতে আসমান ও জমিনের কোনো কিছুই ক্ষতি করতে পারে না; আর তিনি সর্বশ্রোতা, সর্বজ্ঞ।",
        categories=["morning_evening", "protection"],
        source_keys=["teachers_gov_bd"],
    ),
    entry(
        slug="allahumma-inna-najaluka-fi-nuhurihim",
        title="Protection from Harmful People",
        arabic="اللَّهُمَّ إِنَّا نَجْعَلُكَ فِي نُحُورِهِمْ وَنَعُوذُ بِكَ مِنْ شُرُورِهِمْ",
        transliteration="Allahumma inna naj'aluka fi nuhurihim wa na'udhu bika min shururihim.",
        english="O Allah, we place You before them and seek refuge in You from their evils.",
        bangla="হে আল্লাহ, আমরা তাদের মোকাবেলায় আপনাকেই ভরসা হিসেবে গ্রহণ করছি এবং তাদের অনিষ্ট থেকে আপনার আশ্রয় চাইছি।",
        categories=["protection"],
        source_keys=["teachers_gov_bd"],
    ),
    entry(
        slug="alhamdulillahil-ladhi-afani",
        title="When Seeing Someone Afflicted",
        arabic="الْحَمْدُ لِلَّهِ الَّذِي عَافَانِي مِمَّا ابْتَلَاكَ بِهِ وَفَضَّلَنِي عَلَى كَثِيرٍ مِمَّنْ خَلَقَ تَفْضِيلًا",
        transliteration="Alhamdulillahil-ladhi 'afani mimma ibtalaka bihi wa faddalani 'ala kathirin mimman khalaqa tafdila.",
        english="Praise be to Allah who kept me safe from what He tested you with and favored me greatly over many of those He created.",
        bangla="সকল প্রশংসা আল্লাহর, যিনি আমাকে সেই কষ্ট থেকে নিরাপদে রেখেছেন যাতে আপনাকে পরীক্ষা করেছেন এবং তাঁর অনেক সৃষ্টির ওপর আমাকে বিশেষ মর্যাদা দিয়েছেন।",
        categories=["health", "protection"],
        source_keys=["teachers_gov_bd"],
    ),
    entry(
        slug="inna-lillahi-wa-inna-ilayhi-rajiun-allahumma-ajurni",
        title="For Calamity and Loss",
        arabic="إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ، اللَّهُمَّ أْجُرْنِي فِي مُصِيبَتِي وَأَخْلِفْ لِي خَيْرًا مِنْهَا",
        transliteration="Inna lillahi wa inna ilayhi raji'un, Allahumma'jurni fi musibati wa akhlif li khayran minha.",
        english="Surely we belong to Allah and to Him we will return. O Allah, reward me in my calamity and replace it for me with something better.",
        bangla="নিশ্চয়ই আমরা আল্লাহরই এবং তাঁর কাছেই ফিরে যাব। হে আল্লাহ, আমার এই বিপদে আমাকে সওয়াব দিন এবং এর বদলে উত্তম কিছু দান করুন।",
        categories=["distress_relief"],
        source_keys=["teachers_gov_bd"],
    ),
    entry(
        slug="la-ilaha-illallahul-azimul-halim",
        title="Dua in Times of Distress",
        arabic="لَا إِلَهَ إِلَّا اللَّهُ الْعَظِيمُ الْحَلِيمُ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ الْعَرْشِ الْعَظِيمِ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ السَّمَاوَاتِ وَرَبُّ الْأَرْضِ وَرَبُّ الْعَرْشِ الْكَرِيمِ",
        transliteration="La ilaha illallahul-'azimul-halim, la ilaha illallahu rabbul-'arshil-'azim, la ilaha illallahu rabbus-samawati wa rabbul-ardi wa rabbul-'arshil-karim.",
        english="There is no god except Allah, the Magnificent, the Forbearing. There is no god except Allah, Lord of the Mighty Throne. There is no god except Allah, Lord of the heavens, Lord of the earth and Lord of the Noble Throne.",
        bangla="আল্লাহ ছাড়া কোনো সত্য উপাস্য নেই, তিনি মহিমান্বিত ও পরম সহনশীল। আল্লাহ ছাড়া কোনো সত্য উপাস্য নেই, তিনি মহান আরশের রব। আল্লাহ ছাড়া কোনো সত্য উপাস্য নেই, তিনি আসমানসমূহ, জমিন এবং সম্মানিত আরশের রব।",
        categories=["distress_relief"],
        source_keys=["teachers_gov_bd"],
    ),
    entry(
        slug="allahumma-inni-audhu-bika-minal-matham",
        title="Protection from Sin and Debt",
        arabic="اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْمَأْثَمِ وَالْمَغْرَمِ",
        transliteration="Allahumma inni a'udhu bika minal-ma'thami wal-maghram.",
        english="O Allah, I seek refuge in You from sin and debt.",
        bangla="হে আল্লাহ, আমি আপনার কাছে গুনাহ এবং ঋণের বোঝা থেকে আশ্রয় চাই।",
        categories=["forgiveness_repentance", "rizq_finance"],
        source_keys=["teachers_gov_bd"],
    ),
    entry(
        slug="rabbir-hamhuma",
        title="Dua for Parents",
        arabic="رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا",
        transliteration="Rabbir hamhuma kama rabbayani saghira.",
        english="My Lord, have mercy upon them as they raised me when I was small.",
        bangla="হে আমার রব, আমার পিতা-মাতার প্রতি দয়া করুন, যেমন তারা শৈশবে আমাকে লালন-পালন করেছেন।",
        categories=["family_parents"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="rabbana-ghfir-li-wa-liwalidayya",
        title="Forgive Me, My Parents and the Believers",
        arabic="رَبَّنَا اغْفِرْ لِي وَلِوَالِدَيَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ الْحِسَابُ",
        transliteration="Rabbana ighfir li wa liwalidayya wa lil-mu'minina yawma yaqumul-hisab.",
        english="Our Lord, forgive me, my parents and the believers on the Day the account is established.",
        bangla="হে আমাদের রব, হিসাব কায়েমের দিনে আমাকে, আমার পিতা-মাতাকে এবং সকল মুমিনকে ক্ষমা করে দিন।",
        categories=["family_parents", "forgiveness_repentance"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="rabbana-zalamna-anfusana",
        title="We Have Wronged Ourselves",
        arabic="رَبَّنَا ظَلَمْنَا أَنْفُسَنَا وَإِنْ لَمْ تَغْفِرْ لَنَا وَتَرْحَمْنَا لَنَكُونَنَّ مِنَ الْخَاسِرِينَ",
        transliteration="Rabbana zalamna anfusana wa illam taghfir lana wa tarhamna lanakunanna minal-khasirin.",
        english="Our Lord, we have wronged ourselves. If You do not forgive us and have mercy on us, we will surely be among the losers.",
        bangla="হে আমাদের রব, আমরা নিজেদের প্রতি জুলুম করেছি। আপনি যদি আমাদের ক্ষমা না করেন এবং দয়া না করেন, তবে অবশ্যই আমরা ক্ষতিগ্রস্তদের অন্তর্ভুক্ত হব।",
        categories=["forgiveness_repentance"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="ya-muqallibal-qulub",
        title="Keep My Heart Firm on Your Religion",
        arabic="يَا مُقَلِّبَ الْقُلُوبِ ثَبِّتْ قَلْبِي عَلَى دِينِكَ",
        transliteration="Ya muqallibal-qulubi thabbit qalbi 'ala dinik.",
        english="O Turner of the hearts, keep my heart firm upon Your religion.",
        bangla="হে অন্তরসমূহের পরিবর্তনকারী, আমার অন্তরকে আপনার দীনের ওপর দৃঢ় রাখুন।",
        categories=["guidance_faith"],
        source_keys=["dhakamail", "kalbela"],
    ),
    entry(
        slug="rabbana-la-tuzigh-qulubana",
        title="Do Not Let Our Hearts Deviate",
        arabic="رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِنْ لَدُنْكَ رَحْمَةً إِنَّكَ أَنْتَ الْوَهَّابُ",
        transliteration="Rabbana la tuzigh qulubana ba'da idh hadaytana wa hab lana min ladunka rahmah innaka antal-wahhab.",
        english="Our Lord, do not let our hearts deviate after You have guided us, and grant us mercy from Yourself. Surely You are the Bestower.",
        bangla="হে আমাদের রব, আপনি আমাদের হেদায়াত দেওয়ার পর আমাদের অন্তরকে বক্র করবেন না, এবং আপনার পক্ষ থেকে আমাদের রহমত দান করুন। নিশ্চয়ই আপনি মহান দাতা।",
        categories=["guidance_faith", "akhirah"],
        source_keys=["dhakamail", "kalbela", "islamic_relief_canada"],
    ),
    entry(
        slug="wa-ufawwidu-amri-ilallah",
        title="I Entrust My Affair to Allah",
        arabic="وَأُفَوِّضُ أَمْرِي إِلَى اللَّهِ إِنَّ اللَّهَ بَصِيرٌ بِالْعِبَادِ",
        transliteration="Wa ufawwidu amri ilallah innallaha basirun bil-'ibad.",
        english="I entrust my affair to Allah. Surely Allah is Seeing of His servants.",
        bangla="আমি আমার বিষয় আল্লাহর হাতে সোপর্দ করছি। নিশ্চয়ই আল্লাহ তাঁর বান্দাদের ব্যাপারে সর্বদ্রষ্টা।",
        categories=["distress_relief", "guidance_faith"],
        source_keys=["duas_org"],
    ),
    entry(
        slug="hasbunallahu-wa-nimal-wakil",
        title="Allah Is the Best Disposer of Affairs",
        arabic="حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ",
        transliteration="Hasbunallahu wa ni'mal-wakil.",
        english="Allah is sufficient for us, and He is the best disposer of affairs.",
        bangla="আল্লাহই আমাদের জন্য যথেষ্ট, আর তিনি উত্তম কর্মবিধায়ক।",
        categories=["distress_relief", "guidance_faith"],
        source_keys=["duas_org", "celestialshiny"],
    ),
    entry(
        slug="bismillah-tawakkaltu-alallah",
        title="Begin Tasks with Trust in Allah",
        arabic="بِسْمِ اللَّهِ تَوَكَّلْتُ عَلَى اللَّهِ",
        transliteration="Bismillah tawakkaltu 'alallah.",
        english="In the name of Allah, I place my trust in Allah.",
        bangla="আল্লাহর নামে শুরু করছি; আমি আল্লাহর ওপরই ভরসা করছি।",
        categories=["study_success", "guidance_faith"],
        source_keys=["celestialshiny"],
    ),
    entry(
        slug="allahumma-ihdini-wa-saddidni",
        title="Guide Me and Keep Me Upright",
        arabic="اللَّهُمَّ اهْدِنِي وَسَدِّدْنِي",
        transliteration="Allahumma ihdini wa saddidni.",
        english="O Allah, guide me and grant me correctness.",
        bangla="হে আল্লাহ, আমাকে হেদায়াত দিন এবং সঠিকতায় স্থির রাখুন।",
        categories=["guidance_faith", "study_success"],
        source_keys=["celestialshiny"],
    ),
    entry(
        slug="allahumma-barik-li-fi-rizqi",
        title="Bless My Provision",
        arabic="اللَّهُمَّ بَارِكْ لِي فِي رِزْقِي",
        transliteration="Allahumma barik li fi rizqi.",
        english="O Allah, bless my provision.",
        bangla="হে আল্লাহ, আমার রিজিকে বরকত দান করুন।",
        categories=["rizq_finance"],
        source_keys=["celestialshiny"],
    ),
]


def dedupe(entries: list[dict]) -> list[dict]:
    merged: dict[str, dict] = {}

    for item in entries:
        key = normalize_arabic(item["arabic"])
        if key not in merged:
            merged[key] = {**item}
            continue
        current = merged[key]
        current["source_urls"] = sorted(set(current["source_urls"] + item["source_urls"]))
        current["categories"] = sorted(set(current["categories"] + item["categories"]))
        if "notes" in item and "notes" not in current:
            current["notes"] = item["notes"]

    return sorted(merged.values(), key=lambda x: x["slug"])


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    duas = dedupe(RAW)

    category_map: dict[str, list[dict]] = defaultdict(list)
    for dua in duas:
        for category in dua["categories"]:
            category_map[category].append(dua)

    for category, items in category_map.items():
        items.sort(key=lambda x: x["title"])

    index = {
        "summary": {
            "unique_dua_count": len(duas),
            "categories": {k: len(v) for k, v in sorted(category_map.items())},
            "source_urls_used": sorted({url for dua in duas for url in dua["source_urls"]}),
            "source_urls_without_imported_dua_text": [SOURCES["play_store"]],
        },
        "collection_files": {
            category: f"collections/{category}.json" for category in sorted(category_map)
        },
        "all_duas_file": "doas.json",
    }

    readme = """Offline Dua asset folder

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
"""

    DOA_DIR.mkdir(parents=True, exist_ok=True)
    COLLECTIONS_DIR.mkdir(parents=True, exist_ok=True)
    for stale_file in COLLECTIONS_DIR.glob("*.json"):
        stale_file.unlink()
    (DOA_DIR / "README.md").write_text(readme, encoding="utf-8")
    write_json(DOA_DIR / "doas.json", duas)
    write_json(DOA_DIR / "index.json", index)
    old_all = DOA_DIR / "all_duas.json"
    if old_all.exists():
        old_all.unlink()

    for category, items in sorted(category_map.items()):
        collection = {
            "collection": category,
            "collection_name": category.replace("_", " ").title(),
            "duas": [
                {
                    "number": i + 1,
                    **item,
                }
                for i, item in enumerate(items)
            ],
        }
        write_json(COLLECTIONS_DIR / f"{category}.json", collection)


if __name__ == "__main__":
    main()
