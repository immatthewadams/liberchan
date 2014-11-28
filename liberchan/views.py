from liberchan import app


@app.route('/', methods=['GET'])
def index():
    return 'Index'


@app.route('/<post_id>/', methods=['GET'])
def show_post(post_id):
    return 'Post ' + post_id