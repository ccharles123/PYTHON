#hacemos una losta de los partidos de futbol:

matches = [
    {
        "homeTeam" : "Bolivia",
        "awayTeam" : "Uruguay",
        "homeTeamScore" : 3,
        "awayTeamScore" : 1,
        "homeTeamResult" : "Win"
    },
    {
        "homeTeam" : "Brazil",
        "awayTeam" : "Mexico",
        "homeTeamScore" : 1,
        "awayTeamScore" : 1,
        "homeTeamResult" : "Draw"
    },
    {
        "homeTeam" : "Ecuador",
        "awayTeam" : "Venezuela",
        "homeTeamScore" : 5,
        "awayTeamScore" : 0,
        "homeTeamResult" : "Win"
    }
]

print(matches)
print(len(matches))

#vamos a filtrar la lsta con solo los equipos que han ganado:
filterTeamWins = list(filter(lambda item: item["homeTeamResult"] == "Win", matches))
print(filterTeamWins)
print(f"Tamaño de la lista filtrada con los equipos ganadores: {len(filterTeamWins)}")
print(f"No se ha modificado los items de la lista original: {len(matches)}")