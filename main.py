import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")


# command = '''SELECT genres, COUNT(*) FROM titles WHERE type = 'movie' GROUP BY genres'''

# from handle_db import HandleDB
# a = HandleDB("imdb.db")
# a.openConnectDB()
# a.callTable(command)
# a.closeConnectDB()

# from moreCommunCategories import MoreCommunCategory
# command= '''SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type''' 
# a = MoreCommunCategory("imdb.db", command)
# a.percentual()
# a.filterPercentual(5)
# a.piePlot()
# a.closeConnectDB()

# from moviesPerGenres import MoviesPerGenres
# command = '''SELECT genres, COUNT(*) FROM titles WHERE type = 'movie' GROUP BY genres''' 
# a = MoviesPerGenres("imdb.db", command)
# a.dataProcessing()
# a.barPlot()
# a.closeConnectDB()

# from ratingFilmsByGenre import RatingFilmsByGenre
# command = '''SELECT rating, genres FROM 
#             ratings JOIN titles ON ratings.title_id = titles.title_id 
#             WHERE premiered <= 2022 AND type = 'movie' '''   
# a = RatingFilmsByGenre("imdb.db", command)
# a.dataProcessing()
# a.dropData("news", "genres")
# a.sortData('rating')
# a.barPlot()
# a.closeConnectDB()

# from ratingMoviesPremiereYear import RatingMoviesPremiereYear
# command = '''
#             SELECT rating AS Rating, premiered FROM 
#             ratings JOIN titles ON ratings.title_id = titles.title_id 
#             WHERE premiered <= 2022 AND type = 'movie'
#             ORDER BY premiered
#             ''' 
# a = RatingMoviesPremiereYear("imdb.db", command)
# a.dataProcessing()
# a.plot()
# a.closeConnectDB()

# from ratingMoviesByGenreByYear import RatingMoviesByGenreByYear
# command = '''SELECT genres FROM titles ''' 

# a = RatingMoviesByGenreByYear("imdb.db", command)
# a.dataProcessing()

# a.plot()
# a.closeConnectDB()

# from relationDurationGenre import RelationDurationGenre
# command = '''
#             SELECT AVG(runtime_minutes) Runtime, genres 
#             FROM titles 
#             WHERE type = 'movie'
#             AND runtime_minutes != 'NaN'
#             GROUP BY genres
#             '''  

# a = RelationDurationGenre("imdb.db", command)
# a.dataProcessing()

# a.plot()
# a.closeConnectDB()

# from moviesCountry import MoviesCountry
# command = '''
#             SELECT region, COUNT(*) Number_of_movies FROM 
#             akas JOIN titles ON 
#             akas.title_id = titles.title_id
#             WHERE region != 'None'
#             AND type = \'movie\'
#             GROUP BY region
#             ''' 

# a = MoviesCountry("imdb.db", command)
# a.dataProcessing()

# a.barPlot()
# a.closeConnectDB()

from bestMovies import BestMovies
command = '''
            SELECT primary_title AS Movie_Name, genres, rating
            FROM 
            titles JOIN ratings
            ON  titles.title_id = ratings.title_id
            WHERE titles.type = 'movie' AND ratings.votes >= 25000
            ORDER BY rating DESC
            LIMIT 10          
            '''

a = BestMovies("imdb.db", command)


from worstMovies import WorstMovies
command = '''
            SELECT primary_title AS Movie_Name, genres, rating
            FROM 
            titles JOIN ratings
            ON  titles.title_id = ratings.title_id
            WHERE titles.type = 'movie' AND ratings.votes >= 25000
            ORDER BY rating ASC
            LIMIT 10
            ''' 

a = WorstMovies("imdb.db", command)
