text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""



###se imprime el texto de la variable, al usar triple comilla se formatea todo el texto con todo y comillas.
##print(text);


##para separar el texto entre paraffos

sentences = text.split('. ')
##print(sentences);

####buscar palabras

for sentence in sentences:
    if  'temperature' in sentence :
        print(sentence)


