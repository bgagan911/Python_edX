import os, pyperclip,pprint

# Clear Console
os.system('clear')

# Paste the clipboard text.
LargeListText = pyperclip.paste()

pprint.pprint(LargeListText)
#print(LargeListText)

newList = LargeListText.splitlines()
print(newList[2])

for i in range(len(newList)):
    newList[i] = "* " + newList[i]
    # print("newList[" + int(i) + "] = " + newList[i])

LargeListText = "\n".join(i for i in newList[:])
pyperclip.copy(LargeListText)
print("\n\n***  Final List\n\n", LargeListText, "\n\n")