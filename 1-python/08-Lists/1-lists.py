freinds = [1, " omar ", True, False ,[1," abd al gwad"]]
print(freinds[0])   #indexing
print(freinds[-1])

print(freinds[1:3]) # [' omar ', True]
print(freinds[1:])  #[' omar ', True, False, [1, ' abd al gwad']]

freinds[0]=" Amr "  #change the value of an index
print(freinds[0])