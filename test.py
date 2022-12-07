import requests
x = requests.get(' https://api.spoonacular.com/recipes/complexSearch?query=cake&maxFat=25&number=2&apiKey=df91e5f3a57e4ef8bdba434279171925')
print(x.text)