
import io

file = io.open("some_png.png", "rb", buffering = 0)
print(file.read())
