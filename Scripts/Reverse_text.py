bows_list = ['()', '[]', '{}', '<>']
Arabic_letters = 'ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي' + '؟،؛ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ'

def swap(text, char1, char2, unused_char = u'\uffff'):
    text = text.replace(char1, unused_char)
    text = text.replace(char2, char1)
    text = text.replace(unused_char, char2)
    return text

def swap_edges_spaces(text):
    text = list(text)
    counter = 0
    while text[counter] == ' ':
        counter += 1
    while text[-1] == ' ':
        del text[-1]
        text.insert(0, ' ')
    for _ in range(counter):
        del text[0]
        text.append(' ')
    return ''.join(text)

def reverse_arabic(text):
    word, spaces = '', ''
    for char in text:
        if char in Arabic_letters:
            word += spaces
            word += char
            spaces = ''
        elif char == ' ':
            if word != '': spaces += char
        else:
            text = text.replace(word, word[::-1])
            spaces = ''
            word = ''
    if word != '': text = text.replace(word, word[::-1])
    return text

def script(text, start_command, end_command, case='whole text'):
    for bow in bows_list:
        if bow[0] not in (start_command + end_command) or bow[1] not in (start_command + end_command):
            text = swap(text, bow[0], bow[1])
    if start_command == '' or end_command == '':
        if case == 'whole text':
            text = text[::-1]
        else:
            text = test(text)
        return text
    else:
        text = text.replace(start_command, end_command)
        text_list = text.split(end_command)
        for _ in range(0, len(text_list)):
            if _%2 == 1:
                text_list[_] = start_command + text_list[_] + end_command
            else:        
                if case == 'whole text':
                    text_list[_] = text_list[_][::-1]
                else:
                    text_list[_] = reverse_arabic(text_list[_])
                text_list[_] = swap_edges_spaces(text_list[_])
        text = ''.join(text_list)
        return text