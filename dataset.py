import pandas as pd
import math
stops = pd.read_csv(".\\stops.txt")
stop_times = pd.read_csv(".\\stop_times.txt")

stops = stops.loc[:, ['stop_id', 'stop_name']]
stop_times = stop_times.loc[:, ['trip_id', 'arrival_time', 'stop_id', 'stop_sequence']]
mydata = stops.merge(stop_times, on='stop_id', how='inner', suffixes=('_1', '_2'))
mydata = mydata.sort_values(by=['trip_id',"stop_sequence"], ignore_index=True)

mydata["stop_sequence"] = mydata["stop_sequence"].astype(int)
mydata['arrival_time'] = mydata['arrival_time'].apply(lambda time: time if not (t:= int(time[:2]) >= 24) else str(t%24) + time[2:])
mydata["arrival_time"] = pd.to_datetime(mydata["arrival_time"], format="%H:%M:%S")

time_deltas = []
for index, row in mydata.iterrows():
    print(index)
    if row["stop_sequence"] == 1:
        time_deltas.append(pd.Timedelta(0).total_seconds())
    else:
        d = mydata.iloc[index - 1]
        g = row["arrival_time"] - d["arrival_time"]
        time_deltas.append(g.total_seconds())


mydata.insert(5, "time_delta", time_deltas)

mydata.to_csv('mydata.csv')