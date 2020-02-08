from pymongo import MongoClient
import time
import datetime

class DatabaseConnection():

    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.review_store
        self.company_store = self.db.company_list
        self.posting_store = self.db.job_postings
        self.review_store = self.db.reviews

    def add_new_company(self, form):
        res = self.company_store.insert_one(form)

    def get_all_companies(self):
        res = self.company_store.find({})
        lis = []
        for x in res:
            temp = x
            temp['_id'] = str(x['_id'])
            lis.append(temp)
        return lis

    def add_new_posting(self, company_id, form):
        form['company_id'] = company_id
        res = self.posting_store.insert_one(form)

    def get_all_postings_for_company(self, company_id):
        res = self.posting_store.find({'company_id': company_id})
        print(res)
        lis = []
        for x in res:
            temp = x
            temp['_id'] = str(x['_id'])
            lis.append(temp)
        return lis

    def add_new_review(self, company_id, position_id, form):
        form['company_id'] = company_id
        form['position_id'] = position_id
        res = self.review_store.insert_one(form)

    def get_all_postings_for_company(self, company_id):
        res = self.review_store.find({'company_id': company_id})
        print(res)
                for x in res:
            temp = x
            temp['_id'] = str(x['_id'])
            lis.append(temp)
        return lis

    def get_all_postings_for_posting(self, position_id):
        res = self.review_store.find({'position_id': position_id})
                for x in res:
            temp = x
            temp['_id'] = str(x['_id'])
            lis.append(temp)
        return lis