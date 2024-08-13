# Write code below 💖
# Grammys 🏆
from functools import reduce

#lista de canciones con su duracion (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8),
            ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

# Filtrar canciones que duren más de 5 minutos
def filter_playlist (song):
  return  song[1] >= 5.00

longer_than_five_minutes = list(filter(filter_playlist, playlist))
print ("Filtered songs:", longer_than_five_minutes)

# Convertir duración de minutos a segundos
def convert_duration(song):
  duration = song[1]
  minutes = int(duration)
  seconds = (duration - minutes) * 100
  total_seconds = minutes * 60 + round(seconds)
  return total_seconds

minutes_to_seconds = list(map(convert_duration, playlist))
print ("Durations in seconds:", minutes_to_seconds)

# Función para reducir (sumar) los tiempos en segundos
def reduce_song(acumulated, current):
    return acumulated + current

# Usar reduce para calcular el tiempo total en segundos
total_playtime_seconds = reduce(reduce_song, minutes_to_seconds)
print("Time in seconds:", total_playtime_seconds)  # Debería mostrar la suma total

# Convertir el tiempo total de segundos a minutos
total_playtime_minutes = total_playtime_seconds / 60
print("Time in minutes:", total_playtime_minutes)