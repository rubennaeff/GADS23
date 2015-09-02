# mrjob

`mrjob` lets you write MapReduce jobs in Python 2.6+ and run them on several platforms. You can:

- Write multi-step MapReduce jobs in pure Python
- Test on your local machine
- Run on a Hadoop cluster
- Run in the cloud using Amazon Elastic MapReduce (EMR)
- `mrjob` is licensed under the Apache License, Version 2.0.


### Installation

To get started, install with pip:

  pip install mrjob

and begin reading the tutorial of the [official documentation](https://pythonhosted.org/mrjob/).


### Example

In this folder, you'll find an example using `mrjob` in [mr_ex.py](./mr_ex.py).  The file actually contains three different examples, but two are commented out in the main clause. You can uncomment the line of your interest.

```python
if __name__ == '__main__':
    MRWC.run()
    # MRInvIdx.run()
    # MRWC2.run()
```

The folder also contains a couple input text files [wc_input.txt](./wc_input.txt) and [iidx_input.txt](./wc_input.txt).  Note that our example takes its input from the standard input, i.e., the console by default, so you'll need to pipe your input into our python script.

To run the example, type

  cat wc_input.txt | python mr_ex.py > test

The last part `> test` will save the standard output to a file.  This is optional, but it seperates the actual output with the many logging messages the script generates.

To view the output, type

  cat test

You will see:

  "carmen"  2
  "in"  6
  "is"  3
  "sandiego"  1
  "the" 5
  "where" 7
  "world" 4

