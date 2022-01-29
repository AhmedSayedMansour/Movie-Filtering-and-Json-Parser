import pandas as pd
import zipfile
import sys


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


"""
filter = MovieFilter('Movie-Dataset-Latest (1).zip')

#test 1
rows = filter.search(title = None, release_date=None, overview="love", popularity=None, vote_average=8.7, vote_count=None)
filter.get_full_rows(rows)

#test 2
rows = filter.search(title = None, release_date=None, overview="blood", popularity=None, vote_average=5.0, vote_count=None)
filter.get_full_rows(rows)

#test 3
rows = filter.search(title = 'My Brother Chases Dinosaurs', release_date=None, overview="love", popularity=None, vote_average=7.0, vote_count=None)
filter.get_full_rows(rows)

#test 4
rows = filter.search(title = "The Shawshank Redemption", release_date=None, overview="love", popularity=None, vote_average=8.7, vote_count=None)
filter.get_full_rows(rows)

#test 5
rows = filter.search(title = None, release_date='9/23/1994', overview=None , popularity=None, vote_average=None, vote_count=None)
filter.get_full_rows(rows)
"""

if __name__ == "__main__":
    try:
        print('reading from : ', sys.argv[1])
        filter = MovieFilter(sys.argv[1])
        print('write all inputs of the filter if you do not what to use this parameter press enter')
        title = input('title : ')
        if title == '':
            title = None
        release_date = input('release_date : ')
        if release_date == '':
            release_date = None
        overview = input('overview : ')
        if overview == '':
            overview = None
        popularity = input('popularity : ')
        if popularity == '':
            popularity = None
        else:
            popularity = float(popularity)
        vote_average = input('vote_average : ')
        if vote_average == '':
            vote_average = None
        else:
            vote_average = float(vote_average)
        vote_count = input('vote_count : ')
        if vote_count == '':
            vote_count = None
        else:
            vote_count = float(vote_count)
        rows = filter.search(title = title, release_date=release_date, overview=overview, popularity=popularity, vote_average=vote_average, vote_count=vote_count)
        print('Filtered rows are : ', rows)
        new_df = filter.get_full_rows(rows)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(new_df)
    except:
        print('Error occured...')