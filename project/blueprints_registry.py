from flask import Flask

def register_blueprint(app: Flask):

	#from project.api.ping import ping_blueprint
	#app.register_blueprint(ping_blueprint, url_prefix="/api")

	from project.api.user import user_blueprint
	app.register_blueprint(user_blueprint, url_prefix="/api")

	from project.api.post import post_blueprint
	app.register_blueprint(post_blueprint, url_prefix="/api")

	from project.api.follow import follow_blueprint
	app.register_blueprint(follow_blueprint, url_prefix="/api")