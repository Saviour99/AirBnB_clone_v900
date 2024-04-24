#!/usr/bin/env bash
#This is the hello module

sudo apt install python3

python3 -m venv venv

venv/bin/activate

cd venv

python3 -m pip install --upgrade pip

pip install flask

echo "from flask import Flask\napp = Flask(__name__)\n\n@app.route("/",strict_slashes=False)\ndef hello():\n\treturn "Hello HBNB!"\n\nif (__name__) == "__main__":\n\tapp.run(host="0.0.0.0", port=5000)" > app.py

export FLASK_APP=app

flask run
