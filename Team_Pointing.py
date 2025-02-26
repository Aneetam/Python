def calculate_league_points(wins, draws, losses):
    # Complete this function
    r=((wins*4)+(draws*2))-losses
    return r


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
result=calculate_league_points(wins,draws,losses)
print(result)