def find_jumbled_words():
    words = ["listen", "silent", "enlist", "inlets", "google", "glooge"]
    target = "listen"
    jumbled_words = []

    for word in words:
        if sorted(word) == sorted(target):
            jumbled_words.append(word)

    return jumbled_words