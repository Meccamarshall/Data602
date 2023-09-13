#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Shamecca Marshall


# In[2]:


# Data 602 - Assignment 2


# In[3]:


# Understanding Python Native Data Structures


# In[4]:


# 1. Can you debug and fix the output? The code should return the entire list


# In[5]:


numbers = ['1', '2', '3', '4', '5']


# In[6]:


print(numbers)


# In[7]:


print(numbers[-5:])


# In[8]:


## 2. Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.


# In[9]:


sales = [int(input(f"Enter the sales for {day}: ")) for day in "SMTWTFS"]


# In[10]:


sum(sales)


# ##### 3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in alphabetical order

# In[12]:


locations = ['Jamaica', 'Japan', 'Bali', 'Dubai', 'Cuba']


# In[13]:


## Original Order


# In[14]:


print("Original order:")
print(locations)


# In[15]:


## Use the sort() function to arrange your list in order and reprint your list.


# In[16]:


print(sorted(locations))


# In[17]:


## Use the sort(reverse=True) and reprint your list.


# In[18]:


print(sorted(locations, reverse=True))


# In[19]:


## 4. Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. After that, the program should let the user enter a course number, then it should display the course’s room number, instructor, and meeting time.


# In[20]:


# Create dictionary of course numbers and room numbers


# In[21]:


room_dict = {
    'Data602': '2014',
    'Data607': '1130',
    'Data606': '1215',
}


# In[22]:


# Create dictionary of course numbers and instructors


# In[23]:


instructor_dict = {
    'Data602': 'Nicholas Schettini',
    'Data607': 'Peter Kowalchuk',
    'Data606': 'Jason Bryer',
}


# In[24]:


# Create dictionary of course numbers and meeting times


# In[25]:


meeting_dict = {
    'Data602': 'Thursday 6:00pm',
    'Data607': 'Wednesday 7:00pm',
    'Data606': 'Wednesday 8:00pm',
}


# In[26]:


# 5. Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should then demonstrate the four options:
# ● lookup email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address


# In[27]:


def displayMenu():
    print()
    print("1) Look up email address")
    print("2) Add a name and email address")
    print("3) Change email address")
    print("4) Delete name and email address")
    print("5) End program")
    print()


# In[28]:


emailaddress = {}
choice = 0
displayMenu()
while choice != 5:
    choice = int(input("Enter your selection (1-5): "))

    if choice == 1:
        print("Look up email address:")
        name = input("Name: ")
        if name in emailaddress:
            print("The email address is", emailaddress[name])
        else:
            print(name, "was not found")
    elif choice == 2:
        print("Add a name and email address")
        name = input("Name: ")
        email = input("Email: ")
        emailaddress[name] = email
    elif choice == 3:
        print("Change email address")
        name = input("Name: ")
        if name in emailaddress:
            email = input("Enter the new address: ")
            emailaddress[name] = email
        else:
            print(name, "was not found")
    elif choice == 4:
        print("Delete name and email address")
        name = input("Name: ")
        if name in emailaddress:
            del emailaddress[name]
        else:
            print(name, "was not found")          
    elif choice != 5:
        print("Enter a valid selection")
        displayMenu()

