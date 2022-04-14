import json
import openai

with open('OPEN_AI_API.json') as file_api:
    file_data = json.load(file_api)

if file_data['key'] == '':
    print('ERROR: OpenAI API Key not provided!')
    print('       Fill the key property at OPEN_AI_API.json\n')

openai.api_key = file_data['key']

print('SUMMER - Summarizer of texts\n')

print('How does it work? You give me a text. And I give you a simple summary of that (maybe shorter)')

print('\nAvailable engines:')
print('1. DaVinci (default)')
print('2. Ada')
print('3. Babbage')
print('4. Curie')
ai_engine_identifier = int(
    input('Enter the AI engine you want to use (choose a number): '))

if ai_engine_identifier == 2:
    ai_engine = 'ada'
elif ai_engine_identifier == 3:
    ai_engine = 'babbage'
elif ai_engine_identifier == 4:
    ai_engine = 'curie'
else:
    ai_engine = 'davinci'

print('Awesome! Using ' + ai_engine.upper() + ' as the Open AI engine.')

text_input = str(input('Enter your text: '))
text_input = text_input.strip()

print('Please wait...')

response = openai.Completion.create(
    engine=ai_engine,
    prompt="My second grader asked me what this passage means:\n\"\"\"\n" + text_input +
    "\n\"\"\"\nI rephrased it for him, in plain language a second grader can understand:\n\"\"\"\n",
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0,
    stop=["\"\"\""]
)

print('\nYour response is: ')
print(response["choices"][0]["text"])

text_response = response["choices"][0]["text"]

with open('summarized_text.txt', 'a') as file_output:
    print('\nText saved on summarized_text.txt!')
    file_output.write(text_response)
