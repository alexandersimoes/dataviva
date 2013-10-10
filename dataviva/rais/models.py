from dataviva import db
from dataviva.utils import AutoSerialize
from dataviva.attrs.models import Bra, Isic, Cbo

from sqlalchemy import and_

############################################################
# ----------------------------------------------------------
# 2 variable tables
# 
############################################################

class Yi(db.Model, AutoSerialize):

    __tablename__ = 'rais_yi'
    year = db.Column(db.Integer(4), primary_key=True)
    isic_id = db.Column(db.String(5), db.ForeignKey(Isic.id), primary_key=True)
    wage = db.Column(db.Numeric(16,2))
    num_emp = db.Column(db.Integer())
    num_est = db.Column(db.Integer())
    unique_cbo = db.Column(db.Float())
    wage_growth_pct = db.Column(db.Float())
    wage_growth_pct_5 = db.Column(db.Float())
    wage_growth_val = db.Column(db.Numeric(16,2))
    wage_growth_val_5 = db.Column(db.Numeric(16,2))
    num_emp_growth_pct = db.Column(db.Float())
    num_emp_growth_pct_5 = db.Column(db.Float())
    num_emp_growth_val = db.Column(db.Integer())
    num_emp_growth_val_5 = db.Column(db.Integer())

    def __repr__(self):
        return '<Yi %d.%s>' % (self.year, self.isic_id)

class Yb_rais(db.Model, AutoSerialize):

    __tablename__ = 'rais_yb'
    year = db.Column(db.Integer(4), primary_key=True)
    bra_id = db.Column(db.String(8), db.ForeignKey(Bra.id), primary_key=True)
    wage = db.Column(db.Numeric(16,2))
    num_emp = db.Column(db.Integer())
    num_est = db.Column(db.Integer())
    unique_isic = db.Column(db.Float())
    unique_cbo = db.Column(db.Float())
    wage_growth_pct = db.Column(db.Float())
    wage_growth_pct_5 = db.Column(db.Float())
    wage_growth_val = db.Column(db.Numeric(16,2))
    wage_growth_val_5 = db.Column(db.Numeric(16,2))
    num_emp_growth_pct = db.Column(db.Float())
    num_emp_growth_pct_5 = db.Column(db.Float())
    num_emp_growth_val = db.Column(db.Integer())
    num_emp_growth_val_5 = db.Column(db.Integer())

    def __repr__(self):
        return '<Yb_rais %d.%s>' % (self.year, self.bra_id)

class Yo(db.Model, AutoSerialize):

    __tablename__ = 'rais_yo'
    year = db.Column(db.Integer(4), primary_key=True)
    cbo_id = db.Column(db.String(6), db.ForeignKey(Cbo.id), primary_key=True)
    wage = db.Column(db.Numeric(16,2))
    num_emp = db.Column(db.Integer())
    num_est = db.Column(db.Integer())
    unique_isic = db.Column(db.Float())
    wage_growth_pct = db.Column(db.Float())
    wage_growth_pct_5 = db.Column(db.Float())
    wage_growth_val = db.Column(db.Numeric(16,2))
    wage_growth_val_5 = db.Column(db.Numeric(16,2))
    num_emp_growth_pct = db.Column(db.Float())
    num_emp_growth_pct_5 = db.Column(db.Float())
    num_emp_growth_val = db.Column(db.Integer())
    num_emp_growth_val_5 = db.Column(db.Integer())

    def __repr__(self):
        return '<Yo %d.%s>' % (self.year, self.cbo_id)
        
############################################################
# ----------------------------------------------------------
# 3 variable tables
# 
############################################################

class Ybi(db.Model, AutoSerialize):
    
    __tablename__ = 'rais_ybi'
    year = db.Column(db.Integer(4), primary_key=True)
    bra_id = db.Column(db.String(8), db.ForeignKey(Bra.id), primary_key=True)
    isic_id = db.Column(db.String(5), db.ForeignKey(Isic.id), primary_key=True)
    wage = db.Column(db.Numeric(16,2))
    num_emp = db.Column(db.Integer())
    num_est = db.Column(db.Integer())
    rca = db.Column(db.Float())
    distance = db.Column(db.Float())
    opp_gain = db.Column(db.Float())
    wage_growth_pct = db.Column(db.Float())
    wage_growth_pct_5 = db.Column(db.Float())
    wage_growth_val = db.Column(db.Float())
    wage_growth_val_5 = db.Column(db.Float())
    num_emp_growth_pct = db.Column(db.Float())
    num_emp_growth_pct_5 = db.Column(db.Float())
    num_emp_growth_val = db.Column(db.Float())
    num_emp_growth_val_5 = db.Column(db.Float())
    
    def __repr__(self):
        return '<Ybi %d.%s.%s>' % (self.year, self.bra_id, self.isic_id)

