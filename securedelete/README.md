# Files found through `photorec`

- f48320952.png - 1731377086.3945837-hmg_is5.png 3
- f67695936.png - 1731377039.5823972-dod.png 2
- f67707352.png - 1731377095.698013-hmg_is5.png 2
- f67707384.png - 1731377114.9686024-simple.png 2
- f67707416.png - 1731377121.576741-simple.png 2
- f67875480.png - 1731377070.9541516-gutmann.png
- f67875504.png - 1731377074.7612882-gutmann.png
- f115481800.png - 1731377065.7076235-gutmann.png 3
- f67875528.png - 1731377091.913828-hmg_isb.png
- f68162528.png - 1731377009.6838055-dod.png 3
- f68411616.png - 1731377043.8494325-dod.png 3
- f68411620.png - 1731377102.8356466-random.png 3
- f68411664.png - 1731377106.4825747-random.png 3
- f68682512.png - 1731377109.4010875-random.png 3

## Results

To find these photos I had to iterate through all the data `photorec` found and look for only `.png` files as there was around ~110 GB of data that `photorec` found. I did this with the following Python algorithm:

```python
import os
import shutil

def move_png_files(source_dir, destination_dir):
   if not os.path.exists(destination_dir):
       os.makedirs(destination_dir)

   for root, dirs, files in os.walk(source_dir):
       for file in files:
           file_path = os.path.join(root, file)
           if file.lower().endswith('.png'):
               shutil.move(file_path, os.path.join(destination_dir, file))
           else:
               os.remove(file_path)

if __name__ == "__main__":
   source_directory = 'output'
   destination_directory = 'png_files_found'

   move_png_files(source_directory, destination_directory)
```

- This allowed me to find the png's, but there were still ~78,000 files. So as I created the files and already knew the byte count I removed all files that were not in a specific range with the following Python program:

```python
import os

def remove_files_by_size(directory, min_size, max_size):
   for filename in os.listdir(directory):
       file_path = os.path.join(directory, filename)

       if os.path.isfile(file_path) and filename.lower().endswith('.png'):
           file_size = os.path.getsize(file_path)

           if file_size < min_size or file_size > max_size:
               os.remove(file_path)
               print(f"Removed: {file_path} (Size: {file_size} bytes)")

if __name__ == "__main__":
   directory = "png_files_found"

   min_size = 8500
   max_size = 10000

   remove_files_by_size(directory, min_size, max_size)
```

- From here, I was able to manually find the PNGs that I had made even though their titles had been obscured. This was a tedious process, but I was able to find all the files this way.

I was able to find every single picture through `photorec` except for, ironically, a simple deleted file just through `os.delete`. This is not at all what I was expecting to find, but I highlighted some key takeaways below.

## Takeaways

- Overall, searching to recover files is a tedious process, and the results are not always guaranteed. With the program I used, `photorec`, It was able to recover recently deleted files but it was not able to find specific files from my Ubuntu drive, only the entire partition or all parts that were not currently filled. This is a good thing for security as other os's like in Windows I was able to recover specific deleted files easily with another program called `testdisk` which is also made by the same company as `photorec`. So finding specific files in Ubuntu is very hard, If I had not switched to using PNGs, I would have never been able to find the txt files I was searching for.
  - If a hacker had been looking for this specific data would they be able to find it even though It wasnt obscured? I had to parse through 100gb+ of data! And If I had not known exactly what size files, the type of files, and what they png's looked like, then it would have taken forever to find the data, so there is a natural layer of security to this in that it takes sooo much time to find.

- Certain sensitive data, such as PNG's are not effected by the algorithms anywhere near as much as txt files are. For this I don't exactly know why, when I look at the pngs after the algorithms have run over them, they are unrecognizable and cannot be opened. So I don't understand how some of the files are still recoverable and are still legible as well even after the algorithms have run over them.

- I should look to try this study again to see if I can obscure them better this time. Next time I will try with large png's to make it obvious if they have been found or not. Now I know from the previous study that photorec does find deleted png's, now I just need to figure out why these png's are still recoverable after the algorithms were run over them.
