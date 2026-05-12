import re
import discord

from scraper import get_article
from validator import validate_article
from summarizer import summarize_article

# ⚠️ MASUKIN TOKEN BARU KAMU DI SINI (SUDAH HARUS DI-RESET)
TOKEN = "your discord token"

# ⚙️ INTENTS
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("🔥 ORYON ONLINE - READY TO SUMMARIZE")


@client.event
async def on_message(message):

    # ❌ ignore bot sendiri
    if message.author == client.user:
        return

    content = message.content.strip()

    # 🧠 PRIORITY 1 — COMMAND MODE (!oryon)
    if content.lower().startswith("!oryon"):

        # 🔍 extract URL dari message
        match = re.search(r"https?://\S+", content)

        if not match:
            await message.channel.send("⚠️ Format: !oryon <link berita>")
            return

        url = match.group(0)
        user = message.author

        await message.channel.send(f"🧠 ORYON sedang memproses artikel untuk {user.mention}...")

        try:
            # 1. SCRAPE
            title, text = get_article(url)

            # 2. VALIDATE
            error = validate_article(title, text)

            if error:
                await message.channel.send(f"{user.mention}\n{error}")
                return

            # 3. SUMMARIZE AI
            hasil = summarize_article(title, text)

            # 4. OUTPUT
            await message.channel.send(
                f"✨ **ORYON SUMMARY**\n"
                f"{user.mention}\n\n"
                f"---\n"
                f"{hasil}"
            )

        except Exception as e:
            await message.channel.send(
                f"{user.mention}\n"
                "❌ Terjadi kesalahan saat memproses artikel.\n\n"
                f"Detail: {e}"
            )

        return  # ⛔ stop di sini supaya gak lanjut ke mention logic

    # 🧠 PRIORITY 2 — MENTION MODE (@ORYON)
    if client.user in message.mentions:

        await message.channel.send(
            f"""✨ **ORYON AI ASSISTANT**

Halo {message.author.mention}, saya ORYON.

Saya adalah AI yang dapat merangkum berita dari link menjadi ringkasan singkat, jelas, dan mudah dipahami.

📌 **Cara menggunakan ORYON:**
`!oryon <link berita>`

💡 **Contoh:**
`!oryon https://cnn.com/article`

🧠 Saya akan:
- membaca artikel dari link
- menyaring informasi penting
- membuat ringkasan otomatis

Silakan kirim link berita 🚀
"""
        )

        return


client.run(TOKEN)