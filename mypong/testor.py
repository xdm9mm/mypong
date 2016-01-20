import pipong_lib

s = pipong_lib.PongManager()
g = pipong_lib.PongGame()

s.current_game = g
p = s.new_player('Jason')
p = s.new_player('frank')
p = s.new_player('bob')
#g.players.append(p)


for name in s.player_directory:
    print s.player_directory[name].for_json()