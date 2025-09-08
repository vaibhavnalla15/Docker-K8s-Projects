# A simple Flask web application that serves a dynamic "Hello World" message.
# Flask is a lightweight framework for building web apps in Python.
from flask import Flask, render_template_string

app = Flask(__name__)

# The HTML template for our web page. It uses a variable 'message'.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kubernetes Hello</title>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            text-align: center;
        }
        .container {
            background-color: #161b22;
            padding: 40px 60px;
            border-radius: 12px;
            border: 1px solid #30363d;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease-in-out;
        }
        .container:hover {
            transform: scale(1.05);
        }
        h1 {
            font-size: 2.5rem;
            color: #58a6ff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        p {
            font-size: 1.2rem;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ message }}</h1>
        <p>This page is served from a container running in a Kubernetes Pod.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    # This function is executed when a user visits the root URL ('/').
    # We pass the desired message to the HTML template.
    return render_template_string(HTML_TEMPLATE, message="Hello from Docker 🐳 & Kubernetes ☸️")

if __name__ == '__main__':
    # This block runs the app. 'host="0.0.0.0"' makes it accessible from outside the container.
    app.run(host='0.0.0.0', port=5000, debug=True)
