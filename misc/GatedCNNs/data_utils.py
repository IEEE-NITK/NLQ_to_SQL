import numpy as np
import collections
import os
import json

def read_words(conf):
    words = []
    for file in os.listdir(conf.data_dir):
        with open(os.path.join(conf.data_dir, file), 'r') as f:
            for line in f.readlines():
                tokens = line.split()
                # NOTE Currently, only sentences with a fixed size are chosen
                # to account for fixed convolutional layer size.

                # Initial part of the sentence is added with (k - 1) tokens. 
                if len(tokens) == conf.context_size-2:
                    words.extend((['<pad>']*(conf.filter_h - 1)) + ['<s>'] + tokens + ['</s>']) return words

# TODO: Use pre-trained word-vectors
def index_words(words, conf):
    word_counter = collections.Counter(words).most_common(conf.vocab_size-1)

    word_emb = load_word_emb('glove/glove.%dB.%dd.txt'%(B_word,N_word), use_small=USE_SMALL)


    # All the rare words are replaced with the zero vector.
    word_to_idx = {'<unk>': 0}
    idx_to_word = {0: '<unk>'}
    for i,_ in enumerate(word_counter):
        word_to_idx[_[0]] = i+1
        idx_to_word[i+1] = _[0]
    data = []
    for word in words:
        idx = word_to_idx.get(word)
        idx = idx if idx else word_to_idx['<unk>']
        data.append(idx)

    emb_array = np.stack(embs, axis=0)
    with open('glove/word2idx.json', 'w') as outf:
        json.dump(word_to_idx, outf)
    
    return np.array(data), word_to_idx, idx_to_word

def load_word_emb(file_name, load_used=False, use_small=False):
    if not load_used:
        print ('Loading word embedding from %s'%file_name)
        ret = {}
        with open(file_name) as inf:
            for idx, line in enumerate(inf):
                if (use_small and idx >= 5000):
                    break
                info = line.strip().split(' ')
                if info[0].lower() not in ret:
                    ret[info[0]] = np.array(map(lambda x:float(x), info[1:]))
        return ret
    else:
        print ('Load used word embedding')
        with open('glove/word2idx.json') as inf:
            w2i = json.load(inf)
        with open('glove/usedwordemb.npy') as inf:
            word_emb_val = np.load(inf)
        return w2i, word_emb_val


def create_batches(data, conf):
    conf.num_batches = int(len(data) / (conf.batch_size * conf.context_size))
    data = data[:conf.num_batches * conf.batch_size * conf.context_size]


    ydata, xdata = load_data(data + '/sql', data + '/table')
    # ydata = np.copy(data)

    # ydata[:-1] = xdata[1:]
    # ydata[-1] = xdata[0]
    x_batches = np.split(xdata.reshape(conf.batch_size, -1), conf.num_batches, 1)
    y_batches = np.split(ydata.reshape(conf.batch_size, -1), conf.num_batches, 1)

    for i in xrange(conf.num_batches):
        x_batches[i] = x_batches[i][:,:-1]
        y_batches[i] = y_batches[i][:,:-1]
    return x_batches, y_batches, conf

def load_data(sql_paths, table_paths, use_small=False):
    if not isinstance(sql_paths, list):
        sql_paths = (sql_paths, )
    if not isinstance(table_paths, list):
        table_paths = (table_paths, )
    sql_data = []
    table_data = {}

    max_col_num = 0
    for SQL_PATH in sql_paths:
        print "Loading data from %s"%SQL_PATH
        with open(SQL_PATH) as inf:
            for idx, line in enumerate(inf):
                if use_small and idx >= 1000:
                    break
                sql = json.loads(line.strip())
                sql_data.append(sql)

    for TABLE_PATH in table_paths:
        print "Loading data from %s"%TABLE_PATH
        with open(TABLE_PATH) as inf:
            for line in inf:
                tab = json.loads(line.strip())
                table_data[tab[u'id']] = tab

    for sql in sql_data:
        assert sql[u'table_id'] in table_data

    return sql_data, table_data


def get_batch(x_batches, y_batches, batch_idx):
    x, y = x_batches[batch_idx], y_batches[batch_idx]
    batch_idx += 1
    if batch_idx >= len(x_batches):
        batch_idx = 0
    return x, y.reshape(-1,1), batch_idx


def prepare_data(conf):
	words = read_words(conf)
	data, word_to_idx, idx_to_word = index_words(words, conf)
	x_batches, y_batches, conf = create_batches(data, conf)

	del words
	del data

	return x_batches, y_batches
