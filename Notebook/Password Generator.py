
# coding: utf-8

# In[ ]:


#Password Generator


# In[ ]:


import random
level1="abcdefghijklmnopqrstuvwxyz"
level2="abcdefghijklmnopqrstuvwxyz0123456789"
level3="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
level4="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lenght = int(input('How long password do you need? :'))
levelchoice=input('Which level of password do you want ?: \nlevel1 - low letters \nlevel2 - low letters + numbers\nlevel3 - low/high letters + numbers \nlevel4 - low/high letters + numbers + special signs')
def passgen():
    
    if levelchoice =='level1':
        p =  "".join(random.sample(level1,lenght ))
        print(p)
    elif levelchoice =='level2':
        p =  "".join(random.sample(level2,lenght ))
        print(p)
    elif levelchoice =='level3':
        p =  "".join(random.sample(level3,lenght ))
        print(p)
    elif levelchoice =='level4':
        p =  "".join(random.sample(level4,lenght ))
        print(p)
    else:
        print('Incorect variables')

passgen()