class Ybo(db.Model, AutoSerialize):
    
    __tablename__ = 'rais_ybo'
    year = db.Column(db.Integer(4), primary_key=True)
    bra_id = db.Column(db.String(8), db.ForeignKey(Bra.id), primary_key=True)
    cbo_id = db.Column(db.String(6), db.ForeignKey(Cbo.id), primary_key=True)
    wage = db.Column(db.Numeric(16,2))
    num_emp = db.Column(db.Integer())
    num_est = db.Column(db.Integer())
    wage_growth_pct = db.Column(db.Float())
    wage_growth_pct_5 = db.Column(db.Float())
    wage_growth_val = db.Column(db.Float())
    wage_growth_val_5 = db.Column(db.Float())
    num_emp_growth_pct = db.Column(db.Float())
    num_emp_growth_pct_5 = db.Column(db.Float())
    num_emp_growth_val = db.Column(db.Float())
    num_emp_growth_val_5 = db.Column(db.Float())
    
    # oci = db.relationship("Yo",
    #         primaryjoin= "and_(Ybo.year==Yo.year, Ybo.cbo_id==Yo.cbo_id)",
    #         foreign_keys=[Yo.year, Yo.cbo_id], backref = 'Ybo')
    # 
    # def serialize(self):
    #     auto_serialized = super(Ybo, self).serialize()
    #     auto_serialized["oci"] = self.oci[0].oci
    #     return auto_serialized
    
    def __repr__(self):
        return '<Ybo %d.%s.%s>' % (self.year, self.bra_id, self.cbo_id)
    
class Yio(db.Model, AutoSerialize):
    
    __tablename__ = 'rais_yio'
    year = db.Column(db.Integer(4), primary_key=True)
    isic_id = db.Column(db.String(5), db.ForeignKey(Isic.id), primary_key=True)
    cbo_id = db.Column(db.String(6), db.ForeignKey(Cbo.id), primary_key=True)
    wage = db.Column(db.Numeric(16,2))
    num_emp = db.Column(db.Integer())
    num_est = db.Column(db.Integer())
    importance = db.Column(db.Float())
    wage_growth_pct = db.Column(db.Float())
    wage_growth_pct_5 = db.Column(db.Float())
    wage_growth_val = db.Column(db.Float())
    wage_growth_val_5 = db.Column(db.Float())
    num_emp_growth_pct = db.Column(db.Float())
    num_emp_growth_pct_5 = db.Column(db.Float())
    num_emp_growth_val = db.Column(db.Float())
    num_emp_growth_val_5 = db.Column(db.Float())
    
    def __repr__(self):
        return '<Yio %d.%s.%s>' % (self.year, self.isic_id, self.cbo_id)

class Ybio(db.Model, AutoSerialize):
    
    __tablename__ = 'rais_ybio'
    year = db.Column(db.Integer(4), primary_key=True)
    bra_id = db.Column(db.String(8), db.ForeignKey(Bra.id), primary_key=True)
    isic_id = db.Column(db.String(5), db.ForeignKey(Isic.id), primary_key=True)
    cbo_id = db.Column(db.String(6), db.ForeignKey(Cbo.id), primary_key=True)
    wage = db.Column(db.Float())
    num_emp = db.Column(db.Integer())
    num_est = db.Column(db.Integer())
    required = db.Column(db.Float())
    wage_growth_pct = db.Column(db.Float())
    wage_growth_pct_5 = db.Column(db.Float())
    wage_growth_val = db.Column(db.Float())
    wage_growth_val_5 = db.Column(db.Float())
    num_emp_growth_pct = db.Column(db.Float())
    num_emp_growth_pct_5 = db.Column(db.Float())
    num_emp_growth_val = db.Column(db.Float())
    num_emp_growth_val_5 = db.Column(db.Float())
    
    def __repr__(self):
        return '<Ybio %d.%s.%s.%s>' % (self.year, self.bra_id, self.isic_id, self.cbo_id)
