from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# SQLAlchemy를 인스턴스화 한다
db = SQLAlchemy()

# CSRF 인스턴스 생성
csrf = CSRFProtect()


# create_app함수 생성
def create_app():
    # 플라스크 인스턴스(객체)를 생성
    app = Flask(__name__)

    # 앱의 config 설정한다
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBs32J",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # SQL을 콘솔 로그에 출력하는 설정
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY="AuwzyszUSsugKN7KZs6f2",
    )

    # SQLAlchemy와 앱을 연계한다
    db.init_app(app)
    # Migrate와 앱을 연계한다
    Migrate(app, db)
    csrf.init_app(app)

    from apps.crud import views as crud_views

    # register_blueprint
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
