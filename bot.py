import re
import random

responses = (
    ("hello",                ("Hi!", "Hello!", "Greetings!", "Howdy!")),
    ("hi",                   ("Hi!", "Hello!", "Greetings!", "Howdy!")),
    ("how are you",          ("I'm fine, thank you.",)),
    ("i need (.*)",          ("Why do you need %0 ?", "Would it really help you to get %0 ?", "Are you sure you need %0 ?")),
    ("why don't you (.*)",   ("Do you really think I don't %0 ?", "Perhaps eventually I will %0 .", "Do you really want me to %0 ?")),
    ("why can't I (.*)",     ("Do you think you should be able to %0 ?", "If you could %0 , what would you do?", "I don't know -- why can't  you %0 ?", "Have you really tried?")),
    ("i can't (.*)",         ("How do you know you can't %0 ?", "Perhaps you could %0 if you tried.", "What would it take for you to %0 ?")),
    ("i am (.*)",            ("Did you come to me because you are %0 ?", "How long have you been %0 ?", "How do you feel about being %0 ?")),
    ("are you (.*)",         ("Why does it matter whether I am %0 ?", "Would you prefer it if I were not %0 ?", "Perhaps you believe I am %0 .", "I may be %0 -- what do you think?")),
    ("how (.*)",             ("How do you suppose?", "Perhaps you can answer your own question.", "Why can't you answer your question?", "What is it you're really asking?")),
    ("i think (.*)",         ("Do you doubt %0 ?", "Do you really think so?", "But you're not sure %0 ?")),
    ("(.*) friend (.*)",     ("Tell me more about your friends.", "What do you value in a friend?")),
    ("yes",                  ("Okay, but can  you tell me more?", "Can you actually be sure?", "You seem quite certain.")),
    ("no",                   ("Why not?", "Can you tell me why you say no?", "Are you sure?")),
    ("is it (.*)",           ("Do you think it is %0 ?", "Perhaps it's %0 -- what do you think?", "If it were %0 , what would you do?", "It could well be that %0 .")),
    ("can you (.*)",         ("If I could %0 , then what?", "Why do you ask if I can %0 ?")),
    ("can i (.*)",           ("Do you want to be able to %0 ?", "If you could %0 , would you?")),
    ("you are (.*)",         ("Why do you think I am %0 ?", "Perhaps you would like me to be %0 .", "Are you really talking about yourself?")),
    ("you're (.*)",          ("Why do you say I am %0 ?", "Why do you think I am %0 ?", "Are we talking about you, or me?")),
    ("i don't (.*)",         ("Why don't you %0  ?", "DO you want to %0 ?")),
    ("i feel (.*)",          ("Tell me more about these feelings.", "Do you often feel %0 ?", "When do you usually feel %0 ?", "When you feel %0 , what do you do?")),
    ("i have (.*)",          ("Why do you tell me that you've %0 ?", "Have you really %0 ?", "Now that you have %0, what will you do next?")),
    ("i would (.*)",         ("Could you explain why you would %0 ?", "Why would you %0 ?", "Who else knows that you would %0 ?")),
    ("is there (.*)",        ("Do you think there is %0 ?", "Is it likely that there is %0 ?", "Would you like there to be %0 ?")),
    ("my (.*)",              ("Why do you say that your %0 ?", "When your %0 , how do you feel?")),
    ("you (.*)",             ("We should be discussing you, not me.", "Why do you say that about me?", "Why do you care whether I %0 ?")),
    ("i want (.*)",          ("What would it mean to you if you got %0 ?", "Why do you want %0 ?", "What would you do if you got %0 ?", "If you got %0, then what you do?")),
    ("my name is (.*)",      ("Hi, %0",)),
    ("i don't know (.*)",    ("Perhaps you should learn.", "I don't know either.")),
    ("i'm (.*)",             ("Why are you %0 ?",)),
    ("because (.*)",         ("if %0, what else is true?", "Is that a good reason?", "Are there any other good reasons?", "Is that the only reason?", "Why do you think %0 ?")),
    ("i (.*)",               ("Why do you %0 ?",)),
    ("(.*) is (.*)",         ("Why is %0 %1 ?",)),
    ("(.*) can't (.*)",      ("Why can't %0 , %1")),
    ("why (.*)",             ("What do you think?", "Why do you think %0 ?", "Why don't you know the answer yourself?")),
    ("(.*) are (.*)",        ("Why are %0 %1 ?",)),
    ("(.*)",                 ("Can you please elaborate?", "I don't fully understand.", "Let's stop talking about this.", "How are you feeling about this?")),
)

pronouns = {
    "i'm": "you're", 
    "i": "you", 
    "me": "you",
    "yours": "mine",
    "you": "I",
    "am": "are",
    "my": "your",
    "you're": "I'm"
}

random.seed()
print "I'm psychiatrist bot. I can make you feel better. Tell me how you're feeling!"

while True:
    input = raw_input("> ")
    input = input.lower().rstrip('.!?')
    
    for pattern in responses:
        wildcards = []
        if re.match(pattern[0], input):
            wildcards = re.split(pattern[0], input)
            wildcards = filter(bool, wildcards) # returns all e in wildcards for which bool(e) == True
            response = "" 
            for word in random.choice(pattern[1]).split(' '):
                if word.startswith('%'):
                    word = wildcards[int(word.lstrip('%'))] # get the input words to fill in
                    word = ' '.join(pronouns.get(s, s) for s in word.split()) # swap pronouns to make grammar correct
                response += word + ' '
            break
    
    print response
          

        
         
              
                
              
      
      
