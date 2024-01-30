from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
with open("best_movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
