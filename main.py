from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
# define where database is located (use 'sqlite:///tmp/database.db to save within a folder inside the path currently on (relative path))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# # for initalising db
# videos = {}
# def abort_if_video_id_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, message="Video ID could not be found...")
# def abort_if_video_exists(video_id):
#     if video_id in videos:
#         abort(409, "Video already exsits with that ID...")

class Video(Resource):
    @marshal_with(resource_fields) # serialises result into json
    def get(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)
        result = VideoModel.query.get(id=video_id)
        return result
    @marshal_with(resource_fields)
    def post(self, video_id):
        # abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        # videos[video_id] = args
        return video, 201
    def delete(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204

# register as a resource
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    with app.app_context():
        # # initialises db, commented so generated db is not overridden
        # db.create_all()
        app.run(debug=True)

