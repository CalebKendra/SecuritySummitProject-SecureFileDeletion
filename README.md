# Secure File Deletion

This program uses the following algorithms as options for secure deletion:

### 1. Gutmann Method

Overwrites the file with random data 35 times.

### 2. DoD 5220.22-M Method

Specified by the U.S. Department of Defense, this method overwrites the file with random data, 0's, and 1's 7 times.

### 3. HMG IS5 (Enhanced) Method

Specified by the British government, this method overwrites the file with random data, 0's, and 1's 3 times, 1 time for each type of overwrite.

### 4. Random Method

Overwrites the file with random data a random number of times (between 1 and 10), providing variable security. This should be a weaker methods that could possibly be recoverable

### 5. Simple Deletion

Uses the `os.remove` function to delete the file without additional security measures. Should be used as a test bench as these files should be recoverable
