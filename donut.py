import math
import os
import time

def render_donut():
    A = 0
    B = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        z = [0] * 1760  # Z-buffer
        b = [' '] * 1760  # Output buffer

        for j in range(0, 628, 7):  # θ angle loop (0 to 2π with step size)
            for i in range(0, 628, 2):  # φ angle loop (0 to 2π with step size)
                sin_A = math.sin(A)
                cos_A = math.cos(A)
                sin_B = math.sin(B)
                cos_B = math.cos(B)

                sin_i = math.sin(i)
                cos_i = math.cos(i)
                sin_j = math.sin(j)
                cos_j = math.cos(j)

                h = cos_i + 2  # Donut size (major radius + minor radius)
                D = 1 / (sin_j * h * sin_A + sin_i * cos_A + 5)  # Perspective divide

                t = sin_j * h * cos_A - sin_i * sin_A  # x' coordinate
                x = int(40 + 30 * D * (cos_j * h * cos_B - t * sin_B))  # x coordinate
                y = int(12 + 15 * D * (cos_j * h * sin_B + t * cos_B))  # y coordinate
                o = int(x + 80 * y)  # Index in buffers

                N = int(8 * ((sin_i * sin_A - sin_j * cos_i * cos_A) * cos_B -
                             sin_j * cos_i * sin_A - sin_i * cos_A - cos_j * cos_i * sin_B))  # Luminance

                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N % 12]

        print('\033[H', end='')  # Move cursor to top-left
        print(''.join(b))  # Render the donut
        A += 0.04  # Increment angles for rotation
        B += 0.02
        time.sleep(0.03)

if __name__ == "__main__":
    render_donut()
