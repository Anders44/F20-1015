

# Lecture 18 - Operators and other stuff

This is kind of the "stuff" that is in python - with a few exceptions.

We need to cover some aerators.  We have used

| Operator | Specification |
|----------|----------------------|
| `+`      | add |
| `-`      | subtract |
| `*`      | multiply |
| `/`      | divide resulting in a float (remainder) |
| `//`     | divide integer result |
| `%`      | remainder from division |
| `==`     | equal |
| `!=`     | not equal |

Let's be much more specific in what these operators do.

```

a = 2
b = 3
c = 4

x = a + b * c

# Will Print 14 becasue 3 * 4 = 12, then add + 2
print ( f"x={x}" )


```

What we are seeing is "precedence" of operators.  Most languages
on a computer use a "precedence" process.  

<table border="1" cellspacing="0" width="50%" cellpadding="2" style="border-collapse: collapse" bordercolor="#111111">
            <tbody><tr>
              <th>
                <p align="center"><b>Operator</b></p>
              </th>
              <th>
                <b>Description</b></th>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">()</font></td>
              <td>Parentheses (grouping)</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2"><i>f</i>(args...)</font></td>
              <td>Function call</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2"><i>x</i>[index:index]</font></td>
              <td>Slicing</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2"><i>x</i>[index]</font></td>
              <td>Subscription</td>
            </tr>
            <tr>
              <td align="center"><i><font face="Courier New" size="2">
				x.attribute</font></i></td>
              <td>Attribute reference</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">**</font></td>
              <td>Exponentiation</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">~<i>x</i></font></td>
              <td>Bitwise not</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">+<i>x</i>, -<i>x</i></font></td>
              <td>Positive, negative</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">*, /,
              %</font></td>
              <td>Multiplication, division, remainder </td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">+,
              -</font></td>
              <td>Addition, subtraction</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">&lt;&lt;,
              &gt;&gt;</font></td>
              <td>Bitwise shifts</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">&amp;</font></td>
              <td>Bitwise AND</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">^</font></td>
              <td>Bitwise XOR</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">|</font></td>
              <td>Bitwise OR</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">in, not in, is, is not, &lt;, &lt;=,&nbsp;  
				&gt;,&nbsp; &gt;=,<br>
				&lt;&gt;, !=, ==</font></td>
              <td>Comparisons, membership, identity</td>
            </tr>
            <tr>              
			   <td align="center"><font face="Courier New" size="2">not <i>x</i></font></td>
              <td>Boolean NOT</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">and</font></td>
              <td>Boolean AND</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">or</font></td>
              <td>Boolean OR</td>
            </tr>
            <tr>
              <td align="center"><font face="Courier New" size="2">lambda</font></td>
              <td>Lambda expression</td>
            </tr>
            </tbody>
</table>
