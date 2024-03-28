
#task1 
def reverse_string(input_string):
    return input_string[::-1]


original_string = "I'm, Fauzi!"
reversed_string = reverse_string(original_string)


print(f"Task 1:Original String: {original_string}")
print(f"Reversed String: {reversed_string}")



#task2
def find_average(numbers):
 
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


list_of_numbers = [10, 20, 30, 40, 50]


average_result = find_average(list_of_numbers)


print(f"Task 2: List of Numbers: {list_of_numbers}")
print(f"Average: {average_result}")


#task3
def merge_dicts(dict1, dict2):
  
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = [merged_dict[key], value] if isinstance(merged_dict[key], list) else [merged_dict[key], value]
        else:
            merged_dict[key] = value
    return merged_dict


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}


result_dict = merge_dicts(dict1, dict2)


print(f" Task 3: Dictionary 1: {dict1}")
print(f" Dictionary 2: {dict2}")
print(f" Merged Dictionary: {result_dict}")


#task4
def divide_numbers(num1, num2):

    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


number1 = 10
number2 = 0


result = divide_numbers(number1, number2)


print(f"Task 4 :Result of dividing {number1} by {number2}: {result}")



#task5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


my_rectangle = Rectangle(length=5, width=3)


area_result = my_rectangle.calculate_area()


perimeter_result = my_rectangle.calculate_perimeter()


print(f"Task5: length: {my_rectangle.length}")
print(f"Width: {my_rectangle.width}")
print(f"area result: {area_result}")
print(f"perimeter: {perimeter_result}")

#task6
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

unsorted_list = [64, 34, 25, 12, 22, 11, 90]


sorted_list = bubble_sort(unsorted_list)


print(f"Task 6: {unsorted_list}")
print(f"List {sorted_list}")


#task7
import requests
from bs4 import BeautifulSoup

def scrape_top_news_titles(url):
 
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')

    
    titles = [headline.text for headline in soup.find_all('h3')[:5]]

    return titles


news_url = "https://www.bbc.com/news"
top_news_titles = scrape_top_news_titles(news_url)


print("Task 7: Top 5 News Titles:")
for i, title in enumerate(top_news_titles, start=1):
    print(f"{i}. {title}")



#task8
import matplotlib.pyplot as plt


days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
temperatures = [25, 27, 23, 30, 28, 29, 26]


plt.plot(days, temperatures, marker='o')
plt.title('Temperature Trend Over 7 Days')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')


plt.show()



#task9
def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)


list_of_numbers = [1, 2, 3, 4, 3, 5, 6, 4, 7, 8, 9, 1]


duplicate_numbers = find_duplicates(list_of_numbers)


print(f"Task 9:List of Numbers: {list_of_numbers}")
print(f"Duplicate Numbers: {duplicate_numbers}")











