computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
itemnumber = 1
computer_games.sort()
while itemnumber <= len(computer_games):
    print(f'{itemnumber}. {computer_games[itemnumber - 1]}')
    itemnumber += 1