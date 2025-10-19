meme_dict = {
            "67": "Niche bir meme",
            "41": "41 UNCLE",
            "Dudeman": "Dracula dudeman"
            }
print(meme_dict)
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print("Kafanıza takılan bir şey varsa memedicte geri dönünüz")
else:
    print("Böyle bir meme mevcut değil")
