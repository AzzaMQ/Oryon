#app
from flask import Flask, render_template, request

from scraper import get_article
from validator import validate_article
from summarizer import summarize_article

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home', methods=['GET', 'POST'])
def home():

    hasil = ""

    if request.method == 'POST':

        url = request.form['url']

        try:

            print("\n========================")
            print("LINK MASUK:")
            print(url)
            print("========================\n")

            # ambil artikel
            title, text = get_article(url)

            print("\n===== JUDUL =====\n")
            print(title)

            print("\n===== HASIL SCRAPING =====\n")
            print(text)

            # validasi artikel
            error = validate_article(title, text)

            if error:

                return render_template(
                    "index.html",
                    hasil=error
                )

            print("\nAI sedang merangkum...\n")

            # summarize AI
            hasil = summarize_article(title, text)

        except Exception as e:

            print("\n===== ERROR =====\n")
            print(e)

            hasil = f"""
Terjadi error saat memproses artikel.

Detail:
{e}
"""

    return render_template("index.html", hasil=hasil)


if __name__ == '__main__':

    app.run(debug=True)