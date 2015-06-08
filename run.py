#!venv/bin/python
import os
from app import app

DEBUG = os.environ.get("DEBUG", False)
app.run(debug = DEBUG)