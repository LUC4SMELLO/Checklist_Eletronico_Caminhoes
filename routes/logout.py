from flask import Blueprint, redirect, url_for

logout_bp = Blueprint("logout", __name__)

@logout_bp.route("/logout", methods=["GET"])
def logout():

    return redirect(url_for("/.homepage"))