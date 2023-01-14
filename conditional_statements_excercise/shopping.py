budget = float(input())
video_cards = int(input())
processors = int(input())
memory = int(input())

video_card_price = 250
processor_price = (video_card_price * video_cards) * 0.35
memory_price = (video_card_price * video_cards) * 0.10

total_price = (video_card_price * video_cards) + (processor_price * processors) + (memory_price * memory)

if video_cards > processors:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
