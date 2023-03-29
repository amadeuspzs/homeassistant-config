import sys
from sqlalchemy import create_engine
import pandas as pd

def find_last_changed_index(df: pd.DataFrame) -> int:
    """Returns index of last changed value"""
    
    # only a single entry
    if len(df) == 1:
        last_index = 0
    # only a single value
    elif len(df.state.diff().bfill().unique()) == 1:
        last_index =  len(df) - 1
    # first value is different to second
    elif df.state[0] != df.state[1]:
        last_index = 0
    # find last value
    else:
        last_index = df[df.state.diff().bfill() != 0].dropna().index[0] - 1
    return last_index

# define your home assistant db location below:
db = "/home/homeassistant/.homeassistant/home-assistant_v2.db"

# how many restart events can we expect?
num_restarts = 100

# connect using SQLalchemy
try:
    engine = create_engine(f"sqlite:///{db}")
    conn = engine.connect()
except Exception as e:
    raise Exception(f"Could not connect to HA DB: {e}")

def hours_since_last_change(entity_id: str) -> float:

    # build the query
    query = f"""
    SELECT
        state,
        last_updated
    FROM states 
    WHERE 
        entity_id="{entity_id}" AND
        state !="unknown"
    ORDER BY last_updated DESC 
    LIMIT {num_restarts}
    """

    # execute the query and load into a pandas dataframe:
    try:
        df = pd.read_sql_query(query, conn)
        df.state = pd.to_numeric(df.state)
    except Exception as e:
        raise Exception(f"Failed to query HA DB: {e}")

    try:
        last_updated = pd.to_datetime(df.iloc[find_last_changed_index(df)].last_updated,utc=True)
        return (round((pd.Timedelta(pd.Timestamp.now(tz="utc") - last_updated))/pd.Timedelta('1 hour'),1))
    except Exception as e:
        raise Exception(f"Failed to find last state: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} sensor_name")
        exit(1)
    entity_id = sys.argv[1]
    print(hours_since_last_change(entity_id))
