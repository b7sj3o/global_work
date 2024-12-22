import json
from flask import abort, redirect, render_template, request, session, url_for, current_app
import requests
from ..utils import create_blueprint

admin_bp = create_blueprint(name="admin", url_prefix="/admin")

@admin_bp.route("/")
def admin():
    if not session.get("authorized"):
        abort(403)

    show_archieved = request.args.get('show_archieved', 'False') == 'True'
    
    response = requests.get(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/list", params={"show_archieved": show_archieved})
    data = json.loads(response.text)
    
    # TODO: refactor this piece of shit
    for i in range(len(data)):
        created_at = data[i]['created_at']
        date, time = created_at.split('T')
        year, month, day = date.split('-')
        data[i]['created_at'] = f"{month}.{day}.{year}, {time[:5]}"

    return render_template("admin.html", vacancy_requests=data, show_archieved=show_archieved)