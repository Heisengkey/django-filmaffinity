from peliculas.models import Occupation, Category, Movie, User, Rating
from datetime import datetime

path = "data/"


def readOccupations():
    Occupation.objects.all().delete()

    occupations = []
    with open(path+"u.occupation", "r") as file:
        for line in file:
            if line == "\n":
                break
            occupation = Occupation(name=line.strip())
            occupation.save()
            occupations.append(occupation)
    return occupations


def readCategories():
    Category.objects.all().delete()

    categories = []
    with open(path+"u.genre", "r") as file:
        for line in file:
            if line == "\n":
                break
            category = Category(idCategory=int(line.split("|")[
                                1]), name=line.split("|")[0])
            category.save()
            categories.append(category)
    return categories


months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
          "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}


def readMovies():
    Movie.objects.all().delete()

    movies = []
    with open(path+"u.item", "r") as file:
        for line in file:
            if line == "\n":
                break
            date = line.split("|")[2]
            if date == "":  # Si no hay fecha, se pasa la de hoy
                # fecha = datetime.now()
                fecha = None
            else:
                fechaFormat = date.split('-')[0] + '-' + months[date.split('-')[1]] + '-' + date.split('-')[2]
                fecha = datetime.strptime(fechaFormat, '%d-%m-%Y')
            movie = Movie(idMovie=int(line.split("|")[0]), title=line.split(
                "|")[1], releaseDate=fecha, imdbUrl=line.split("|")[4])
            movie.save()
            movie.categories.set(Category.objects.filter(
                idCategory__in=line.split("|")[5:]))
            movies.append(movie)
    return movies


def readUsers():
    User.objects.all().delete()

    users = []
    with open(path+"u.user", "r") as file:
        for line in file:
            if line == "\n":
                break
            user = User(idUser=int(line.split("|")[0]), age=int(line.split("|")[1]), gender=line.split("|")[
                        2], occupation=Occupation.objects.get(name=line.split("|")[3]), zipCode=line.split("|")[4])
            user.save()
            users.append(user)
    return users


def readRatings():
    Rating.objects.all().delete()

    ratings = []
    with open(path+"u.data", "r") as file:
        for line in file:
            if line == "\n":
                break
            rating = Rating(idUser=User.objects.get(idUser=line.split("\t")[0]), idMovie=Movie.objects.get(
                idMovie=line.split("\t")[1]), rating=line.split("\t")[2], timestamp=datetime.fromtimestamp(int(line.split("\t")[3])))
            ratings.append(rating)
    Rating.objects.bulk_create(ratings)
    return ratings


def populate():
    print("Populating database...")
    occupations = readOccupations()
    print("Occupations read, " + str(len(occupations)) + " in total.")
    categories = readCategories()
    print("Categories read, " + str(len(categories)) + " in total.")
    movies = readMovies()
    print("Movies read, " + str(len(movies)) + " in total.")
    users = readUsers()
    print("Users read, " + str(len(users)) + " in total.")
    ratings = readRatings()
    print("Ratings read, " + str(len(ratings)) + " in total.")

    return "Datos cargados correctamente\n" + "Ocupaciones: " + str(len(occupations)) + " ; " + "Categorias: " + str(len(categories)) + " ; " + "Películas: " + str(len(movies)) + " ; " + "Usuarios: " + str(len(users)) + " ; " + "Puntuaciones: " + str(len(ratings)) + " ; "
