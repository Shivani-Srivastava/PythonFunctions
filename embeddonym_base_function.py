def embeddonym(wordlist, model_name = 'glove-wiki-gigaword-300'):
  import gensim.downloader as api
  import pandas as pd
  print('Loading model')
  model = api.load(model_name)
  print('Model loaded; getting wordlist ready to embed')

  if type(wordlist) == list:
    words = wordlist
  elif type(wordlist) == str:
    words = wordlist.split('\n')

  output_df = pd.DataFrame()
  error_words = []

  for word in words:
    try:
      emb_nym = model.most_similar(str(word))
      df = pd.DataFrame(emb_nym, columns = ['alt_word','similarity'])
      df.insert(0,'root_word',word)
      output_df = pd.concat([df,output_df])

      print(word, "added!")
    except:
      print(word," ran into an error.")
      error_words.append(word)
  print("Wordlist completed")
  return(output_df,error_words)