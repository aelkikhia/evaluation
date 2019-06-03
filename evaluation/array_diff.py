from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required
from evaluation.eval_lib import array_diff


class ArrayDiff(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("current",
                        type=list,
                        required=True,
                        location='json',
                        help="must be a list")
    parser.add_argument("target",
                        type=list,
                        required=True,
                        location='json',
                        help="must be a list")

    # @jwt_required()
    def post(self):
        data = ArrayDiff.parser.parse_args()

        additions, deletions = array_diff(data['current'], data['target'])

        return {'additions': additions, 'deletions': deletions}, 200

