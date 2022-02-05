from api import create_app

app = create_app()
@app.route("/")
def root_path():
    return "hello"

if __name__ == "__main__":
    app.run()