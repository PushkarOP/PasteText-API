from flask import Flask, request, render_template_string, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import string
import random
from markupsafe import escape

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Text(db.Model):
    id = db.Column(db.String, primary_key=True)
    content = db.Column(db.Text)

@app.route('/', methods=['POST'])
def post_text():
    content = request.get_json().get('content')
    id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    text = Text(id=id, content=content)
    db.session.add(text)
    db.session.commit()
    return jsonify({'id': id, 'link': request.host_url + 'text/' + id})

@app.route('/text/<id>', methods=['GET'])
def get_text(id):
    text = Text.query.get_or_404(id)
    escaped_text = escape(text.content)  # escape before rendering
    return render_template_string(escaped_text)

if __name__ == '__main__':
    with app.app_context(): 
        if not os.path.exists('/tmp/test.db'):
            db.create_all()
    app.run(host='0.0.0.0', port=8000)
