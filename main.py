from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

# Initialize game variables
x = randint(1, 100)
attempt = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global x, attempt
    message = ""
    if request.method == "POST":
        try:
            user_num = int(request.form["number"])
            attempt += 1
            if user_num == x:
                message = f"Угадал! Загаданное число: {x}. Количество попыток: {attempt}"
                x = randint(1, 100)  # Reset the game
                attempt = 0
            elif user_num > x:
                message = "Загаданное число меньше этого."
            elif user_num < x:
                message = "Загаданное число больше этого."
        except ValueError:
            message = "Пожалуйста, введите корректное число."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)