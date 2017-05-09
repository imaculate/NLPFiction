# word-rnn-tensorflow
Multi-layer Recurrent Neural Networks (LSTM, RNN) for word-level language models in Python using TensorFlow.

Mostly reused code from https://github.com/hunkim/word-rnn-tensorflow which was inspired from Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).

# Requirements
- [Tensorflow 1.1.0rc0](http://www.tensorflow.org)

# Basic Usage
To train with default parameters on the harry potter corpus, run:
```bash
python train.py --data_dir 'data/hp'
```

To sample from a trained model
```bash
python sample.py
```

To pick using beam search, use the `--pick` parameter. Beam search can be
further customized using the `--width` parameter, which sets the number of beams
to search with. For example:
```bash
python sample.py --pick 2 --width 4
```

# Sample output

### Word-RNN
```
# python sample.py -n 200

Rowena Cleansweep on one arm wall, and Moody’s voice had vanished and made a slight shiver, nodding over the pile onto his head, clearly as angrily. “Just try and get in, Harry,” said Ron. “But what did you survive? Tell me so many closest indeed. Now, I used more than before, the diary’s still chained potted methods o’ rat dung, To poison them started out. Bill — progress — Flint — how did I matter, Potter. It was problem to choose ter end this out now … it is not that,” she said shortly. “D’you think she’d been saying — Professor Borgin, everything you —”

“There are all weekend, they’re getting a bit anywhere more, Dad’s at least for your lack of eleven, this might like a single, countercurse this possible week, you alone …”

The clock right in the Great Hall was dragged into the air, and preparing more worse than the prefects have noticed their horror by killing Grimmauld Place from Ron.

He had training suddenly. His chair had recently begun to disentangle fire. It was full to nobody to die here, but so obvious, like every word of all the eve of the honor.”

“The diary had happened, how accurate Voldemort left
```
## Beam search

Beam search differs from the other `--pick` options in that it does not greedily
pick single words; rather, it expands the most promising nodes and keeps a
running score for each beam.

### Word-RNN (with beam search)
```
# python sample.py --prime "Rowena" -n 100 --pick 2 --width 4

Rowena kittens on the back of the back of the door. It looked as though he had been recounting his adventures of the previous friends. He had no choice. The Prime Minister had taken refuge in the middle of the wardrobe. Harry looked up at Harry.

“Grindelwald?”

Ignoring the remainder of the Order of the Phoenix,” she said. “Cedric Diggory.”

“Oh right,” said Harry.

His insides acted as though he had been having. It had been a very good audience; he longed to be a Squib. It was a stag. It was a stag. It was a stag. It was only a baby!”

Parvati tightened
```

### Word-RNN (without beam search)
```
# python sample.py --prime "Rowena" -n 100

Rowena kittens by the dropped she looked ready for closeness.

“No near the trophy dormitory, George gripped the binoculars. Buckbeak did say why Riddle was attacked by the world’s very funny feelings about for nonverbal questions about the man version of point eleven to Ron, Ron, having managed, finally, Ron, and Hermione left the infirmary and jabbed out Ginny, “you’ve been hiding for Draco Malfoy. We made him kill each other for you,” said Slughorn. “Oh, don’t you?”

“I — just saved anyone in brand-new writing. “I’m Ted, as Hermione was taking advantage when he had suffered agreement as it held up. Neville’s
```
