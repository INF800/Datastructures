# origin source: https://www.youtube.com/watch?v=JavJqJHLo_M
# use python rich too!

Rakesh = 'Rakesh'

file_1 = \
f"""
Hi I am {Rakesh}
"""

file_2 = \
f"""
Hi I am {Rakesh} and
I want
"""

file_3= \
f"""
Hi I am {Rakesh} and
I want to demo this
"""

file_4= \
f"""
Hi I am {Rakesh} and
I want to demo this
console anim
"""

file_5= \
f"""
Hi I am {Rakesh} and
I want to demo this
console anim .
"""


file_5= \
f"""
Hi I am {Rakesh} and
I want to demo this
console anim .
"""


file_6= \
f"""
Hi I am {Rakesh} and
I want to demo this
console anim ..
"""

file_7= \
f"""
Hi I am {Rakesh} and
I want to demo this
console anim ...
"""

# -------------------
# animation function
# -------------------
import os, time
os.system('clear')
def anim(frames_list, delay=1, repeat=10):
    for iter in range(repeat):
        for frame in frames_list:
            print(frame)
            time.sleep(delay)
            os.system('clear')

if __name__ == '__main__':
    
    frames = [file_1, file_2, file_3, file_4, file_5]
    anim(frames, delay=0.2, repeat=100)