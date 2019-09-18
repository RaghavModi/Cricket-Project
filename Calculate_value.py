def players(player):
    points=0 
    runs=player.get('runs')
    points=int(runs/2)
    if runs>=100:
        points=points+10
    elif runs>=50:
        points=points+10
    faced=player.get('faced')/2
    points=points+2
    four=player.get('fours')
    points=points+four
    six=player.get('sixes')*2
    points=points+six
    wickets=player.get('wickets')*10
    points=points+wickets
    bowled=player.get('bowled')/6
    points=points+bowled
    maiden=player.get('maiden')*3
    points=points+maiden
    given=player.get('given')
    if given<30:
        points=points+5
    elif given>=30 and given<35:
        points=points+3
    else:
        points=points+1
    catches=player.get('catches')*10
    points=points+catches
    stumps=player.get('stumps')*20
    points=points+stumps
    run=player.get('run out')*5
    points=points+run
    return int(points)


