from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Index'


@app.route('/posts/<post_id>', methods=['GET'])
def show_post(post_id):
    return 'Post ' + post_id

if __name__ == '__main__':
    app.run(debug=True)