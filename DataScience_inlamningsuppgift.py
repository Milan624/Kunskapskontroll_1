import pandas as pd
import sqlite3

import logging
logger = logging.getLogger()

logging.basicConfig(
    filename=r'C:\Users\milan\Documents\TUC\logfile.log',
    format='[%(asctime)s][%(levelname)s] %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger.debug('This is a debug-level log record.')
logger.info('This is an info-level log record.')
logger.warning('I have a bad feeling about this...')

con = sqlite3.connect(r'C:\Users\milan\Documents\TUC\Data_science\coffe.db')
df = pd.read_csv(r"C:\Users\milan\Documents\TUC\Data_science\index.csv")
df.groupby("coffee_name")["money"].agg(sum)
df
latte_df = df[df['coffee_name'] == 'Latte']
print(latte_df)
df['coffee_name'] = df['coffee_name'].replace('Hot Chocolate', 'Cold Chocolate')
print(df['coffee_name'].unique())
df

def replace_coffee_name(df):
    """
    >>> df = pd.DataFrame({'coffee_name': ['Hot Chocolate', 'Latte', 'Hot Chocolate']})
    >>> replace_coffee_name(df)
    >>> df['coffee_name'].tolist()
    ['Cold Chocolate', 'Latte', 'Cold Chocolate']
    """
    df['coffee_name'] = df['coffee_name'].replace('Hot Chocolate', 'Cold Chocolate')
    
    df
    
    

df.to_sql("kaffetabellen", con, if_exists="replace")