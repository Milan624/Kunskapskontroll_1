import pandas as pd
import doctest

def replace_coffee_name(df):
    """
    Ersätter 'Hot Chocolate' med 'Cold Chocolate' i kolumnen 'coffee_name'.

    >>> df = pd.DataFrame({'coffee_name': ['Hot Chocolate', 'Latte', 'Hot Chocolate']})
    >>> replace_coffee_name(df)
    >>> df['coffee_name'].tolist()
    ['Cold Chocolate', 'Latte', 'Cold Chocolate']
    """
    df['coffee_name'] = df['coffee_name'].replace('Hot Chocolate', 'Cold Chocolate')

if __name__ == "__main__":
    result = doctest.testmod()
    print(result)