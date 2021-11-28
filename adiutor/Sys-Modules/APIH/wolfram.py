import wolframalpha
import yaml

with open('adiutor/Config/config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Taking input from user
question = input('Question: ')

# App id obtained by the above steps
app_id = config['api']['wolframalpha']

# Instance of wolf ram alpha
# client class
client = wolframalpha.Client(app_id)

# Stores the response from
# wolf ram alpha
res = client.query(question)

# Includes only text from the response
answer = next(res.results).text

print(answer)
