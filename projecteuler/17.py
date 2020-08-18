ones = ['', 'one', 'two', 'three', 'four', 'five',\
        'six', 'seven', 'eight', 'nine']
tens = ['', -1, 'twenty', 'thirty', 'forty', 'fifty', \
        'sixty', 'seventy', 'eighty', 'ninety']
teens = ["ten", 'eleven', 'twelve', 'thirteen',\
        'fourteen', 'fifteen', 'sixteen', 'seventeen',\
        'eighteen', 'nineteen']
hundreds = ['', 'onehundred', 'twohundred',\
        'threehundred', 'fourhundred', 'fivehundred',\
        'sixhundred', 'sevenhundred', 'eighthundred',\
        'ninehundred']

def countletters(i: int) -> int:
    ssum = 0
    dig0 = i // 100
    dig1 = (i // 10) % 10
    dig2 = i % 10
    if dig0:
        ssum += len(hundreds[dig0])
        if dig1 or dig2:
            ssum += 3
    if dig1 == 1:
        ssum += len(teens[dig2])
    else:
        if dig1:
            ssum += len(tens[dig1])
        ssum += len(ones[dig2])
    return ssum

ssum = 0
for i in range(1, 1000):
    ssum += countletters(i)
ssum += len('onethousand')
print(ssum)

# print(countletters(516))
# print(len("fivehundredandsixteen"))
