from flask import render_template
from ..utils import create_blueprint

admin_bp = create_blueprint(name="admin", url_prefix="/admin")

@admin_bp.route("/")
def admin():
    return render_template("admin.html")