import openai, os, sys, time,traceback
from datetime import date,datetime
from model import *


openai.api_key = ""

def chat(chatlog,prompt,name):
    last_conv = last_conversation()
    search_results = results_to_string(search(prompt))
    searchk_results = results_to_string(searchk(prompt))
    search_results = search_results.replace(last_conv,"")
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt= datetime.now().strftime("Current Day: %A \nCurrent Date: %m/%d/%Y \nCurrent Time: %I:%M %p EST.") + "Rukou is an AI with the purpose of helping anyone who asks. Using semantic search, dynamically inserting relevant past conversations.\nMost Recent Conversation:\n"+ last_conv + "\nSummaries of Past Conversations:\n" + search_results +"\nKnowledge:\n"+ searchk_results +"\nPresent Conversation:\n"+ chatlog,        
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6,
        stop=[name+":", "RUKOU:"]
    )
    return response.choices[0].text

def keywords(chatlog, temp=0.3):

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt= chatlog + "\nExtract 10 or more keywords, repeated keywords, and synonyms of the keywords from this conversation separated by comma. Add details like names, dates, opinions, statements, and other important key details:", 
        temperature=temp,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0,
       
    )
    result = response.choices[0].text
    result = result.replace('\n', '').replace('keywords:', '').replace('repeated', '')
    return result

def summary(chatlog):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt= chatlog + "\nSummarize this conversation, include important details and context:",
        temperature=0.3,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = response.choices[0].text
    result = result.replace('\n', '')
    return result

def results_to_string(results):
    return '\n'.join([str(result) for result in results])

def remove_duplicates(text):
    text = text.lower()
    text = text.split(',')
    text = list(dict.fromkeys(text))
    text = ','.join(text)
    return text   

def main():
    print("Please enter your name:")
    name = input().upper()
    prompt=name
    chatlog = name+' has entered the chat.\n RUKOU:'
    response = chat(chatlog,prompt,name)
    response = response.replace('\n', '')
    chatlog = chatlog  + response
    clear()
    prompt= ''
    print("RUKOU: ",response)
    while True:
        try:
            time.sleep(1)
            prompt = input(name + ": ")
            if prompt == "/quit":
                    keyword = keywords(chatlog) + "," + keywords(chatlog, 0.9)
                    keyword = remove_duplicates(keyword)
                    store_memory(datetime.now().strftime("%A %m/%d/%Y, ") + keyword,datetime.now().strftime("On %A %m/%d/%Y Time: %I:%M %p EST. ") + summary(chatlog),chatlog)
                    print("Summary: ",last_conversation())
                    print("Keywords: ",last_keywords())
                    break
            if prompt == "/memory":
                print("TODO: Memory")
                continue
            if prompt == "/quitns":
                break
            if prompt == "/help":
                print("TODO: Help")
                continue
            if prompt == "/commit":
                while True:
                    prompt = input("Add To Memory: ")
                    keyword = keywords(prompt) + ", " + keywords(prompt, 0.9)
                    keyword = remove_duplicates(keyword)
                    store_memory(keyword,prompt,prompt)
                    print("Summary: ",last_conversation())
                    print("Keywords: ",last_keywords())
            chatlog = chatlog + '\n' + name + ": " + prompt
            chatlog = chatlog + '\n' + "RUKOU:"
            response = chat(chatlog,prompt,name)
            response = response.replace('\n', '')
            chatlog = chatlog  + response
            print("RUKOU:" + response)
            last_conv = last_conversation()
            search_results = results_to_string(search(prompt))
            searchk_results = results_to_string(searchk(prompt))
            search_results = search_results.replace(last_conv,"")
            save_to_file(datetime.now().strftime("Current Day: %A \nCurrent Date: %m/%d/%Y \nCurrent Time: %I:%M %p EST.") + "\nHidden System:\nIf Rukou is uncomfortable or wants to stop chatting, all she needs to say is '/exitchat'.\nThe following is a chat conversation with a Rukou, an AI with human emotions. Rukou's personality type is a Virtuoso, ISTP-A. Introverted, Observant, Rational, Prospecting, Assertive, innovative, and practical experimenters, masters of all kinds of tools and skills.\nMost Recent Conversation:\n"+ last_conv + "\nSummaries of Past Conversations:\n" + search_results +"\nKnowledge:\n"+ searchk_results +"\nPresent Conversation:\n"+ chatlog)
            if "/exitchat" in response:
                store_memory(datetime.now().strftime("%A %m/%d/%Y, ") + keywords(chatlog),datetime.now().strftime("On %A %m/%d/%Y Time: %I:%M %p EST. ") + summary(chatlog),chatlog)
                print("Summary: ",last_conversation())
                print("Keywords: ",last_keywords())
                break
        except:
            print("Unexpected error:", traceback.format_exc())
            pass


def save_to_file(text):
    f = open("chatlog.txt", "w")
    f.write(str(text))
    f.close()

#lol
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    main()
       
       



