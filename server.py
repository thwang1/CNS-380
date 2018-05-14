from flask import Flask, request

app = Flask(__name__)
files = list()

@app.route("/api/add", methods=["POST"])
def api_add():
    data = request.form.get("data")
    files.append("[{}] {}<br>".format(request.remote_addr,data))
    return str()

@app.route("/")
def root():
    return "\n".join(files)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)

