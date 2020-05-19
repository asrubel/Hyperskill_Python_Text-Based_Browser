from sys import argv
from os import mkdir
from os import path
from _collections import deque

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

if not (len(argv) == 2 and argv[1]):
    exit()

if not path.exists(argv[1]):
    mkdir(argv[1])
sites = {'bloomberg.com', 'nytimes.com'}
tabs = set()
pages = deque()

current_page = ''
while True:
    if current_page == 'back':
        if pages:
            pages.pop()
            current_page = pages.pop()
        else:
            current_page = ''
            continue
    else:
        current_page = input()

    parts = current_page.split(".")
    if len(parts) > 1:
        site_name = ".".join(parts[:-1])
    else:
        site_name = current_page

    if current_page in sites:
        tabs.add(site_name)
        pages.append(current_page)
        with open(f"tb_tabs/{site_name}.txt", "w") as file:
            if current_page == 'bloomberg.com':
                print(bloomberg_com)
                file.write(bloomberg_com)
            elif current_page == 'nytimes.com':
                print(nytimes_com)
                file.write(nytimes_com)
    elif current_page in tabs:
        pages.append(current_page)
        with open(f"tb_tabs/{site_name}.txt", "r") as file:
            print(file.read())
    elif current_page == 'back':
        continue
    elif current_page == 'exit':
        break
    else:
        print("Error: Incorrect URL")
