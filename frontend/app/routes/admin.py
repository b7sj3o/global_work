import json
from flask import redirect, render_template, request, session, url_for, current_app
import requests
from ..utils import create_blueprint

admin_bp = create_blueprint(name="admin", url_prefix="/admin")

@admin_bp.route("/")
def admin():
    if 'authorized' in session:
        show_archieved = request.args.get('show_archieved', 'False') == 'True'
        
        response = requests.get(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/list", params={"show_archieved": show_archieved})
        data = json.loads(response.text)

        return render_template("admin.html", vacancy_requests=data, show_archieved=show_archieved)

    return redirect(url_for("base.home"))
