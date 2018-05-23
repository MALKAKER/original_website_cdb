from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="mam",
    password="aabbcc100",
    hostname="mam.mysql.pythonanywhere-services.com",
    databasename="mam$complex_database1",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 280
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
db = SQLAlchemy(app)


#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True)
#    email = db.Column(db.String(120), unique=True)

#    def __init__(self, username, email):
#        self.username = username
#        self.email = email

 #   def __repr__(self):
 #       return '<User %r>' % self.username

class Complex(db.Model):
  #  __tablename__ = 'complex'
    pdb_entry = db.Column(db.String(100), primary_key=True)
    year_pub=db.Column(db.Integer)
    chains = db.Column(db.String(100))
#    not yet implemented
    interface_area = db.Column(db.Integer)
    interface_area_seq = db.Column(db.String(100))
#    >>
    resolution=db.Column(db.Float(20))
    isAntiBody=db.Column(db.Boolean(20))
    link = db.Column(db.String(100))
    pdb_prot_A=db.Column(db.String(100))
    name_prot_A=db.Column(db.String(100))
    chain_prot_A=db.Column(db.String(100))
    length_protein_A = db.Column(db.Integer)
    scop_prot_A=db.Column(db.String(100))
    super_fam_A=db.Column(db.String(100))
    reso_prot_A=db.Column(db.Float(20))
    year_pub_prot_A = db.Column(db.Integer)
    accession_prot_A=db.Column(db.String(20))
    identity_prot_A=db.Column(db.Integer)
    seq_prot_A=db.Column(db.String(100))
    res_num_prot_A = db.Column(db.Integer)#   not yet implemented
    pdb_prot_B=db.Column(db.String(100))
    name_prot_B=db.Column(db.String(100))
    chain_prot_B=db.Column(db.String(100))
    length_protein_B = db.Column(db.Integer)
    scop_prot_B=db.Column(db.String(100))
    super_fam_B=db.Column(db.String(100))
    reso_prot_B=db.Column(db.Float(20))
    year_pub_prot_B = db.Column(db.Integer)
    accession_prot_B=db.Column(db.String(100))
    identity_prot_B=db.Column(db.Integer)
    seq_prot_B=db.Column(db.String(100))
    res_num_prot_B = db.Column(db.Integer)#   not yet implemented

    def __str__(self):
        s=str(self.pdb_entry[0:4])+"\t"+str(self.resolution)+"\t"+str(self.year_pub)+"\t"+str(self.pdb_prot_A[0:4])+"\t"+str(self.identity_prot_A)+"\t"+str(self.year_pub_prot_A)+"\t"+str(self.length_protein_A)+"\t"+str(self.reso_prot_A)+"\t"+str(self.pdb_prot_B[0:4])+"\t"+str(self.identity_prot_B)+"\t"+str(self.year_pub_prot_B)+"\t"+str(self.length_protein_B)+"\t"+str(self.reso_prot_B)
        return s


db.create_all()

#admin = User('admin', 'admin@example.com')
#guest = User('guest', 'guest@example.com')
#db.session.add(admin)
#db.session.add(guest)
#db.session.commit()
#users = User.query.all()
#print (users)