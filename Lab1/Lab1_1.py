def test():
    assert max_word("Ana are mere si pere") == "si"
    assert max_word("Si x si y") == "y"
    assert max_word("")==""
def max_word(text):
    #input: text-un sir de caractere
    #output: ans-un cuvant 
    #functia parcurge cuvintele din sir si cauta cel mai mare cuvant din punct de vedere alfabetic
    text = text.split();
    ans = ""

    for word in text:
        if word.lower() > ans.lower():
            ans = word
    
    return ans
test()
#citesc sirul
text = input().strip()
#afisez cuvantul cel mai mare(aflabetic)
print(max_word(text))