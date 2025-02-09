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
from flask import Blueprint, render_template, request, Response
from app.database.controllers import Database
from reportlab.pdfgen import canvas
from app import app

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = db_mod.get_distinct_pcts()
    selected_pct_1 = pcts[0]  # 默认选择第一个PCT
    selected_pct_2 = pcts[0]
    selected_pct_data = db_mod.get_n_data_for_PCT(str(selected_pct_1), 5)
    barchart_data = get_barchart_data(str(selected_pct_2))

    if request.method == 'POST':
        form = request.form
        form_id = form.get('form-id')

        if form_id == 'form1':
            # 处理表单1的数据
            selected_pct_1 = form.get('pct-option', pcts[0])
            selected_pct_data = db_mod.get_n_data_for_PCT(str(selected_pct_1), 5)
        elif form_id == 'form2':
            # 处理表单2的数据
            selected_pct_2 = form.get('pct-option', pcts[0])
            barchart_data = get_barchart_data(str(selected_pct_2))

    # prepare data structure to send to front end to update display
    dashboard_data = {    
        "tile_data_items": generate_data_for_tiles(),  
        "top_items_plot_data": generate_top_px_items_barchart_data(),
        "pct_list": pcts,
        "pct_data": selected_pct_data,
        "search_value": search_list,
        "percentage_card_data": generate_data_for_card(),
        "barchart_data": {
            "antibiotics_data": {
                "labels": json.dumps(barchart_data['antibiotics_data']['labels']),
                "data": json.dumps(barchart_data['antibiotics_data']['data'])
            }
        }
    }

    db_mod.get_average_act_cost()
    db_mod.get_total_act_cost()

    print(dashboard_data)  # 调试输出
    
    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html',dashboard_data=dashboard_data)


def generate_data_for_tiles():
    """Generate the data for the four home page tiles."""

    # Get the top prescribed item and its percentage
    top_item_data = db_mod.get_top_prescribed_item_with_percentage()
    tile_data = {
        "total_items": db_mod.get_total_number_items(),
        "avg_act_cost": db_mod.get_average_act_cost(),
        "total_act_cost": db_mod.get_total_act_cost(),
        "top_px_item": top_item_data["top_item_name"],
        "top_px_item_count": top_item_data["top_item_count"],
        "top_px_item_percentage": top_item_data["percentage"],
        "num_unique_items": db_mod.get_number_unique_items()
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

def get_barchart_data(selected_pct):
    """Render the view page of the dashboard passing in data to populate dashboard."""  

    antibiotics_data = db_mod.get_antibiotics_data_for_selected_pct(selected_pct)
    
    barchart_data = {
        'pct_list': selected_pct,
        'antibiotics_data': antibiotics_data,
        # 其他数据
    }
    
    return barchart_data

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

@app.route('/generate_report', methods=['GET'])
def generate_report():
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer)
    
    c.drawString(100, 750, "Dashboard Report")
    c.drawString(100, 730, "This is a sample report for the dashboard.")
    
    c.showPage()
    c.save()

    pdf_buffer.seek(0)
    return Response(pdf_buffer, mimetype='application/pdf',
                    headers={'Content-Disposition': 'inline; filename=dashboard_report.pdf'})

  
def generate_data_for_card():
    """Generate data for the percentage card"""
    card_data = {
        "Antibacterials": db_mod.get_percentage_of_Antibacterials(),
        "Antifungal": db_mod.get_percentage_of_Antifungal(),
        "Antiviral": db_mod.get_percentage_of_Antiviral(),
        "Antiprotozoal": db_mod.get_percentage_of_Antiprotozoal(),
        "Anthelmintics": db_mod.get_percentage_of_Anthelmintics(),
    }
    return card_data
