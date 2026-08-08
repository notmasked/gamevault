import pandas as pd
from random import randint

df = pd.read_csv('data/games_data_10k.csv', index_col="Name", keep_default_na=False)

def main():
    print("===========================")
    print("=====--- GameVault ---=====")
    print("===========================")
    while True:
        print("1. Search game\n2. Top Rated games\n3. Browse by genre\n4. Browse by year\n5. Random game\n6. Exit")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Please enter a number.")
            continue
        match choice:
            case 1:
                search_game()
            case 2:
                top_rated_games()
            case 3:
                browse_genre()
            case 4:
                browse_year()
            case 5:
                random_game()
            case 6:
                print("Closing GameVault...")
                exit()
            case _:
                print("Please enter a valid option.")
                continue

def search_game():
    while True:
        print("============")
        print("=- Search -=")
        print("============")

        query = input("Enter name: ")

        result = df[df.index.str.contains(query, case=False, na=False)]

        if result.empty:
            print("No games found.")
        else:
            print("=============================")
            print(result)
            print("=============================")

        print("1. Search again")
        print("2. Back")

        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            continue    
        elif choice == 2:
            print("===========================")
            print("=====--- GameVault ---=====")
            print("===========================")
            return       
        else:
            print("Please enter a valid option.")

loaded = 0
def top_rated_games():
    global loaded
    def load_games():
        global loaded
        n = loaded
        loaded += 26
        return sorted_games[n:(n+26)]

    print("=========================")
    print("===- Top Rated Games -===")
    print("=========================")
    sorted_games = df.sort_values(by="Rating", ascending=False)[1:]
    print(load_games())
    while True:
        print("=========================")
        print("1. Load More\n2. Back")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Please enter a number.")
            continue
        match choice:
            case 1:
                print(load_games())
                continue
            case 2:
                loaded = 0
                print("===========================")
                print("=====--- GameVault ---=====")
                print("===========================")
                return
            case _:
                print("Please enter a valid option.")
                continue

def browse_genre():
    global loaded
    def load_genre(genre):
        global loaded
        n = loaded
        loaded += 26
        if df[df["Genre"] == genre][n:(n+26)].empty:
            return "Thats all!"
        else:
            return df[df["Genre"] == genre][n:(n+26)]

    def genre_func(gen):
        global loaded
        print("==================================")
        print(load_genre(gen))
        while True:
            print("==================================")
            print("1. Load more\n2. Back")
            try:
                choice1 = int(input("Enter: "))
            except ValueError:
                print("==================================")
                print("Please enter a number.")
                continue
            match choice1:
                case 1:
                    print("==================================")
                    print(load_genre(gen))
                    continue
                case 2:
                    print("==================================")
                    loaded = 0
                    break
                case _:
                    print("==================================")
                    print("Please select a valid option.")
                    continue

    print("=========================")
    print("==-- Browse By Genre --==")
    print("=========================")
    while True:
        print("1. Action\n2. Adventure\n3. Casual\n4. Indie\n5. Massively Multiplayer\n6. RPG\n7. Racing\n8. Simulation\n9. Sports\n10. Strategy\n11. Back")
        print("=========================")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("=========================")
            print("Please enter a number.")
            continue
        match choice:
            case 1:
                genre_func("Action")
            case 2:
                genre_func("Adventure")
            case 3:
                genre_func("Casual")
            case 4:
                genre_func("Indie")
            case 5:
                genre_func("Massively Multiplayer")
            case 6:
                genre_func("RPG")
            case 7:
                genre_func("Racing")
            case 8:
                genre_func("Simulation")
            case 9:
                genre_func("Sports")
            case 10:
                genre_func("Strategy")
            case 11:
                loaded = 0
                print("===========================")
                print("=====--- GameVault ---=====")
                print("===========================")
                return
            case _:
                print("=========================")
                print("Please select a valid option.")
                continue

def browse_year():
    global loaded
    def ascending_year():
            global loaded
            n = loaded
            loaded += 26
            sorted_years = df.sort_values(by="Released_year")
            if sorted_years[n:(n+26)].empty:
                return "Thats all!"
            else:
                return sorted_years[n:(n+26)]
    def descending_year():
            global loaded
            n = loaded
            loaded += 26
            if df.sort_values(by="Released_year", ascending=False)[n:(n+26)].empty:
                return "Thats all!"
            else:
                return df.sort_values(by="Released_year", ascending=False)[n:(n+26)]

    def year_func(order):
            global loaded
            print("==================================")
            print(order())
            while True:
                print("==================================")
                print("1. Load more\n2. Back")
                try:
                    choice1 = int(input("Enter: "))
                except ValueError:
                    print("==================================")
                    print("Please enter a number.")
                    continue
                match choice1:
                    case 1:
                        print("==================================")
                        print(order())
                        continue
                    case 2:
                        print("==================================")
                        loaded = 0
                        break
                    case _:
                        print("==================================")
                        print("Please select a valid option.")
                        continue
        
    print("========================")
    print("==-- Browse By Year --==")
    print("========================")
    while True:
        print("1. Ascending order (Oldest first)\n2. Descending order (Newest first)\n3. Back")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("==================================")
            print("Please enter a number.")
            print("==================================")
            continue
        match choice:
            case 1:
                year_func(ascending_year)
            case 2:
                year_func(descending_year)
            case 3:
                print("===========================")
                print("=====--- GameVault ---=====")
                print("===========================")
                break
            case _:
                print("==================================")
                print("Please select a valid option.")
                print("==================================")
                continue



def random_game():

    def random_game_gen():
        n = randint(0, len(df)-1)
        game = df.iloc[n]
        game_name = game.name
        game_year = game["Released_year"]
        game_genre = game["Genre"]
        game_subgenre = game["Sub_genre"]
        game_rating = game["Rating"]

        result = f'''
    Name : {game_name}
    Rating : {game_rating}
    Genre : {game_genre}
    Sub Genre : {game_subgenre}
    Released Year : {game_year}
        '''
        return result
            
    print("===========================")
    print("====--- Random Game ---====")
    print("===========================")
    print(random_game_gen())
    print("==================================")
    while True:
        print("1. Another random game\n2. Back")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("==================================")
            print("Please enter a number.")
            print("==================================")
            continue
        match choice:
            case 1:
                print("==================================")
                print(random_game_gen())
                continue
            case 2:
                print("===========================")
                print("=====--- GameVault ---=====")
                print("===========================")
                break
            case _:
                print("==================================")
                print("Please select a valid option.")
                print("==================================")
                continue

main()