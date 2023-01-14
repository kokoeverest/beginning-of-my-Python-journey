max_altitude = 8848
base_camp = 5364
days_climbing = 1

while True:
    sleep = input()

    if sleep == 'END' and base_camp < max_altitude:
        print('Failed!')
        print(f'{base_camp}')
        break
    elif sleep == 'END' and base_camp >= max_altitude:
        print(f'Goal reached for {days_climbing} days!')
        break

    meters_climbed = int(input())
    base_camp += meters_climbed

    if sleep == 'Yes':
        days_climbing += 1
    if base_camp >= max_altitude:
        print(f'Goal reached for {days_climbing} days!')
        break
    #     base_camp += meters_climbed
    # elif sleep == 'No':
    #     base_camp += meters_climbed

    if days_climbing >= 5:
        print('Failed!')
        print(f'{base_camp}')
        break

# Атанас е алпинист, чиято следваща цел е изкачването на Еверест. Вашата задача е да напишете програма
# която да следи до каква височина е достигнал Атанас и за колко дни е изкачил върха. Той започва
# изкачването си от ден първи от базов лагер, който е на 5 364 метра, а самият връх е на 8 848м. Преди всяко
# изкачване на определени метри, Атанас може да си почине в някой лагер и да продължи на следващия ден
# или да продължи изкачването без да спре, като максималното време, в което той може да изкачва върха е
# 5 дни. Програмата приключва при получаване на командата "END", при достигане на върха(8 848м) или при
# превишаване на разрешените 5 дни за изкачване.

'''# Вход
# От конзолата се четат по два реда до въвеждане на команда "END", ако са минали повече от 5 дни в
# изкачване или се достигне върха (8 848м):
#  "Yes" / "No" - текст - дали Атанас ще нощува преди изкачването на следващите метри или не
#  Изкачени метри - цяло число в интервала [1...4000]'''

# Изход
# След получаване на командата "END", превишаване на разрешениете 5 дни за изкачване или се достигне върха
# (8 848м), на конзолата се отпечатва:
#  Ако Атанас е изкачил Еверест:
# "Goal reached for {брой дни които Атанас е изкачвал върха} days!"
#  Ако Атанас НЕ е изкачил Еверест:
# "Failed!"
# "{достигнатите от Атанас метри}"
# Yes
# 535
# Yes
# 849
# Yes
# 499
# Yes
# 400
# Yes
# 500

# Yes
# 1000
# Yes
# 945
# No
# 1200
# END
