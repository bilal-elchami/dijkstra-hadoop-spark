# Dijkstra’s algorithm - Hadoop Python

This project was developed during my masters at Paris-Dauphine university. You can find [here](document/report.pdf) the project report.

## Single-source shortest path problem

The purpose of this algorithm is to find shortest path of a source node to all other nodes in a graph. This problem is solved by the Dijkstra’s algorithm.
This project has double purposes. First, to get familiar with Dijkstra’s algorithm, then implement a MapReduce version of it. The algorithm is iterative, so the identified MapReduce job must be iterated several times to find the final solution.
We provided a Python-Hadoop streaming and Spark (Python) implementations of the algorithm. 

Optional: perform scalability experiments. A single comparison on a reasonable big graph would be sufficient.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif">
</p>

## Formating data

This script takes data and convert it to the compatible format of the algorithm. For specific data formats, you can implement your own map job formatter.

```sh
cat data/new-data.dat | sort | python/prepare.py 1 >> data/input.dat
```

## Solving a graph using Dijkstra’s algorithm

### Python

```sh
# Executing python MapReduce job 3 times with the cat command
$ cat data/input.dat | python/mapper.py | sort | python/reducer.py | \
                       python/mapper.py | sort | python/reducer.py | \
                       python/mapper.py | sort | python/reducer.py
```

### Python-Hadoop streaming

```sh
# Executing hadoop streaming MapReduce Job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar \
                    -input data/input.dat -output output \
                    -file python/mapper.py -mapper mapper.py \
                    -file python/reducer.py -reducer reducer.py
```

### Spark

You can copy the source code in [this file](spark.py) and paste it in pyspark commandline.
TODO: implement spark submit version.

### Scalability experiment

We used facebook data for the Scalability experiment. You can download it [here](https://snap.stanford.edu/data/egonets-Facebook.html).

### Hadoop Streaming Job Chaining

Check this [repository](https://github.com/bilal-elchami/hadoop_streaming_job_chaining) to chain Map Reduce streaming jobs and run them multiples time (iterations).
