# K-means clustering

The most popular clustering method, implemented in python 

![screenshot](http://bayanbox.ir/view/6491693936731419361/2019-06-04-144504.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### What's K-means?

It is an unsupervised learning algorithm (meaning there are no target labels) that allows you to identify similar groups or clusters of data points within your data.

### Built With

* [Python 3](https://www.python.org/download/releases/3.0/)
* [Matplotlib](https://matplotlib.org)
 
### Prerequisites

Install Matplotlib with the following commands:

```
python -m pip install -U pip
python -m pip install -U matplotlib
```

## The Algorithm

The algorithm will categorize the items into k groups of similarity. To calculate that similarity, we will use the euclidean distance as measurement.
The algorithm works as follows:

```
1-First we initialize k points, called means, randomly.
2-We categorize each item to its closest mean and we update the mean’s coordinates, which are the averages of the items categorized in that mean so far.
3-We repeat the process for a given number of iterations and at the end, we have our clusters.
```
	
### Used equations

Euclidean distance:

![distance](https://wikimedia.org/api/rest_v1/media/math/render/svg/795b967db2917cdde7c2da2d1ee327eb673276c0)

Average(calculating new centroid for each cluster):

![average](https://wikimedia.org/api/rest_v1/media/math/render/svg/dc56506f7a018c71acd48c3942b5c2e217ab6f08)

## Authors

* **Arman** - *Initial work*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

