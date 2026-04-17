
def count_words(text):
    
    text = text.lower()
    
    # Chain replace() to remove punctuation
    clean_text = text.replace(",", "").replace(".", "").replace("!", "").replace(":", "")
    clean_text = clean_text.replace("?", "").replace("(", "").replace(")", "")
    
    words = clean_text.split()
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

sample_text = " Dans un coin oublié d’un vieux laboratoire, vivait un petit ordinateur gris qui passait ses journées à calculer sagement,"
" afficher des tableaux et clignoter avec fierté. Il n’était ni rapide, ni puissant, mais il était heureux de rendre service."
" Un matin pourtant, quelque chose changea. Une erreur minuscule apparut dans sa mémoire, puis une autre, puis cent autres,"
" comme de petites fissures dans ses pensées électroniques. Les chiffres qu’il connaissait par cœur se mélangeaient, les "
"lettres glissaient hors de leurs mots, et même l’heure à l’écran semblait hésiter, incapable de se souvenir du moment "
"présent. Le petit ordinateur commença à douter de tout : de ses programmes, de ses fichiers, même de son nom de machine."
" Il ouvrait des dossiers qu’il ne reconnaissait plus et lançait des messages d’erreur comme des appels au secours. Ses"
" ventilateurs tournaient avec une tristesse sourde, semblable à un soupir, tandis que son écran devenait de plus en plus "
"pâle. Il avait l’impression que son esprit se dispersait dans les circuits, comme une pluie de données perdues dans le"
" silence. À la fin de la journée, il resta immobile, la lumière de veille tremblant faiblement, seul avec ses souvenirs "
"corrompus, incapable de comprendre comment il avait pu se perdre lui-même."

print(count_words(sample_text))