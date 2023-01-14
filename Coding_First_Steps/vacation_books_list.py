
total_pages = int(input())
pages_per_hour = int(input())
days_for_one_book = int(input())

total_reading_hours = (total_pages // pages_per_hour)
reading_hours_per_day = total_reading_hours / days_for_one_book

print(reading_hours_per_day)
