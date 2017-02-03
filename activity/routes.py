from flask_restful import Api

from activity.controllers.activity import ActivityAPI, ActivityListAPI

def configure(app):
    api = Api(app)
    api.add_resource(ActivityAPI, '/activities/<int:id>', endpoint = 'activity')
    api.add_resource(ActivityListAPI, '/activities', endpoint = 'activities')

# @app.route("/")
# def hello():
#     return jsonify({'result': "Hello World!"})