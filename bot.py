import re
import random

respPatterns = [["hello",
                 ["Hi!","Hello!","Greetings!","Howdy!"]],
                ["hi",
                 ["Hi!","Hello!","Greetings!","Howdy!"]],
                ["my name is (.*)",
                 ["Hi, %0"]],
                ["i like (.*)",
                 ["Why do you like %0 ?"]],
                ["i don't know (.*)",
                 ["Perhaps you should learn.",
                 "I don't know either."]],
                ["i'm (.*)",
                 ["Why are you %0 ?"]],
                ["because (.*)",
                 ["Is that a good reason?"],
                 ["Are there any other good reasons?"],
                 ["Is that the only reason?"]],
                ["i (.*)",
                 ["Why do you %0 ?"]],
                ["(.*) is (.*)",
                 ["Why is %0 %1 ?"]],
                ["why (.*)",
                 ["What do you think?"]],
                ["(.*) are (.*)",
                 ["Why are %0 %1 ?"]],
                ["(.*)",
                 ["Can you please elaborate?",
                 "I don't fully understand.",
                 "Let's stop talking about this.",
                 "How are you feeling about this?"]]
                ]

pronouns = {"i'm": "you're", "i":"you","me":"you","yours":"mine","you":"I","am":"are","my":"your","you're":"I'm"}

random.seed()
print "I'm psychiatrist bot. I can make you feel better. Tell me how you're feeling!"

while True:
    input = raw_input("> ") #get input
    input = input.lower()
    input = input.rstrip('.!?')
    
    for pattern in respPatterns:
        wildcards = []
        if re.match(pattern[0], input):
            wildcards = re.split(pattern[0], input)
            wildcards = [x for x in wildcards if x]
            rand = random.randint(0,len(pattern[1]) - 1)
            responseWords = pattern[1][rand].split(' ')
            response = "" 
            for word in responseWords:
                if word.startswith('%'):
                    word = word.lstrip('%')
                    word = wildcards[int(word)]
                    word = ' '.join(pronouns.get(s,s) for s in word.split())
                response += word + ' '
            break
    
    print response
          

        
         
              
                
              
      
      
