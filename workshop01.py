def count_words(sentence):
    words = sentence.split()
    word_count = {}
    repeated_words = set()

    for word in words:
        if word in word_count:
            word_count[word] += 1
            repeated_words.add(word)
        else:
            word_count[word] = 1

    print(f"มีคำทั้งหมด {len(words)} คำ")

    if repeated_words:
        print("มีคำที่ปรากฏมากกว่า 1 ครั้ง:")
        for word in repeated_words:
            count = word_count[word]
            print(f"คำว่า '{word}' ปรากฏ {count} ครั้ง")

    else:
        print("ไม่มีคำที่ปรากฏมากกว่า 1 ครั้ง")

print("++++++++++++++++++++++++++++++++++++++")

user_sentence = input("ป้อนข้อความ: ")

print("++++++++++++++++++++++++++++++++++++++")

count_words(user_sentence)

print("++++++++++++++++++++++++++++++++++++++")