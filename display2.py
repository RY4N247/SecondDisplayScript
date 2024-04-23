import subprocess
import time
def execute_terminal_commands():
    # Replace these commands with the commands you want to execute
    commands = [
        "xrandr --output HDMI-1 --scale 1.5x1.67",
        "xrandr --output eDP-1 --primary --mode 2880x1800 --pos 0x1804 --rotate normal --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off",
        "xrandr --output eDP-1 --scale 0.9999x0.9999",
        "xrandr --output HDMI-1 --mode 1920x1080 --rate 144.00",
        "feh --bg-scale /home/ryan/Pictures/turtle.png" ##change directory to your image file
    ]
    for command in commands:
        subprocess.run(command, shell=True)
        time.sleep(1)

def main():
    try:
        execute_terminal_commands()
        time.sleep(2)
        print("\033[92mDisplay successfully configured!\033[0m")
       

    except:
        print("\033[91mfailed\033[0m")

if __name__ == "__main__":
    main()

