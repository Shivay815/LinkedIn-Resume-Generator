from flask import Flask, send_from_directory
from routes.api_routes import api_blueprint
from config.config import Config

def create_app():
    app = Flask(__name__, static_folder="static")

    # Load configuration
    app.config.from_object(Config)
    
    # Register the Blueprint for routes
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Serve the HTML files
    @app.route('/')
    def index():
        return send_from_directory('static', 'index.html')

    @app.route('/resume.html')
    def resume_page():
        return send_from_directory('static', 'resume.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
