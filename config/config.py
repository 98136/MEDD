import os

bert_data_path = os.path.join(os.getcwd(), './data/xianyu/bert_data.json')
bert_tag_path = os.path.join(os.getcwd(), './data/xianyu/bert_tag.json')
# bert_model_path = os.path.join(os.getcwd(), './MultiBERT/pytorch_model.bin')
bert_vocab_path = os.path.join(os.getcwd(), './MultiBERT/vocab.txt')
# bert_vocab_path="bert-base-multilingual-cased"
# bert_model_path=os.path.join(os.getcwd(), './MultiBERT/')
bert_model_path="bert-base-multilingual-cased"
class params:
    bert_dim = 768
    output_dim = 23
    batch_size = 2
    adam_lr = 1e-5
    adamw_lr = 5e-5
    epoch = 20
    num_layers = 1
    rnn_dim = 200
