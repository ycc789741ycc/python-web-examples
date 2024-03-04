from flask import Flask, jsonify, make_response


def create_app():
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def health_check():
        return make_response(jsonify({'status': 'ok'}), 200)

    return app
