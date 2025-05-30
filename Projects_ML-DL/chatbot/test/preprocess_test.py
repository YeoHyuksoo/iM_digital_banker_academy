import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing

sent = "내일 오전 10시에 짬뽕 주문하고 싶어ㅋㅋ"

p = Preprocess(userdic = '../utils/user_dic.tsv')
pos = p.pos(sent)
print(pos)
keywords = p.get_keywords(pos, without_tag=False)
print(keywords)
keywords = p.get_keywords(pos, without_tag=True)
print(keywords)