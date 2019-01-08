This is an attempt to replace LSTMs with gated CNNs. You can find a short summary about the paper on Gated CNNs [here](https://github.com/chennakeshava1998/research-paper-summaries/blob/master/notes/gatedCNN.md). 

This code is adapted from https://github.com/anantzoid/Language-Modeling-GatedCNN. The major differences are:
1. Causal convolutions are not required for NLQ2SQL usecase.
2. The amount of padding has been changed to k-1 instead of k/2, where k is the soze of the filter.
3. Pretrained word embeddings have been used. 