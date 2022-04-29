import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

# from schema_visualization import SchemaVizualization
# comando = "SELECT NAME AS 'Table_Name' FROM sqlite_master WHERE type = 'table'"
# a = SchemaVizualization("imdb.db")
# a.openConnectDB()
# a.tableList(comando)
# a.printTableSchema()

# from communCategories import CommunCategory
# command= '''SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type''' 
# a = CommunCategory("imdb.db", command)
# a.percentual()
# a.filterPercentual(5)
# a.piePlot()
# a.closeConnectDB()

# from moviesGenres import MoviesGenres
# command = '''SELECT genres, COUNT(*) FROM titles WHERE type = 'movie' GROUP BY genres''' 
# a = MoviesGenres("imdb.db", command)
# a.dataProcessing()
# a.barPlot()
# a.closeConnectDB()

# from ratingGenres import RatingGenres
# command = '''SELECT rating, genres FROM 
#             ratings JOIN titles ON ratings.title_id = titles.title_id 
#             WHERE premiered <= 2022 AND type = 'movie' '''   
# a = RatingGenres("imdb.db", command)
# a.dataProcessing()
# a.dropData("news", "genres")
# a.sortData('rating')
# a.barPlot()
# a.closeConnectDB()

# from ratingYear import RatingYear
# command = '''SELECT rating AS Rating, premiered FROM 
#             ratings JOIN titles ON ratings.title_id = titles.title_id 
#             WHERE premiered <= 2022 AND type = 'movie'
#             ORDER BY premiered''' 
# a = RatingYear("imdb.db", command)
# a.dataProcessing()
# a.plot()
# a.closeConnectDB()

# from ratingGenreYear import RatingGenreYear
# command = '''SELECT genres FROM titles ''' 
# a = RatingGenreYear("imdb.db", command)
# a.dataProcessing()
# a.plot()
# a.closeConnectDB()

# from durationGenre import DurationGenre
# command = '''SELECT AVG(runtime_minutes) Runtime, genres 
#             FROM titles 
#             WHERE type = 'movie'
#             AND runtime_minutes != 'NaN'
#             GROUP BY genres''' 
# a = DurationGenre("imdb.db", command)
# a.dataProcessing()
# a.plot()
# a.closeConnectDB()

# from moviesCountries import MoviesCountries
# command = '''SELECT region, COUNT(*) Number_of_movies FROM 
#             akas JOIN titles ON 
#             akas.title_id = titles.title_id
#             WHERE region != 'None'
#             AND type = \'movie\'
#             GROUP BY region''' 
# a = MoviesCountries("imdb.db", command)
# a.dataProcessing()
# a.barPlot()
# a.closeConnectDB()

# from bestMovies import BestMovies
# command = '''SELECT primary_title AS Movie_Name, genres, rating
#             FROM 
#             titles JOIN ratings
#             ON  titles.title_id = ratings.title_id
#             WHERE titles.type = 'movie' AND ratings.votes >= 25000
#             ORDER BY rating DESC
#             LIMIT 10'''
# a = BestMovies("imdb.db", command)


# from worstMovies import WorstMovies
# command = '''SELECT primary_title AS Movie_Name, genres, rating
#             FROM 
#             titles JOIN ratings
#             ON  titles.title_id = ratings.title_id
#             WHERE titles.type = 'movie' AND ratings.votes >= 25000
#             ORDER BY rating ASC
#             LIMIT 10''' 
# a = WorstMovies("imdb.db", command)
