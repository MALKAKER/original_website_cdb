
from flask import Flask,request,render_template,flash, redirect, url_for
#import try_sql
import sqlalchemy_query
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
import os.path
from flask_sqlalchemy import SQLAlchemy

from complex_declare import db
from complex_declare import Complex
session = db.session()

app=Flask(__name__)


#quit()













@app.route("/")
def start():
    return render_template('search.html')#('search.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST' : #post the  complex results to the web page
        theQuery=""
        protdata=[]
        listC=[]
        exception=""

       # pass the list of the results
        listC,exception,theQuery=sqlalchemy_query.search_results(request) #sending to search functions in class sqlalchemy_query

        i=0
        if(listC):
            for c in listC:
                i=i+1
                linkPA="http://www.rcsb.org/pdb/explore/explore.do?structureId="+c.pdb_prot_A[0:4]
                linkPB="http://www.rcsb.org/pdb/explore/explore.do?structureId="+c.pdb_prot_B[0:4]
                c.accession_prot_A=c.accession_prot_A.replace("-","")
                c.accession_prot_B=c.accession_prot_B.replace("-","")
                linkAccessionPA_1="http://www.uniprot.org/uniprot/"+c.accession_prot_A
                linkAccessionPA_2=""
                accA=[c.accession_prot_A,""]
                if c.accession_prot_A.find(",")!=-1:
                    accA=c.accession_prot_A.split(",")
                    if(accA[0]!=accA[1]):
                        linkAccessionPA_1="http://www.uniprot.org/uniprot/"+accA[0]
                        linkAccessionPA_2="http://www.uniprot.org/uniprot/"+accA[1]
                    else:
                        linkAccessionPA_1="http://www.uniprot.org/uniprot/"+accA[0]
                        accA[1]=""
                linkAccessionPB_1="http://www.uniprot.org/uniprot/"+c.accession_prot_B
                linkAccessionPB_2=""
                accB=[c.accession_prot_B,""]
                if c.accession_prot_B.find(",")!=-1:
                    accB=c.accession_prot_B.split(",")
                    if(accB[0]!=accB[1]):
                        linkAccessionPB_1="http://www.uniprot.org/uniprot/"+accB[0]
                        linkAccessionPB_2="http://www.uniprot.org/uniprot/"+accB[1]
                    else:
                        linkAccessionPB_1="http://www.uniprot.org/uniprot/"+accB[0]
                        accB[1]=""
               # a dictionary for the results table at the web html
                p={"pdb_entry":str(c.pdb_entry),"year_pub":str(c.year_pub),"resolution":str(c.resolution),
               "link":str(c.link),"pdb_prot_A":str(c.pdb_prot_A),"linkPA":str(linkPA),"linkAccessionPA_1":str(linkAccessionPA_1),
               "linkAccessionPA_2":str(linkAccessionPA_2),"name_prot_A":str(c.name_prot_A),"accession_prot_A_1":str(accA[0]),
               "accession_prot_A_2":str(accA[1]),"chain_prot_A":str(c.chain_prot_A),"length_protein_A":str(c.length_protein_A),
               "identity_prot_A":str(c.identity_prot_A),"scop_prot_A":str(c.scop_prot_A),"reso_prot_A":str(c.reso_prot_A),
               "year_pub_prot_A":str(c.year_pub_prot_A),"res_num_prot_A":str(c.res_num_prot_A),"pdb_prot_B":str(c.pdb_prot_B),
               "linkPB":str(linkPB),"linkAccessionPB_1":str(linkAccessionPB_1),"linkAccessionPB_2":str(linkAccessionPB_2),
               "name_prot_B":str(c.name_prot_B),"accession_prot_B_1":str(accB[0]),"accession_prot_B_2":str(accB[1]),"chain_prot_B":str(c.chain_prot_B),
               "length_protein_B":str(c.length_protein_B),"identity_prot_B":str(c.identity_prot_B),"scop_prot_B":str(c.scop_prot_B),
               "reso_prot_B":str(c.reso_prot_B),"year_pub_prot_B":str(c.year_pub_prot_B),"res_num_prot_B":str(c.res_num_prot_B)}
                protdata.append(p)
               #text for download:
                content = ""



               #text for download:

        return render_template("result.html",result = protdata,exception=exception,theQuery=theQuery,count=i)

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/citingUs")
def contactUs():
    return render_template('citingUs.html')

@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/intro")
def intro():
    return 'Hello, Worldi!'

if __name__=="__main__":
    app.run(debug=True)

