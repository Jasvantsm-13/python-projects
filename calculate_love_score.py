def calculate_love_score(name1, name2):
    # Combine names and make them lowercase
    combined_names = (name1 + name2).lower()

    # Count letters in "TRUE"
    t = combined_names.count('t')
    r = combined_names.count('r')
    u = combined_names.count('u')
    e = combined_names.count('e')
    true_total = t + r + u + e

    # Count letters in "LOVE"
    l = combined_names.count('l')
    o = combined_names.count('o')
    v = combined_names.count('v')
    e2 = combined_names.count('e')  # Count 'e' again
    love_total = l + o + v + e2

    # Combine both totals to form the love score
    love_score = int(str(true_total) + str(love_total))

    # ✅ This is the exact expected output format
    print(love_score)
#enter here your name 
calculate_love_score("jeet", "nency")
