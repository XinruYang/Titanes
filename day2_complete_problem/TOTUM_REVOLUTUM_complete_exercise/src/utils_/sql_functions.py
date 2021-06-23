import json
import os, sys
from sqlalchemy import create_engine
import pandas as pd 


dir = os.path.dirname

path1 = dir(dir(os.path.abspath(__file__)))
sys.path.append(path1)


def load_sql():

    querry = """
        SELECT fire_id, latitude, longitude, scan, track, acq_date, acq_time, frp, fire_type
        FROM australia_fires.fire_archive_M6_96619
        UNION ALL
        SELECT fire_id, latitude, longitude, scan, track, acq_date, acq_time, frp, fire_type 
        FROM australia_fires.fire_archive_V1_96617
        """
    with open(dir(path1) + os.sep + 'config' + os.sep + 'bd_info.json') as json_file:
        db_conf = json.load(json_file)

    engine = create_engine('mysql+pymysql://' + db_conf['USER'] + ':' + db_conf['PASSWORD'] + '@' + db_conf['IP_DNS'] + ':' + str(db_conf['PORT'])+ '/' + db_conf['BD_NAME'])
    con = engine.connect()
    df = pd.read_sql_query(querry, con=con)
    return df
    