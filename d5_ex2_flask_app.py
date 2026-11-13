from flask import Flask, abort

app = Flask("__name__")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


users = [
    "john", "jane", "joe", "anne",
]

@app.route("/users/")
def user_list():
    lis = [
        f"<li>{user}</li>"
        for user in users
    ]

    return f"<ul>{"\n".join(lis)}</ul>"

@app.route("/users/<name>")
def user(name):
    if name not in users:
        abort(404)

    return f"<p>Salut, pagina user-ului {name}.</p>"

# se execută cu (comandă de shell)
# flask --debug --app d5_ex2_flask_app.py run