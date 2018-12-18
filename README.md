# 計理期末ChatBot---Simple_JukeBox

## package requirement
1.bottle
2.pygraphviz
3.requests
4.transitions
5.beautifulsoup4

## How to use
### run ngrok
run ngrok in the folder
```
./ngrok http 5000
```
### run the app
```
python3 app.py
```

## How to use the chatbot
Here is the diagram

![](https://i.imgur.com/08Cq7nR.png)

You can send 'help' to know what you can send

There are mainly there mode
### Select rock song
Send 'rock song' in the user mode, the chatbot turn into rock song mode
The chatbot will tell you to choose a band.
You can choose one of the bands simple by pressing the button.
Or you can go back to user mode by send go back


After you choose the mode, you have two choice
1. choose another song by send the name of the band(the bot will tell you)
2. send 'go back' to go back to the band select state

### Select study song
Send 'study song' in the user mode, the chatbot turn into study song mode
The Chatbot will send you a study bgm and ask you question
You have two choice:
1. choose another song by send 'study song'
2. send 'go back' to go back to the user mode

### Talking mode
In this mode, Chatbot will ask your emotion, you have three choice
1. happy
2. angry
3. sad

You can choose one of them simply by pressing the button

#### choose happy
The Chatbot will send you a song and then ask you if you want another.
There are two buttons
1. yes
2. no

If yes it will send you another song and ask you again
If no it will send you a song to encourage you and return the user mode

#### choose angry and sad
The Chatbot will send you a song and then ask for your feeling.
There are three buttons
1. feel better
2. angry
3. sad

If feel better it will send you a song to encourage you and return the user mode
If angry or sad it will send you a song of angry or sad and ask you again


