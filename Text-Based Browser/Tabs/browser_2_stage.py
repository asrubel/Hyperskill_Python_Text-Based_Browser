from sys import argv
from os import mkdir
from os import path

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

if len(argv) == 2 and argv[1]:
    if not path.exists(argv[1]):
        mkdir(argv[1])
    sites = {'bloomberg.com', 'nytimes.com'}
    tabs = set()

    while True:
        user_prompt = input()
        parts = user_prompt.split(".")
        if len(parts) > 1:
            site_name = ".".join(parts[:-1])
        else:
            site_name = user_prompt

        if user_prompt in sites:
            tabs.add(site_name)
            with open(f"tb_tabs/{site_name}.txt", "w") as file:
                if user_prompt == 'bloomberg.com':
                    print(bloomberg_com)
                    file.write(bloomberg_com)
                elif user_prompt == 'nytimes.com':
                    print(nytimes_com)
                    file.write(nytimes_com)
        elif user_prompt in tabs:
            with open(f"tb_tabs/{site_name}.txt", "r") as file:
                print(file.read())
        elif user_prompt == 'exit':
            break
        else:
            print("Error: Incorrect URL")
