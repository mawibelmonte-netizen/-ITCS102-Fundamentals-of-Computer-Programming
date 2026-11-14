anime = []

ans = input("Do you watch any anime series? (YES/NO) --> ").lower()

while True:
    
    if ans == "yes":
        title = input("What is the title of the anime --> ")
        anime.append(title)
        ans = input("Do you want to continue to give anime title? (YES/NO) --> ").lower()
    else:
        print(anime)
        break