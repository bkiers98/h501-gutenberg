import pandas as pd
import numpy as np
from tt_gutenberg.transform import get_data


def list_authors(by_languages=True, alias=True):
    '''
    This function returns a list of author aliases sorted by the number
    of translations associated with that alias. 
    '''
    df_author_translations = get_data()
    print(df_author_translations.info())
    df_aliases = df_author_translations.groupby('author_alias') \
                                        [['language']] \
                                        .count() \
                                        .reset_index() \
                                        .rename(
                                            {'language' : 'total_languages'}
                                            )

    print(df_aliases)
    
    alias_list = df_aliases.sort_values(by='total_languages', ascending=False) \
                                        ['author_alias'] \
                                        .to_list()
    return alias_list
    