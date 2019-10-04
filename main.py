from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

        <form action="/action_page.php" method="POST">
            Rotate by:<input type="text" name="rot" value="0">
            <textarea name="text" rows="10" cols="30"></textarea>
            <input type="submit">
        </form>

    </body>
</html>"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form.get("rot")
    string = request.form.get("text")
    encrypted_msg = rotate_string(string, rotation)

    return encrypted_msg


@app.route("/")
def index():
    return form

app.run()