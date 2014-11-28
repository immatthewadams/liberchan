from liberchan import app


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/<post_id>/', methods=['GET'])
def show_post(post_id):
    return 'Post ' + post_id