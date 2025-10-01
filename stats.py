from collections import Counter

def get_num_words(st):
    print(f"Found {len(st.split())} total words")

def get_count_char(st):
    return dict(Counter(st.lower()))

def get(st):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(st)
    print("--------- Character Count -------")
    l = get_count_char(st)
    ans = []
    for a in l:
        ans.append((l[a],a))
    ans.sort(reverse=True)
    for a,b in ans:
        if b.isalpha():
            print(f"{b}: {a}")
    print("============= END ===============")