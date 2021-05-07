#define needed functions here
#function that creates transition matrice
def transition_matrice(data, location, customer_key):
    """
    Takes in a matrice with full list of transitions and format:
    data.index.type() = DATETIME

    input:
    data = a Pandas DataFrame
    location = Columnname in data that contains the locations
    customer_key = Columnname in data that contains customer key 
    
    returns:
    transition matrice.

    requirements:
    pandas imported
    """
    #check for correct data type
    try:
        if type(data) != pandas.core.frame.DataFrame:
            raise ValueError("This function requires a pandas DataFrame as input")
    except:
        if type(data) != pd.core.frame.DataFrame:
            raise ValueError("This function requires a pandas DataFrame as input")

    #check for correct index
    try:
        if type(data.index) != pandas.core.indexes.datetimes.DatetimeIndex:
            raise ValueError("This function requires a pandas DatetimeIndex as index")
    except:
        if type(data.index) != pd.core.indexes.datetimes.DatetimeIndex:
            raise ValueError("This function requires a pandas DatetimeIndex as index")
    
    #
    
    #iterate over all transitions for all customers
    data.groupby(customer_key)
    