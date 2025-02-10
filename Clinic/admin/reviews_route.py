from aiohttp.web_routedef import route
from flask import Blueprint
from socks import method

from clinic.admin.bl_models.doctors_bl import DoctorBL

admin_reviews_route = Blueprint("admin_reviews_route", __name__)


@admin_reviews_route.route('/admin/reviews', methods=["GET"])
def get_reviews():
    reviews, error = DoctorBL.get_reviews()