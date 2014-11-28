from liberchan import app


@app.route('/<post_id>/', methods=['GET'])
def show_post(post_id):
    return 'Post ' + post_id