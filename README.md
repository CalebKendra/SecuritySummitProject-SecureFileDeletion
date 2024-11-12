# Secure File Deletion

This is an analysis program that creates a `png` file that is then deleted by the algorithms below. After this, I use a program called [photorec]([url](https://www.cgsecurity.org/wiki/photoRec)) to attempt to find these previously deleted `png` files. From this, I can roughly test whether these `png` files are deleted or still readable.

This program uses the following algorithms as options for secure deletion:

### 1. Gutmann Method

Overwrites the file with random data 35 times.

### 2. DoD 5220.22-M Method

Specified by the U.S. Department of Defense, this method overwrites the file with random data, 0s, and 1s seven times.

### 3. HMG IS5 (Enhanced) Method

Specified by the British government, this method overwrites the file with random data, 0s, and 1s three times, one time for each type of overwrite.

### 4. Random Method

Overwrites the file with random data a random number of times (between 1 and 10), providing variable security. This should be a weaker method that could be recoverable

### 5. Simple Deletion

Uses just the `os.remove` function to delete the file without additional security measures. Should be used as a test bench as these files should be recoverable
