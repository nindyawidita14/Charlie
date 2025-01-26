"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Senior Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
UPDATED:       07/06/2024
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""
import json
import plotly
import plotly.express as px
import pandas as pd
from flask import Blueprint, render_template, request,jsonify
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = db_mod.get_distinct_pcts()
    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
    else:
        # pick a default PCT to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)

    # prepare data structure to send to front end to update display
    dashboard_data = {    
        "tile_data_items": generate_data_for_tiles(),  
        "top_items_plot_data": generate_top_px_items_barchart_data(),
        "pct_list": pcts,
        "pct_data": selected_pct_data,
        "search_value": search_list
        
    }

    db_mod.get_average_act_cost()
    db_mod.get_total_act_cost()
    
    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html',dashboard_data=dashboard_data)

def generate_data_for_tiles():
    """Generate the data for the four home page tiles."""
    tile_data = {
        "total_items": db_mod.get_total_number_items(),
        "avg_act_cost": db_mod.get_average_act_cost(),
        "total_act_cost": db_mod.get_total_act_cost(),
        "top_px_item": None,
        "num_unique_items": None
    }
    return tile_data



def generate_top_px_items_barchart_data():
    """Generate the data needed to populate the number of most prescrbed items per PCT barchart."""
    
    # Create a dataframe to store the database query results
    df = pd.DataFrame({
        "data_values": db_mod.get_prescribed_items_per_pct(),
        "pct_codes": db_mod.get_distinct_pcts()
    })
    # Generate the plot
    fig = px.bar(df, x="pct_codes", y="data_values", 
                 labels={"pct_codes": "PCT code", 
                         "data_values": "Prescribed items (number)"}).update_xaxes(categoryorder="sum descending")

    # Convert the plot for rendering and add any metadata (description/header)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Prescribed items per Primary Care Trust (PCT)"
    description = "Total number (sum) of prescribed items per PCT (Primary Care Trust) by PCT code."
    plot_data = {
        'graphJSON': graphJSON,
        'header': header,
        'description': description
    }
    return plot_data


@views.route('/home/', methods=['GET', 'POST'])
def search_list (q):
    users = User.query.get(q)
    if request.method == 'POST':        
        BNF_code = request.form['BNF code']
        BNF_name = request.form['BNF name']
        PNIC = request.form['NIC']
        ACT_cost = request.form['ACT Cost']
        db.session.add(PrescribingData)
        db.session.commit()
        flash ('Edited')
        return  redirect(url_for('dashboard'))
    return render_template('index.html', results=results, q=q)
# Shearch
#@views.route('/')
#def search_list():
    #q = request.args.get("q")
    #print (q)

    #if q:
       #results = PrescribingData.query.filter(PrescribingData.BNF_code.contains(q) | PrescribingData.BNF_name.contains(q)) 
   # else:
     #  results = []

   # return render_template("results/search.results.html", results=results)

# @views.route('/search/', methods=['GET', 'POST'])
# def search():
 # if request.method == 'POST':
       #  form = request.form
       #  search_value = form['search_string']
       #  search = "%{0}%".format(search_value)
       #  results = PrescribingData.query.filter(Database_(PrescribingData.BNF_code.like(search),PrescribingData.BNF_name.like(search))).all()
      #   return render_template('index.html' , search=results , legend="Search Result")
 # else:
        # return redirect('/')