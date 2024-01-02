from werkzeug.utils import secure_filename
from flask import Flask, request
from documents import *
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'File missing', 422

        file = request.files['file']
        if file.filename == '':
            return 'Filename missing', 422

        if file and allowed_file(file.filename):
            # Use a secure filename (no arbitrary paths) with a random suffix
            filename = secure_filename(generate_stored_filename(file.filename))
            file.save(filename)
            import sqlite3
            time = datetime.now().isoformat()
            with sqlite3.connect('db.sqlite') as conn:
                cur = conn.cursor()
                cur.execute("""INSERT INTO files('filename', 'time_created') VALUES(?, ?);""", (filename, time))
            return 'Uploaded!', 200
    return UPLOAD_HTML, 200
@app.route('/get_files')
def get_files():
    import sqlite3
    html = ""
    html_prefix = """
<table>
  <tr>
    <th>Filename</th>
    <th>Timestamp</th>
  </tr>
"""
    html_postfix = """
</table>
"""
    with sqlite3.connect('db.sqlite') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM files;")
        for filename, timestamp in cur.fetchall():
            html += f"<tr><td>{filename}</td><td>{timestamp}</td></tr>"
    return html_prefix + html + html_postfix, 200            

if __name__ == '__main__':
    app.run(debug=True)
