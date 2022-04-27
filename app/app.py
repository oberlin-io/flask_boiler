from flask import Flask
import config as cnf


def run():

    app=Flask(__name__)

    @app.route('/')
    def home():
        r={
            'status': 'success',
            }
        return r

    app.run(host=cnf.app_host, port=cnf.app_port)


if __name__=='__main__':
    run()
