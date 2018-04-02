#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
def get_rank(user_id):
    client = MongoClient('127.0.0.1',27017)
    db = client.shiyanlou
    contests = db.contests
    userdata = list(contests.aggregate([{'$match':{'user_id':user_id}},{'$group' : {'_id' : user_id, 'score' : {'$sum' : "$score"}, 'time' : {'$sum' : "$submit_time"}}}]))
    if len(userdata) == 0:
        return 0,0,0
    data = userdata[0]
    userdata = list(contests.aggregate([{'$group':{'_id':'$user_id','score':{'$sum':'$score'},'time':{'$sum':'$submit_time'}}},{'$match':{'$or':[{'score':{'$gt':data['score']}},{'time':{'$lt':data['time']},'score':data['score']}]}},{'$group':{'_id':None,'count':{'$sum':1}}}]))
    if len(userdata) > 0 :
        rank = userdata[0]['count']+1
    else:
        rank = 1
    score = data['score']
    submit_time = data['time']
    return rank, score, submit_time

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Parameter error.")
        sys.exit()
    user_id = sys.argv[1]
    userdata = get_rank(int(user_id))
    print(userdata)
