from flask import Blueprint
from flask.helpers import url_for
from flask.templating import render_template
from flask_login import current_user, login_required
from flask_login.utils import logout_user
from werkzeug.utils import redirect

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', static_folder='static')

@main_blueprint.route('/app', methods=['GET'])
@login_required
def app():
    return render_template(
        'app.html',
        current_user=current_user
    )

@main_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_blueprint.login'))