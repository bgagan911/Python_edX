# PasswordLocker : An Insecure Password locker program

import sys, os, pyperclip

# data structure {Dictionary} to store information.
# website/site and corresponding password
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345',
             }

# Take Arguement
if len(sys.argv) < 2:
    os.system('clear')
    print('\n\n\n\t\t\tUsage: python PasswordLocker.py [account] - copy account password',end='\n\n\n')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS: 
    pyperclip.copy(PASSWORDS[account]) 
    print('\n\n\nPassword for ' + account + ' copied to clipboard.\n\n\n') 
else: 
    print('\n\n\nThere is no account named ' + account + '\n\n\n')