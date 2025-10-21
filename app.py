from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        user_id = int(request.args.get('id', 1))
    except (ValueError, TypeError):
        user_id = 1
    return f'<h1>Hello, user #{user_id}!</h1>'


if __name__ == '__main__':
    app.run(debug=True) 