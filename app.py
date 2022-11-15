from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint
from settings import create_app, ENVIRONMENT_NAME

from _WebApi.ChistesController import chistes_controller


app = create_app(ENVIRONMENT_NAME)
db = SQLAlchemy(app)

Context = app.config["CONTEXT_FACTORY"](app)
#Context.setup()

cors = CORS(app)

app.register_blueprint(chistes_controller)


SWAGGER_URL = '/api'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Template - Backend (API REST)",
        'docExpansion': "none",
        'filter': ''
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(port=app.config["PORT"])
