lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun'
}

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def scan(stuff):
    words = stuff.split()

    # 创建返回的句子（TOKEN, WORD对的列表）
    sentence = []

    # 遍历单词并确定它们的TOKEN类型
    for word in words:
        if is_number(word):
            sentence.append(('number', int(word)))
        else:
            # 获取单词的TOKEN类型，如果不在词汇表总，则为'ERROR'
            token_type = lexicon.get(word.lower(), 'error')
            # 将(TOKEN, WORD)元组添加到句子列表中
            sentence.append((token_type, word))
    
    return sentence