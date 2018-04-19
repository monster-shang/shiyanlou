import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_json('user_study.json')
def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(df[['user_id','minutes']].groupby('user_id').sum())
    fig.show()
