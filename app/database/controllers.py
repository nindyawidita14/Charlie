"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    
    def convert_tuple_list_to_raw(self, tuple_list):
        """Helper function to convert results from tuple list to plain list."""
        order_row = [tuple(row) for row in tuple_list]
        return  [item for i in order_row for item in i]
    
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.execute(db.select(func.sum(PrescribingData.items))).first()[0])
    
    def get_top_prescribed_item_with_percentage(self):
        """Get the top prescribed item and its percentage of all items."""
         # Query to get the top prescribed item
        top_item_query = db.session.query(
            PrescribingData.BNF_name,
            func.sum(PrescribingData.items).label('total_items')
        ).group_by(
            PrescribingData.BNF_name
        ).order_by(
            func.sum(PrescribingData.items).desc()
        ).limit(1).first()

        if top_item_query:
            top_item_name = top_item_query[0]
            top_item_count = top_item_query[1]

            # Query to get the total number of items
            total_items_query = db.session.query(
                func.sum(PrescribingData.items)
            ).scalar()

            # Calculate the percentage
            if total_items_query and total_items_query > 0:
                percentage = (top_item_count / total_items_query) * 100
            else:
                percentage = 0
            return {
                "top_item_name": top_item_name,
                "top_item_count": top_item_count,
                "percentage": round(percentage, 2)  # Round to 2 decimal places
            }
        
        else:
            return {
                "top_item_name": "N/A",
                "top_item_count": 0,
                "percentage": 0
            }
    
    def get_percentage_of_Anthelmintics(self):
        """Return the percentage of Anthelmintics in all infection drugs"""
        count_0505 = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('0505%'))
        ).scalar()

        total_count = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('05%')) 
        ).scalar()

        percentage = (count_0505 / total_count * 100) if total_count > 0 else 0

        return round(percentage, 2)
    
    def get_percentage_of_Antiprotozoal(self):
        """Return the percentage of Antiprotozoal in all infection drugs"""
        count_0504 = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('0504%'))
        ).scalar()

        total_count = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('05%')) 
        ).scalar()

        percentage = (count_0504 / total_count * 100) if total_count > 0 else 0

        return round(percentage, 2)
    
    def get_percentage_of_Antiviral(self):
        """Return the percentage of Antiviral in all infection drugs"""
        count_0503 = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('0503%'))
        ).scalar()

        total_count = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('05%')) 
        ).scalar()

        percentage = (count_0503 / total_count * 100) if total_count > 0 else 0

        return round(percentage, 2)
    
    def get_percentage_of_Antibacterials(self):
        """Return the percentage of Antibacterials in all infection drugs"""
        count_0501 = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('0501%'))
        ).scalar()

        total_count = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('05%')) 
        ).scalar()

        percentage = (count_0501 / total_count * 100) if total_count > 0 else 0

        return round(percentage, 2)
    
    def get_percentage_of_Antifungal(self):
        """Return the percentage of Antifungal in all infection drugs"""
        count_0502 = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('0502%'))
        ).scalar()

        total_count = db.session.execute(
            db.select(func.count(PrescribingData.BNF_code))
            .where(PrescribingData.BNF_code.like('05%')) 
        ).scalar()

        percentage = (count_0502 / total_count * 100) if total_count > 0 else 0

        return round(percentage, 2)
    
    def get_average_act_cost(self):
        """Return the average act cost of prescribed items"""
        return round(db.session.execute(db.select(func.avg(PrescribingData.ACT_cost))).first()[0],2)

    def get_total_act_cost(self):
        """Return the total act cost of prescribed items"""
        return round(db.session.execute(db.select(func.sum(PrescribingData.ACT_cost * PrescribingData.items))).first()[0],2)        
    
    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        result = db.session.execute(db.select(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT)).all()
        return self.convert_tuple_list_to_raw(result)
    
    def get_number_unique_items(self):
        """Get the number of unique items"""
        return db.session.execute(db.select(func.count(PrescribingData.items.distinct()).label('number_unique_item'))).first()[0]
    

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        result = db.session.execute(db.select(PrescribingData.PCT).distinct()).all()
        return self.convert_tuple_list_to_raw(result)

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()
    

    def get_antibiotics_data_for_selected_pct(self, pct):
        """Return the total number of prescribed antibiotics for each GP practice in a selected PCT."""
        results = db.session.query(
            PracticeData.practice_name,
            func.sum(PrescribingData.items).label('total_antibiotics')
        ).join(
            PrescribingData, PracticeData.practice_code == PrescribingData.practice
        ).filter(
            PrescribingData.PCT == pct,
            PrescribingData.BNF_code.like('0501%')  # 假设抗生素的BNF代码以'0501'开头
        ).group_by(
            PracticeData.practice_name
        ).all()
        
        labels = [row.practice_name for row in results]
        data = [row.total_antibiotics for row in results]
        
        return {
            'labels': labels,
            'data': data
        }