def palindrome(words):
    w = []
    for word in words:
        w.append(word)

    j = len(w) - 1
    i = 0

    while i != len(w):
        if w[j] != w[i]:
            print(words, '不是回文唷!')
            break
        j -= 1
        i += 1

    if i == len(w):
        print(words, '是回文。')

words = input('回文判斷，請輸入英文單字：')
palindrome(words)