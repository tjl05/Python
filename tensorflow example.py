# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:50:30 2018

@author: Seb
"""


import tensorflow as tf


const1 = tf.constant([[1,2,3], [1,2,3]]);

const2 = tf.constant([[3,4,5], [3,4,5]]);



result = tf.add(const1, const2);


with tf.Session() as sess:

  output = sess.run(result)

  print(output)
  