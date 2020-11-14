import os
from flask import Flask, render_template, flash, request, url_for, redirect
from werkzeug.utils import secure_filename
import search_document as sd

UPLOAD_FOLDER = '/uploadFiles'
ALLOWED_EXTENSIONS = {'txt','pdf'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

setupData = sd.setup()

@app.route('/') #good
def mainPage():
    return render_template('mainpage.html')

@app.route('/Perihal') #good
def perihal():
    return render_template('perihal.html')

@app.route('/Upload', methods = ['GET','POST']) #masih bad
def uploadPage():
    return ("ini page buat upload")

@app.route('/Search/<query>', methods = ['GET', 'POST'])
def searchPage(query):
    global setupData
    setupData = sd.updateMaster(setupData)
    q, workingTerm, sim, indices = sd.search(query, setupData)
    flist, search_size, titles, openings, docs, masterTerm, lenMaster, masterCount = setupData
    
    html = "<!DOCTYPE html> \n <html> \n "
    html += "<head> \n <title>AID Search!</title> \n"
    html += "<link href=\"{{ url_for('static', filename='style.css') }}\" type=\"text/css\" rel=\"stylesheet\"> \n </head> \n"
    html += "<body> \n <a style=\"text-decoration: none\" href=\"./\"><h2>AID <span class=\"Searchy\">Search!</span></h2></a>"
    html += "<div class=\"listDoc\" id=\"listdoc\"> \n"
    html += "<h3> Daftar Dokumen </h3> \n <ul> \n"
    
    for filename in flist:
        html += "<li> "+str(filename)[5:]+"</li> \n"
    
    html += "</ul> \n </div> \n"
    html += "<div class=\"searchRes\" id=\"searchres\"> \n"
    html += "<h3> Hasil Pencarian: </h3> <p> (diurutkan dari tingkat kemiripan tertinggi) </p> \n <ol> \n"
    
    for i in range(search_size):
        html += "<li> <b>"+titles[indices[i]]+"</b><br/> \n"
        html += "Jumlah kata: "+str(len(docs[indices[i]+1]))+"<br/> \n"
        html += "Tingkat kemiripan: "+str(int(10000*sim[i])/100)+"%"+"<br/> \n"
        html += openings[indices[i]]+"<br/> \n </li> \n"
    
    html += "</ol> \n </div> \n"
    html += "<div class=\"matrix\" id=\"matrix\"> \n"
    html += "<table> \n"
    html += "<tr> \n <th>Term</th> \n <th>Query</th> \n"
    
    for i in range(search_size):
        html += "<th>D"+str(i+1)+"</th> \n"
    html += "</tr> \n"
    
    for i in range(len(q)):
        html += "<tr> \n <td>"+q[i]+"</td>"
        for j in range(search_size+1):
            html += "<td>"+str(workingTerm[j][i])+"</td> \n"
        html += "</tr> \n"
    
    html += "</table> \n </div> \n"
    html += "<footer class=\"perihal\"> \n"
    html += "<a style=\"color:black ; text-decoration: none\" href=\"./Perihal\"> \n"
    html += "<h3>Perihal AID</h3> \n </a> \n </footer> \n"
    html += "</body> \n </html>"
    
    return html
    

if __name__ == '__main__':
    app.run()
