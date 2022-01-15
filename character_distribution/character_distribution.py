from collections import Counter
import pinyin

class CharacterDistribution:
    filename = 'doc.txt'
    punctuation = ['，', '。', ' ', '；', '\n']
    token_count = 0
    percent_token_count = 0
    n = 0
    text = ''

    def __init__(self):
        document = open(self.filename, 'r')
        self.text = document.read()
        for p in self.punctuation:
            self.text = self.text.replace(p, '')
        document.close()

    def make_freq_chart(self):
        char_freq_dist = Counter(self.text)
        for key in char_freq_dist:
            self.token_count+=char_freq_dist[key]
        print("Enter an integer 1-99: ", end='')
        proportion = int(input())
        proportion/=100
        chars_list = open('chars_list.txt', 'w')
        while self.percent_token_count/self.token_count < proportion:
            char = char_freq_dist.most_common()[self.n]
            c = f'{char[0]}: {pinyin.get(char[0])}\n'
            print(c, end='')
            chars_list.write(c)
            self.percent_token_count+=int(char_freq_dist[char[0]])
            self.n+=1
        chars_list.close()


def test():
    char_freqs = CharacterDistribution()
    char_freqs.make_freq_chart()

test()
