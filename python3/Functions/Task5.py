#n = input("Enter number:")


def transform(n):
    n_string = str(n)
    n_list = list(n_string)
    simple = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'foreteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    dozens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundreds = ['', 'hundred']
    if n == 0:
        n = "zero"
    elif 0 < n < 20:
        n = simple[n]
    elif 20 <= n < 100:
        n = [dozens[int(n_list[0])], ' ', simple[int(n_list[1])]]
    elif 100 <= n < 1000:
        a = n % 100
        b = n//100
        if 0 <= a < 20:
            n = [simple[b], ' ', hundreds[1], ' ', simple[a]]
        elif 20 <= a < 100:
            n = [simple[b], ' ', hundreds[1], ' ', dozens[a//10], ' ', simple[a % 10]]
    elif n == 1000:
        n = "one thousand"
    return ''.join(n)
for i in range(0, 1001):
    print transform(i)