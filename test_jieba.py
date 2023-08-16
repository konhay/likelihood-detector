import jieba


# 分词
def stripdata(Test):
      seg_list = jieba.cut(Test)
      line = '/'.join(seg_list)
      word = stripword(line)
      print('\n关键字：\n'+word)
      return word


# 停用词分析
def stripword(seg):
      # 打开写入关键词的文件
      keyword = open('key_word.txt', 'w+', encoding='utf-8')
      wordlist = []

      # 获取停用词表
      # https://github.com/goto456/stopwords
      stop = open('stopword.txt', 'r+', encoding='utf-8')
      stopword = stop.read().split('\n')

      #遍历分词表
      for key in seg.split('/'):
            # 去除停用词，去除单字，去除重复词
            if not(key.strip() in stopword) and (len(key.strip())>1) and not(key.strip() in wordlist):
                  wordlist.append(key)
                  # print(key)
                  keyword.write(key+'\n')
      print('关键字个数：'+'\n'+str(len(wordlist)))
      #停用词去除END

      stop.close()
      keyword.close()
      return '/'.join(wordlist)


# 以本地文件进行测试
def test():
      Rawdata = open('raw.txt', 'r+')
      text = Rawdata.read()
      stripdata(text)
      Rawdata.close()

