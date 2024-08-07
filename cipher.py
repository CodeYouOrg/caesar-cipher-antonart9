# add your code here

# need to make a text prompt, 
# take user's prompt and assign alphabetical index value to each letter
# pass it thru the +5 postition formula for the indexes gathered from the input
# assing new alphabetical valuse based on new indexed position
# print the encoded message



# text prompt for use phrase
phrase = input("Please enter your phrase: ")

while True:
    try:
        chars = int(input("Please specify number of charecters: "))
        break
    except ValueError:
        print("That is not a number. Please try again...")

if chars > 26:
    chars = chars - 26

adict = {}


aindex = 1

for i in range(32,123): 
    adict[chr(i)] = aindex
    aindex += 1

sdict = {}
sindex = 1    
for y in range(32,97):
    sdict[chr(y)] = sindex
    sindex += 1
    
for i in adict:
    if i in sdict:
        adict[i] = adict.get(i) - chars

pindex = []
cypher = []
cdict = {v: k for k, v in adict.items()}

for i in phrase.lower():
    if i in sdict:
        pindex.append(adict.get(i))
    else:
        pindex.append(adict.get(i) + (chars))

for i in pindex:
    if i > 91:
        i = i - 91    
    cypher.append(cdict.get(i))

final = ""

for i in cypher:
    if i == 0:
        i = " "
    final += str(i)

print("Your Encrypted Message is:", final)



