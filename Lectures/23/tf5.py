
import tensorflow as tf

v3 = tf.constant(3)
v5 = tf.constant(5)
b = tf.math.add(v3,v5)
print_output = tf.print(b)

v2 = tf.constant(2)
c = tf.math.multiply ( print_output, v2 )

print(c)
