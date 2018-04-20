import json
import pandas as pd
def analysis(file,user_id):
    try:
        df = pd.read_json(file)
        minutes = df[df['user_id']==user_id].minutes.sum()
        times = df[df['user_id']==user_id].minutes.count()
        return times,minutes
    except:
        return 0,0
