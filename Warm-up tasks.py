# task from: http://hack.engeto.com/warmup

import operator

def longest_word_in_a_sequence():
    # Determine the longest word in a sequence
    seq = "Determine the longest word in a sequence in this veeeeery looong statement".split()
    longest = ""
    length = 0
    for wrd in seq:
        a = len(wrd)
        if (a) >= length:
            length = a
            longest = wrd
    print()
    print(longest)
    # returns only one longest word - doesn't take into account more than one word of the same, longest, length

def get_filename_extension():
    """"
    Write a Python program that will accept a filenames input return
    the extension of that file.
    """
    filename = "super.test.txt".split(".")
    print(filename[len(filename)-1])

def dif_odd_even():
    """"
    Write a Python program that will collect all the even numbers and odd numbers
    separately. Then return the absolute difference between the highest even and
    highest odd value.
    """
    nums = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527, 999, 1000
    ]
    highestOdd = 0
    highestEven = 0
    for i in nums:
        pass
    sorted_values = sorted(nums)
    for i in sorted_values:
        if i % 2 == 1 and i >= highestOdd:
            highestOdd = i
        if i % 2 == 0 and i >= highestEven:
            highestEven = i
    print(abs(highestEven-highestOdd))

def get_counts(inValue):
    #startingInput = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2,666,666,666,666]
    #startingInput = "returns only one longest word - doesn't take into account more than one word of the same".split()
    if isinstance(inValue,str):
        startingInput = inValue.split()
    else:
        startingInput = inValue
    singleInputValues = set(startingInput)
    dictionaryOfCounts = {}
    for i in singleInputValues:
        kv = {i : startingInput.count(i)}
        dictionaryOfCounts.update(kv)
    sortedDictionaryOfCounts = sorted(dictionaryOfCounts.items(), key=operator.itemgetter(1),reverse=True)

    # print(" Item |Count")
    # print("=============")



    tableHeader = " {0:<10}{1:<3}{2:<4}".format("Item", '|', "Count")
    print(tableHeader)
    print((len(tableHeader)+1)*"=")
    for touple in sortedDictionaryOfCounts:
        #print((" {0:<5}{1:<3}{2:<4}".format(touple[0], '|', touple[1])))
        print((" {0:<10}{1:<3}{2:<4}".format(touple[0], '|', touple[1])))

# get_counts("returns only one longest word - doesn't take into account more than one word of the same")

