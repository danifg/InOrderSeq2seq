This repository includes the code of the In-Order Sequence-to-Sequence Constituent Parser described in ACL paper [Enriched In-Order Linearization for Faster Sequence-to-Sequence Constituent Parsing](https://github.com/danifg/InOrderSeq2seq). The implementation is based on (https://github.com/LeonCrashCode/Encoder-Decoder-Parser) and reuses part of its code, including data preparation and evaluating scripts. 

This implementation requires [dynet2.0 library](https://github.com/clab/dynet) and you can find pretrained word embeddings for English and Chinese in https://github.com/LeonCrashCode/InOrderParser. 

### Building

    mkdir build
    cd build
    cmake .. -DEIGEN3_INCLUDE_DIR=/path/to/eigen -DBACKEND=cuda
    make    


### Data

To get shift-reduce linearizations:

    python ./scripts/get_inorder_oracle.py en [training data in bracketed format] [training data in bracketed format] > [training linearization]
    python ./scripts/get_inorder_oracle.py en [training data in bracketed format] [development data in bracketed format] > [development linearization]
    python ./scripts/get_inorder_oracle.py en [training data in bracketed format] [test data in bracketed format] > [test linearization]
    
### Training

    ./build/impl/constituent-parser --dynet-mem 1700 --train_file [training linearization] --dev_file [development linearization] --bracketed_file dev.trees --layers 2 --input_dim 64 --pos_dim 6 --bilstm_input_dim 100 --bilstm_hidden_dim 200 --attention_hidden_dim 50 --words_file ../embs/sskip.100.vectors --pretrained_dim 100 --action_dim 40 --train --use_pos --unk_strategy (--fast)

To train a model with the proposed deterministic attention technique, use the option --fast. 

### Greedy Decoding

    ./build/impl/constituent-parser --dynet-mem 1700 --train_file [training linearization] --test_file [test linearization] --bracketed_file test.trees --layers 2 --input_dim 64 --pos_dim 6 --bilstm_input_dim 100 --bilstm_hidden_dim 200 --attention_hidden_dim 50 --words_file ../embs/sskip.100.vectors --pretrained_dim 100 --action_dim 40 --use_pos  --unk_strategy (--fast) --model_file [BEST_MODEL]

### 10-Beam-search Decoding

    ./build/impl/constituent-parser-batch --dynet-mem 1700 --train_file [training linearization] --test_file [test linearization] --bracketed_file test.tree --layers 2 --input_dim 64 --pos_dim 6 --bilstm_input_dim 100 --bilstm_hidden_dim 200 --attention_hidden_dim 50 --words_file ../embs/sskip.100.vectors --pretrained_dim 100 --action_dim 40 --use_pos  --unk_strategy  --model_file [BEST_MODEL]

### Citation

To appear in ACL 2020.

### Acknowledgments

This work has received funding from the European Research Council (ERC), under the European Union's Horizon 2020 research and innovation programme (FASTPARSE, grant agreement No 714150), from the ANSWER-ASAP project (TIN2017-85160-C2-1-R) from MINECO, and from Xunta de Galicia (ED431B 2017/01, ED431G 2019/01).


