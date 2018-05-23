
from flask import Flask,request,render_template,flash, redirect, url_for
import try_sql
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
   return render_template('search.html')

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
       complex_pdb=(request.form['complex_pdb']).strip()
       com_year_from=request.form['complex_year_from']
       com_year_to=request.form['complex_year_to']
       name=request.form['prot_name'].strip()
       is_antibody=request.form['antibody']
       prot_pdb=request.form['prot_pdb'].strip()
       prot_access=request.form['prot_access'].strip()
       scop_family=request.form['scop']
       pro_year_from=request.form['prot_year_from']
       pro_year_to=request.form['prot_year_to']
       len_A_from=request.form['lengthA_from']
       len_A_to=request.form['lengthA_to']
       len_B_from=request.form['lengthB_from']
       len_B_to=request.form['lengthB_to']
       res_from=request.form['res_from']
       res_to=request.form['res_to']
       ident_from=request.form['ident_from']
       ident_to=request.form['ident_to']
       flag=False
       if(com_year_from=="" and com_year_to=="" and ident_from=="" and ident_to=="" and is_antibody=="no" and complex_pdb=="" and prot_pdb=="" and prot_access=="" and name=="" and scop_family==""  and pro_year_from=="" and pro_year_to=="" and len_A_from=="" and len_A_to=="" and len_B_from=="" and len_B_to=="" and res_from=="" and res_to==""):
           flash("please insert search fields")
           flag=True
       #technical varification
       if(com_year_from!=""):
           if(not com_year_from.isdigit()):
               flash("Invalid complex pub. year from value")
               flag=True
       if(com_year_to!=""):
           if(not com_year_to.isdigit()):
               flash("Invalid complex pub. year to value")
               flag=True
       if(pro_year_from!=""):
           if(not pro_year_from.isdigit()):
               flash("Invalid protein pub. year from value")
               flag=True
       if(pro_year_to!=""):
           if(not pro_year_to.isdigit()):
               flash("Invalid protein pub. year to value")
               flag=True
       if(len_A_from!=""):
           if(not len_A_from.isdigit()):
               flash("Invalid protein A from value")
               flag=True
       if(len_A_to!=""):
           if(not len_A_to.isdigit()):
               flash("Invalid protein A to value")
               flag=True
       if(len_B_from!=""):
           if(not len_B_from.isdigit()):
               flash("Invalid protein B from value")
               flag=True
       if(len_B_to!=""):
           if(not len_B_to.isdigit()):
               flash("Invalid protein B to value")
               flag=True
       if(res_from!=""):
           if(not res_from.replace('.','',1).isdigit()):
               flash("Invalid resolution from value")
               flag=True
       if(res_to!=""):
           if(not res_to.replace('.','',1).isdigit()):
               flash("Invalid resolution to value")
               flag=True
       if(ident_from!=""):
           if(not ident_from.isdigit()):
               flash("Invalid identity from value")
               flag=True
       if(ident_to!=""):
           if(not ident_to.isdigit()):
               flash("Invalid identity to value")
               flag=True

       if(flag==True): # if there was an error in the search
           return redirect(url_for('search'))

       # pass the list of the results
       listC,exception,theQuery=sqlalchemy_query.search_results(request) #sending to search functions in class sqlalchemy_query
       data=""
       i=0
       if(listC):
           path_=os.getcwd()
           os.chdir(path_+"\static") # to save the download file
           os.remove("complexes.txt") # delete the exist download file
           f = open("complexes.txt","w") # open new file to download
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
               content=content+"complex "+str(i)+"\n"
               content=content+"Complex: "
               content=content+"PDB- "+str(c.pdb_entry) +"; "
               content=content+"is antibody- "+str(c.isAntiBody) +"; "
               content=content+"chains- "+str(c.chains) +"; "
               content=content+"publish year- "+str(c.year_pub)+"; "
               content=content+"resolution- "+str(c.resolution)+"; "
               content=content+"Protein A: "
               content=content+"PDB- "+str(c.pdb_prot_A)+"; "
               content=content+"name- "+str(c.name_prot_A)+"; "
               content=content+"chain- "+str(c.chain_prot_A)+"; "
               content=content+"length- "+str(c.length_protein_A)+"; "
               content=content+"scop family- "+str(c.scop_prot_A)+"; "
               content=content+"scop super family- "+str(c.super_fam_A)+"; "
               content=content+"resolution- "+str(c.reso_prot_A)+"; "
               content=content+"publish year- "+str(c.year_pub_prot_A)+"; "
               content=content+"accession- "+str(c.accession_prot_A)+"; "
               content=content+"identity- "+str(c.identity_prot_A)+"; "
               content=content+"seq- "+str(c.seq_prot_A)+"\n"
               content=content+"Protein B: "
               content=content+"PDB- "+str(c.pdb_prot_B)+"; "
               content=content+"name- "+str(c.name_prot_B)+"; "
               content=content+"chain- "+str(c.chain_prot_B)+"; "
               content=content+"length- "+str(c.length_protein_B)+"; "
               content=content+"scop family- "+str(c.scop_prot_B)+"; "
               content=content+"scop super family- "+str(c.super_fam_B)+"; "
               content=content+"resolution- "+str(c.reso_prot_B)+"; "
               content=content+"publish year- "+str(c.year_pub_prot_B)+"; "
               content=content+"accession- "+str(c.accession_prot_B)+"; "
               content=content+"identity- "+str(c.identity_prot_B)+"; "
               content=content+"seq- "+str(c.seq_prot_B)+"\n"
               content=content+"\n\n"
               data=data+content
           f.write(data)
           f.close()
           os.chdir(path_)
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

if __name__=="__main__":
    app.run(debug=True)

