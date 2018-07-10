from flask import Flask, render_template


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        """
        Index page of the web app

        :return: Flask response
        """
        return render_template('index.html')
    return app

if __name__ == '__main__':
    app =create_app()
    app.run()