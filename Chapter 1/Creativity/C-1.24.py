"""Write a short Python function that counts the number of vowels in a given
character string."""

def count_vowel(str):
    vowel_list=["a","e","i","o","u"]
    count= 0
    for vowel in vowel_list:
        if vowel in str:
            count+=1
    return count

print(count_vowel("Lord Krishna"))

