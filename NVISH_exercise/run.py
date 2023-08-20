from flask_migrate import Migrate

from app import create_app, db

app = create_app()
migrate = Migrate(app, db)


if __name__ == '__main__':
    with app.test_request_context():
        print("registering endpoints: ")
        for rule in app.url_map.iter_rules():
            print(rule.endpoint)

    app.run(host='0.0.0.0', port=5000, debug=True)
