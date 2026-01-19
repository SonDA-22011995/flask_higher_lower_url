from functools import wraps

from flask import Flask, render_template, abort, session
from ultils_number import (
    generate_random_number,
    is_valid_int_input,
    compare_numbers
)


app = Flask(__name__)
app.secret_key = "Sonda@" + '154936480668766032181586949800592793298'

def render_result(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        result = func(*args, **kwargs)

        html = ""
        if result == -1:
            html = f'<h1>Too low, try again!</h1>'
            html += (
                f'<img '
                    f'src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"'
                    f'style="width:300px;height:300px"'
                f'/>'
            )

        if result == 0:
            html = f'<h1>Too high, try again!</h1>'
            html += (
                f'<img '
                    f'src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"'
                    f'style="width:300px;height:300px"'
                f'/>'
            )

        if result == 1:
            html = f'<h1>You found me</h1>'
            html += (
                f'<img '
                    f'src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"'
                    f'style="width:300px;height:300px"'
                f'/>'
            )

            html += f'<a style="display:block" href="/">Play again!</a>'

        return html

    return wrapper_func

@app.route("/")
def home():
    session["random_number"] = generate_random_number()

    html = "<h1>Guess a number between 0 and 9</h1>"
    html = (html +
            f'<img '
                f'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" '
                f'style="width:300px;height:300px"'
            f'/>'
            )
    return html


@app.route("/guess/<number>")
@render_result
def guess(number: str):
    if not is_valid_int_input(number):
        abort(400, description="The number is not valid")

    random_number = session.get("random_number")
    result = compare_numbers(int(number), random_number)
    return result

@app.errorhandler(400)
def page_not_found(error):
    return render_template(
        "400.html",
        message=error.description
    ), 400

if __name__ == "__main__":
    app.run(debug=True)


