"""
This script is responsible for linking the application frontend built in html with the blockchain services simulation script.  
Created by Mauro Cardoso, 27 of April 2022, 01:55
"""

from backend import write_block_sc_raw_material, write_block_sc_pharma,\
    write_block_regulator, write_block_warehouse, write_block_distribuitor, check_integrity, genesis_block
from flask import Flask, render_template, request, redirect

app = Flask(__name__) # instance of the flask class

@app.route('/', methods=['POST','GET']) #Handler of the url request   
def index():
    if request.method == 'POST':
        pass
    return render_template('index.html')

@app.route('/raw_manufacturer', methods=['POST','GET']) #Handler of the url request   
def raw_manufacturer():
    if request.method == 'POST':
        genesis_block()   
        raw_Contracted = request.form.get('raw_Contracted')
        raw_Contractor = request.form.get('raw_Contractor')
        raw_Amount = request.form.get('raw_Amount')    
        write_block_sc_raw_material(raw_contracted = raw_Contracted, raw_contractor = raw_Contractor, raw_amount = raw_Amount)

    return render_template('index.html')

@app.route('/pharma_manufacturer', methods=['POST','GET']) #Handler of the url request   
def pharma_manufacturer():
    if request.method == 'POST':
        genesis_block()
        ph_Quantity = request.form.get('ph_Quantity')
        ph_Drug = request.form.get('ph_Drug')
        write_block_sc_pharma(ph_quantity = ph_Quantity, ph_drug = ph_Drug)   
    return render_template('index.html')

@app.route('/regulator', methods=['POST','GET']) #Handler of the url request   
def regulator():
    if request.method == 'POST':
        genesis_block()
        r_Requester = request.form.get('r_Requester')
        r_Regulator = request.form.get('r_Regulator')
        r_Validation = request.form.get('r_Validation')
        write_block_regulator(r_requester = r_Requester, r_regulator = r_Regulator, r_validation = r_Validation)
    return render_template('index.html')

@app.route('/warehouse', methods=['POST','GET']) #Handler of the url request   
def warehouse():
    if request.method == 'POST':
        genesis_block()
        wr_Contracted = request.form.get('wr_Contracted')
        wr_Contractor = request.form.get('wr_Contractor')
        wr_Amount = request.form.get('wr_Amount')
        wr_Drug = request.form.get('wr_Drug')
        write_block_warehouse(wr_contracted = wr_Contracted, wr_contractor = wr_Contractor, wr_amount = wr_Amount, wr_drug = wr_Drug)
    return render_template('index.html')

@app.route('/distribuitor', methods=['POST','GET']) #Handler of the url request   
def distribuitor():
    if request.method == 'POST':
        genesis_block()
        dr_Sender = request.form.get('dr_Sender')
        dr_Receiver = request.form.get('dr_Receiver')
        dr_Amount = request.form.get('dr_Amount')
        dr_Address = request.form.get('dr_Address')
        write_block_distribuitor(dr_sender = dr_Sender, dr_receiver = dr_Receiver, dr_amount = dr_Amount, dr_address = dr_Address)
    return render_template('index.html')


@app.route('/checking') #Handler of the url request   
def check():
    results = check_integrity()
    return render_template('index.html', checking_results = results)
    
if __name__ == '__main__':
    app.run(debug=True) # Entrance of the app
    # dev server in terminal -> python project name
