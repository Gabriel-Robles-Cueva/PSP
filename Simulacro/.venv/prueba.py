from Flask import flask

application= Flask(__name__)

@application.route('/get-users/<username>')
def get_users(username):
    return "Algo"+username