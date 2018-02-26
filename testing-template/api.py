from flask import Flask
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)


class {{ resource_name }}(Resource):
    def get(self):
        return {'hello': 'world'}


{% if health_check == 'yes' %}
class HealthCheck(Resource):
    def get(self):
        return {}
{% endif %}


api.add_resource({{ resource_name }}, '/')

{% if health_check == 'yes' %}
api.add_resource(HealthCheck, '/health')
{% endif %}

if __name__ == '__main__':
    app.run(debug = True)
