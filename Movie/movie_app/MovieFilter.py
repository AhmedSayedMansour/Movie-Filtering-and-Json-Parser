import pandas as pd
import zipfile

class MovieFilter():
    """Class MovieFilter to handle reading the csv from the zip file and search"""

    def __init__(self, path):
        """Extract the file and create dataframe"""
        zf = zipfile.ZipFile(path)
        df = pd.read_csv(zf.open(zf.namelist()[0]), index_col = 0)
        self.df = df

    def search(self, title=None, release_date=None, overview=None, popularity=None, vote_average=None, vote_count=None):
        """search for a specific movie"""

        filteredRows = []
        if title is not None:
            ls = list(self.df[self.df['title']==title].index)
            if len(ls) == 0:
                return []
            if len(filteredRows) == 0:
                filteredRows = ls
            else :
                filteredRows = list(set(ls).intersection(set(filteredRows)))

        if release_date is not None:
            ls = list(self.df[self.df['release_date']==release_date].index)
            if len(ls) == 0:
                return []
            if len(filteredRows) == 0:
                filteredRows = ls
            else :
                filteredRows = list(set(ls).intersection(set(filteredRows)))

        if overview is not None:
            ls = list(self.df[self.df['overview'].astype(str).str.contains(overview)].index)
            if len(ls) == 0:
                return []
            if len(filteredRows) == 0:
                filteredRows = ls
            else :
                filteredRows = list(set(ls).intersection(set(filteredRows)))

        if popularity is not None:
            ls = list(self.df[self.df['popularity']==popularity].index)
            if len(ls) == 0:
                return []
            if len(filteredRows) == 0:
                filteredRows = ls
            else :
                filteredRows = list(set(ls).intersection(set(filteredRows)))

        if vote_average is not None:
            ls = list(self.df[self.df['vote_average']==vote_average].index)
            if len(ls) == 0:
                return []
            if len(filteredRows) == 0:
                filteredRows = ls
            else :
                filteredRows = list(set(ls).intersection(set(filteredRows)))

        if vote_count is not None:
            ls = list(self.df[self.df['vote_count']==vote_count].index)
            if len(ls) == 0:
                return []
            if len(filteredRows) == 0:
                filteredRows = ls
            else :
                filteredRows = list(set(ls).intersection(set(filteredRows)))

        return filteredRows

    def get_full_rows(self, rows):
        """Return full rows from the data frame with the rows numbers"""

        return self.df.loc[rows, :]
