UPLOAD_HTML = '''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
</form>
'''

ALLOWED_EXTENSIONS = ['pdf','md','txt']
def allowed_file(filename):
    return filename.count('.') == 1 and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_stored_filename(filename):
    import uuid
    GITIGNORE_PREFIX = 'DYNAMIC_DOCUMENT_UPLOAD_'
    random_suffix = uuid.uuid4().hex
    name, extension = filename.split('.')
    return GITIGNORE_PREFIX + name + random_suffix + '.' + extension
