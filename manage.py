#! /usr/bin/env python3
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'development')

if __name__ == '__main__':
    os.getenv('FLASK_CONFIG')
    app.run(port=8102)
