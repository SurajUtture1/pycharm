class movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('movie name:', self.title)
        print('hero:', self.hero)
        print('heroine name:', self.heroine)


List_of_movies = []
while True:
    title = input('Enter movie name:')
    hero = input('Enter hero name:')
    heroine = input('Enter heroine :')
    m = movie(title, hero, heroine)
    List_of_movies.append(m)
    print('movie added to list successfully')
    option = input('Do you want to add one more movie [Yes|No] :')
    if option.lower() == 'no':
        break
print('All movies information')
print('#' * 40)
for movie in List_of_movies:
    movie.info()
