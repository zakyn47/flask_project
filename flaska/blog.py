from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaska.auth import login_required
from flaska.db import get_db
import requests
import pandas
import json


bp = Blueprint("blog", __name__)

@bp.route("/")
@login_required
def index():
    return render_template(
        "blog/index.html",
        data_cz=tipsport_data("CZ"),
        data_sk=tipsport_data("SK"))

def tipsport_data(country:str):
    data = requests.get(
        f"https://www.tipsport.{country}/rest/casino/v6/games/lobby?mobile=false&brandSite=TIPSPORT_{country}").json()
    nejhranejsi_hry = json.dumps(data["lobbyGames"][0]["games"])
    sorted_data = pandas.read_json(nejhranejsi_hry).sort_values(by="popularity", ascending=False)[["name", "popularity"]]
    return sorted_data.to_html()

