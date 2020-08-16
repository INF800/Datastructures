from rich.console import Console
console = Console()
# console.print

Rakesh = 'Rakesh'

file_7= \
f"""
Hi I am [bold red]{Rakesh}[/bold red] and
I want to [u]demo[/u] this
console [i]anim[/i] ...
"""

# -------------------
# animation function
# -------------------
import os, time
os.system('clear')
def anim(frames_list, delay=1, repeat=10):
    for _ in range(repeat):
        for frame in frames_list:
            acc = []
            for char in frame:
                acc.append(char)
                console.print( ''.join(map(str, acc))  )
                time.sleep(delay)
                os.system('clear')
            acc = []

if __name__ == '__main__':
    
    frames = [file_7]
    anim(frames, delay=0.16, repeat=100)