import vioce
import change
import chat

if __name__ == '__main__':
    while True:
        vioce.my_record()
        token = change.get_token()
        try:
            mytext = change.get_word(token)
        except:
            print('失败了')
        print("我：" + mytext)
        #answers = chat.tulingRootBot
        voiceanserver = chat.answer(mytext)
        change.toVioce(voiceanserver)
        vioce.say()