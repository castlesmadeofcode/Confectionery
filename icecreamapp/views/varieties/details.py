import sqlite3
from django.shortcuts import render, redirect, reverse
from icecreamapp.models import Variety
from icecreamapp.models import model_factory
from ..connection import Connection



def get_variety(variety_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Variety)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            v.id,
            v.name,
            v.country_of_origin
        FROM icecreamapp_variety v
        WHERE v.id = ?
        """, (variety_id,))

        return db_cursor.fetchone()
        

def get_variety_flavor(variety_id): 
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Variety)
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            vf.id, 
                vf.flavor_id,
                vf.variety_id, 
                vf.toppings,
                f.id, 
                f.name, 
                f.alcohol_percent, 
                v.id,
                v.name,
                v.country_of_origin
            FROM icecreamapp_varietyflavor vf
            JOIN icecreamapp_variety v ON v.id = vf.variety_id    
            JOIN icecreamapp_flavor f ON f.id = vf.flavor_id     
            WHERE v.id = ?
        """, (variety_id,))
        return db_cursor.fetchall()


def variety_details(request, variety_id):
    if request.method == 'GET':
        variety = get_variety(variety_id)
        variety_flavor = get_variety_flavor(variety_id)
        template = 'varieties/detail.html'
        context = {
            'variety': variety,
            'variety_flavor': variety_flavor
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE icecreamapp_variety
                SET name = ?,
                    country_of_origin = ?

                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['country_of_origin'],
                    variety_id,
                ))

            return redirect(reverse('icecreamapp:varieties'))

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM icecreamapp_varietyflavor
                WHERE id = ?
                """, (variety_id,))

            return redirect(reverse('icecreamapp:varieties'))