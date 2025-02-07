"""
NAME:          models.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          22/11/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Database ORM class
"""

from app import db

class PrescribingData(db.Model):
    """class for the prescription data table."""
    __tablename__ = 'practice_level_prescribing'
    id = db.Column("ID", db.Integer, primary_key=True)
    SHA = db.Column("SHA", db.String(3))
    PCT = db.Column("PCT", db.String(3))
    practice = db.Column("PRACTICE", db.String(6))
    BNF_code = db.Column("BNFCODE", db.String(15))
    BNF_name = db.Column("BNFNAME", db.String(40))
    items = db.Column("ITEMS", db.Integer)
    NIC = db.Column("NIC", db.Float)
    ACT_cost = db.Column("ACTCOST", db.Float)
    quantity = db.Column("QUANTITY", db.Integer)

class PracticeData(db.Model):
    """Class for the practice address data table."""
    __tablename__ = 'practices'
    practice_code = db.Column("CODE", db.String(6), primary_key=True)
    practice_name = db.Column("PRACTICE", db.Text)
    address_line_1 = db.Column("ADDRESS1", db.Text)
    address_line_2 = db.Column("ADDRESS2", db.Text)
    city = db.Column("AREA", db.Text)
    county = db.Column("CITY", db.Text)
    post_code = db.Column("POSTCODE", db.String(10))



