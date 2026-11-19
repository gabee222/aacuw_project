import sqlite3
import matplotlib.pyplot as plt

rows = [ (2017, 161, 481, 289, 288, None),
        (2018, 174, 549, 288, 320, None),
        (2019, 174, 420, 320, 315, None),
        (2020, 163, 450, 315, 129, "COVID"),
        (2021, 67, 556, 129, 313, "COVID"),
        (2022, 104, 556, 313, 363, "MADE PLAYOFFS"),
        (2023, 135, 543, 363, 396, None),
        (2024, 173, 525, 396, 379, None),
        (2025, 185, 556, 379, 390, "MADE PLAYOFFS"),
        (2026, 202, 469, 390, None, None),
]

year = [r[0] for r in rows]
playerExpenses = [r[1] for r in rows]
winPct = [r[2] for r in rows]
revenue = [r[3] for r in rows]
nextRevenue = [r[4] for r in rows]
notes = [r[5] for r in rows]

plt.figure()
plt.scatter(playerExpenses, winPct)
plt.xlabel("Player Expenses ($M)")
plt.ylabel("Wins / 1000 Games")
plt.title("Player Expenses Relation to Win Percentage")
plt.savefig("expenses_v_wins.png")

plt.figure()
plt.scatter(winPct, nextRevenue)
plt.xlabel("Wins / 1000 Games")
plt.ylabel("Revenue of Following Season ($M)")
plt.title("Win Percentage Relation to Following Season's Revenue")
plt.savefig("wins_v_next_rev.png")

plt.figure()
plt.scatter(playerExpenses, nextRevenue)
plt.xlabel("Player Expenses in Season n ($M)")
plt.ylabel("Revenue of Season n+1 ($M)")
plt.title("Player Expenses Relation to Following Season's Revenue")
plt.savefig("expenses_v_next_rev.png")