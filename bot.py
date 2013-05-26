import re
import random

responses = (
    ("hello",                ("Hi!", "Hello!", "Greetings!", "Howdy!")),
    ("hi",                   ("Hi!", "Hello!", "Greetings!", "Howdy!")),
    ("my name is (.*)",      ("Hi, %0",)),
    ("i like (.*)",          ("Why do you like %0 ?",)),
    ("i don't know (.*)",    ("Perhpans you should learn.", "I don't know either.")),
    ("i'm (.*)",             ("Why are you %0 ?",)),
    ("because (.*)",         ("Is that a good reason?", "Are there any other good reasons?", "Is that the only reason?")),
    ("i (.*)",               ("Why do you %0 ?",)),
    ("(.*) is (.*)",         ("Why is %0 %1 ?",)),
    ("why (.*)",             ("What do you think?",)),
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
          

        
         
              
                
              
      
      
