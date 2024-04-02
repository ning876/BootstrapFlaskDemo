import os
import uuid
from config import cfg
ALLOWED_EXTENSIONS=cfg.get('user_profile','').get('ALLOWED_EXTENSIONS','')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_filename(filename):
    extensions=filename.rsplit('.', 1)[1]
    filename=str(uuid.uuid4())+'.'+extensions
    return filename
