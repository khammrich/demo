# import the application factory from eddemo
# future wsgi.py file

from eddemo import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')