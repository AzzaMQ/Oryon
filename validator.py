#validator
def validate_article(title, text):

    # artikel kosong
    if not text.strip():

        return """
Website tidak bisa dibaca.

Kemungkinan:
- website memblokir scraping
- artikel premium
- atau website menggunakan JavaScript
"""

    # artikel terlalu pendek
    if len(text) < 200:

        return f"""
Artikel gagal dibaca dengan sempurna.

Website kemungkinan:
- memblokir bot
- menggunakan proteksi anti scraping
- atau artikel premium/paywall

Judul yang terdeteksi:
{title}
"""

    # deteksi anti bot
    bad_words = [
        "enable javascript",
        "sign up",
        "subscribe",
        "cookie policy",
        "accept cookies"
    ]

    for word in bad_words:

        if word.lower() in text.lower():

            return """
Website ini menggunakan proteksi JavaScript / anti bot.

Coba gunakan website lain seperti:
- CNN
- Kompas
- CNBC
- Reuters
- Detik
"""

    return None