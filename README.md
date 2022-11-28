# :books: eureka-python

![banner](./docs/banner.png "eureka-python")

A curated list of [Python](https://www.python.org/) solutions for problems regarding algorithms and data structures! The project is shipped with a testing environment for learning and experimenting. Tests are written in [pytest](https://docs.pytest.org/en/7.1.x/) and mocks in [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/). [PyHamcrest](https://pyhamcrest.readthedocs.io/en/latest/) matchers are used extensively to improve code readability.

## :pushpin: Installation

```shell
$ git clone https://github.com/leowajda/eureka-python.git # clone the repository from GitHub
$ cd eureka-python                                        # navigate to root directory
$ python3 -m venv ./venv                                  # setup venv
$ source venv/bin/activate                                # activate it
$ pip install -r requirements.txt                         # install dependencies
$ pytest                                                  # (optional) run all the tests
```

## :pencil2: Index

|  ID  |                                                                       Name                                                                        |                                                                                                          Python                                                                                                           |
|:----:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  1   |                                                 [Two Sum](https://leetcode.com/problems/two-sum/)                                                 | [:arrow_up_down:](https://github.com/leowajda/eureka-python/blob/master/src/array/iterative/lc_0001.py) [:arrows_counterclockwise:](https://github.com/leowajda/eureka-python/blob/master/src/array/recursive/lc_0001.py) |
|  34  | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |                                                          [:arrow_up_down:](https://github.com/leowajda/eureka-python/blob/master/src/array/iterative/lc_0034.py)                                                          |
|  79  |                                             [Word Search](https://leetcode.com/problems/word-search/)                                             |                                                     [:arrows_counterclockwise:](https://github.com/leowajda/eureka-python/blob/master/src/graph/recursive/lc_0079.py)                                                     |
|  91  |                                             [Decode Ways](https://leetcode.com/problems/decode-ways/)                                             |                                                         [:arrow_up_down:](https://github.com/leowajda/eureka-python/blob/master/src/strings/iterative/lc_0091.py)                                                         |
| 104  |                            [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)                            |                                                  [:arrows_counterclockwise:](https://github.com/leowajda/eureka-python/blob/master/src/binary_tree/recursive/lc_0104.py)                                                  |
| 110  |                                    [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)                                    |                                                  [:arrows_counterclockwise:](https://github.com/leowajda/eureka-python/blob/master/src/binary_tree/recursive/lc_0110.py)                                                  |
| 162  |                                       [Find Peak Element](https://leetcode.com/problems/find-peak-element/)                                       |                                                          [:arrow_up_down:](https://github.com/leowajda/eureka-python/blob/master/src/array/iterative/lc_0162.py)                                                          |
| 297  |                   [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)                   |                                                  [:arrows_counterclockwise:](https://github.com/leowajda/eureka-python/blob/master/src/binary_tree/recursive/lc_0297.py)                                                  |
| 509  |                                        [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)                                        |                                                          [:arrow_up_down:](https://github.com/leowajda/eureka-python/blob/master/src/math/iterative/lc_0509.py)                                                           |
| 704  |                                           [Binary Search](https://leetcode.com/problems/binary-search/)                                           | [:arrow_up_down:](https://github.com/leowajda/eureka-python/blob/master/src/array/iterative/lc_0704.py) [:arrows_counterclockwise:](https://github.com/leowajda/eureka-python/blob/master/src/array/recursive/lc_0704.py) |
| 1137 |                                  [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)                                  |                                                          [:arrow_up_down:](https://github.com/leowajda/eureka-python/blob/master/src/math/iterative/lc_1137.py)                                                           |
| 1448 |                         [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)                         |                                                  [:arrows_counterclockwise:](https://github.com/leowajda/eureka-python/blob/master/src/binary_tree/recursive/lc_1448.py)                                                  |