from flask import Blueprint, render_template

# selfAssembly blueprint definition
selfAssembly = Blueprint('selfAssembly', __name__, static_folder='static', static_url_path='/selfAssembly', template_folder='templates')


# Routes
@selfAssembly.route('/selfAssembly')
def index():
    return render_template('selfAssembly.html')
