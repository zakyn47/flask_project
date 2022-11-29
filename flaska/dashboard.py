import functools
import pandas
import requests
import json

from flask import Blueprint, render_template
from werkzeug.security import check_password_hash, generate_password_hash

from flaska.db import get_db
from flaska.auth import login_required
import pandas
import random

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@login_required
@bp.route("/dashboard", methods=("GET", "POST"))
def dashboard():
    return render_template(
        "dashboard/dashboard.html",
        data=osrs_item_search(random.randrange(1, 5000)))


def osrs_item_search(item_id):
    if id_exist(item_id):
        data = requests.get(f"https://secure.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={item_id}").json()
        return data["item"]

    else:
        return f"{item_id} Item id does not exist"


def id_exist(item_id):
    data = requests.get(f"https://secure.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={item_id}")
    return True if data.status_code == 200 else False
