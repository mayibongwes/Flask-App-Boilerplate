from flask import Blueprint, render_template,  abort, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # try:
    return render_template('index.html')
    # except:
    #     abort(422)


@main.errorhandler(404)
def not_found(error):
    return (
    jsonify(
            {"success": False,
             "error": 404,
             "message":
             "Resource Not Found"}
            ),
            404,
    )

@main.errorhandler(422)
def unprocessable(error):
    return (
        jsonify(
                {"success": False,
                 "error": 422,
                 "message": "Unprocessable"}
                ),
                422,
    )

# Add other HHTTP status code handlers