# infrastructure/routes/task_routes.py
# Este archivo puede ser opcional si prefieres definir las rutas directamente en tu archivo principal de Flask o dentro de los controladores.

from infrastructure.controllers.task_controller import task_blueprint

def init_app(app):
    app.register_blueprint(task_blueprint)
