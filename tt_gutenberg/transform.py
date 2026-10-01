import pandas as pd

DATA = {'df_authors': pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv'), \
        'df_metadata': pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')}

def get_data():
    '''
    This function fetches the two DataFrames and merges them on a
    common axis, returning the merged DataFrame
    '''
    df_metadata = DATA['df_metadata']
    df_authors = DATA['df_authors']
    df_author_works = pd.merge(df_metadata, df_authors, \
                                on='gutenberg_author_id', \
                                how='left')
    df_author_works.rename(columns={'alias': 'author_alias'}, \
                                    inplace=True)

    return df_author_works
