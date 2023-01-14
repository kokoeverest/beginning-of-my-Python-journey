pool_volume = int(input())
first_pipe_litres_per_hour = int(input())
second_pipe_litres_per_hour = int(input())
worker_missing_hours = float(input())

first_pipe_fill = worker_missing_hours * first_pipe_litres_per_hour
second_pipe_fill = worker_missing_hours * second_pipe_litres_per_hour


total_water_filled = first_pipe_fill + second_pipe_fill

if pool_volume >= total_water_filled:
    print(f"The pool is {total_water_filled / pool_volume * 100}% full. Pipe 1: {first_pipe_fill / total_water_filled * 100:.2f}%. Pipe 2: {second_pipe_fill / total_water_filled * 100:.2f}%.")
else:
    print(f"For {worker_missing_hours} hours the pool overflows with {total_water_filled - pool_volume} liters.")
# Басейн с обем V има две тръби от които се пълни. Всяка тръба има определен дебит (литрите вода минаващи през /
# една тръба за един час). Работникът пуска тръбите едновременно и излиза за N часа. Напишете програма, която /
# изкарва състоянието на басейна, в момента, когато работникът се върне.

# Да се отпечата на конзолата едно от двете възможни състояния:
#     • До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
#         ◦ "The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%. /
#         Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
#         ◦ "For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."