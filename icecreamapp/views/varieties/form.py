import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from icecreamapp.models import Variety
from icecreamapp.models import model_factory
from ..connection import Connection


def get_varieties():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Variety)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            v.id,
            v.name,
            v.country_of_origin
        from icecreamapp_variety v
        """)

        return db_cursor.fetchall()

# @login_required
def variety_form(request):
    if request.method == 'GET':
        varieties = get_varieties()
        template = 'varieties/form.html'
        context = {
            'all_varieties': varieties
        }

        return render(request, template, context)
