#summarizer
import ollama

def summarize_article(title, text):

    # batasi text
    text = text[:1200]

    response_ai = ollama.chat(

        model='llama3.2',

        messages=[

            {
                'role': 'user',

                'content': f'''

Kamu adalah AI peringkas berita modern.

Aturan:
- langsung mulai ke isi
- jangan gunakan kalimat pembuka
- jangan bilang "berikut ringkasan"
- jangan terlalu formal
- singkat dan jelas
- enak dibaca

Format WAJIB:

RINGKASAN UTAMA
(paragraf)

POIN PENTING
- poin 1
- poin 2
- poin 3

KESIMPULAN
(kesimpulan singkat)

Judul:
{title}

Isi:
{text}

'''
            }

        ]

    )

    hasil = response_ai['message']['content']

    # kalau AI gagal jawab
    if not hasil.strip():

        return """
AI gagal membuat rangkuman.

Coba:
- gunakan artikel lain
- atau ulang beberapa saat lagi
"""

    return hasil