from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Website Python</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background-color: #f2f2f2;
                padding-top: 250px;
            }

            h1 {
                color: #e63946;
            }

            p {
                font-size: 18px;
            }

            button {
                padding: 12px 25px;
                background-color: #e63946;
                color: yellow;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <h1>Halo, Dunia!</h1>
        <p>Website ini dibuat menggunakan Python Flask.</p>
        <button>Pesan Sekarang</button>
    </body>
    </html>
    """

app.run(debug=True)