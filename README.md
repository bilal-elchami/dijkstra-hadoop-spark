# Big Data's course Project

Master en informatique pour la finance - Université Paris-Dauphine

## Single-source shortest path problem

The task is to find shortest paths from a source node to all other nodes in the graph. This problem is solved by the Dijkstra’s algorithm, which is sequential.
The project has a double purpose. First get familiar with Dijkstra’s algorithm, then devise a MapReduce version of the algorithm. As you will realise, the process is actually iterative, so the identified MapReduce job must be iterated a certain number of times.
Provide both a Python-Hadoop streaming and Spark implementation of the algorithm, and test it on the simple graph data provided in classes.
Optional: perform scalability experiments as for previous projects. A single comparison on a reasonable big graph would be sufficient

## Formating data

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

copy code from [this file](spark.py)
