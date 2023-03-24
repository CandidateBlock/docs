Base Number Systems
===================

Humans have used various Base systems for numbers over the years. The majority of the world's
number systems are organised by tens, fives, and twenties, suggesting the use of the hands and 
feet in counting.

Base\ :sub:`10`
***************

Base\ :sub:`10` is the number system we mostly use, probably because we have 10 digits on our hands.

Symbols are: 0123456789 (Total 10)

Numbers are represented in an overflow system, with each column being 10 times larger than the last, due to base\ :sub:`10`. ::

    Units     = 10 ^ 0 =   1
    Tens      = 10 ^ 1 =  10
    Hundredes = 10 ^ 2 = 100
    etc...

Examples
--------

In the following examples values have their base defined by the subscript text as Number\ :sub:`Base`.

Value = 6\ :sub:`10`

+----------+------+-------+
| Hundreds | Tens | Units |
+----------+------+-------+
| 0        | 0    | 6     |
+----------+------+-------+

(100 x 0) + (10 x 0) + (1 x 6) = 6\ :sub:`10`

----

Value = 21\ :sub:`10`

+----------+------+-------+
| Hundreds | Tens | Units |
+----------+------+-------+
| 0        | 2    | 1     |
+----------+------+-------+

(100 x 0 ) + (10 x 2) + (1 x 1) = 21\ :sub:`10`

----

Value = 255\ :sub:`10`

+----------+------+-------+
| Hundreds | Tens | Units |
+----------+------+-------+
| 2        | 5    | 5     |
+----------+------+-------+

(100 x 2) + (10 x 5) + (1 x 5) = 255\ :sub:`10`

Base\ :sub:`2` (Binary)
***********************

Base\ :sub:`2` (Binary) is the number system computers use to store numbers as the electric current can only be in two states

1. Off, represented as Symbol 0
2. On, represented as Symbol 1

Symbols are: 01 (Total 2)

Numbers are represented in an overflow system, with each column being 2 times larger than the last, due to base\ :sub:`2`. ::

           1 = 2 ^ 0 =   1
          10 = 2 ^ 1 =   2
         100 = 2 ^ 2 =   4
        1000 = 2 ^ 3 =   8
       10000 = 2 ^ 4 =  16
      100000 = 2 ^ 5 =  32
     1000000 = 2 ^ 6 =  64
    10000000 = 2 ^ 7 = 128
    etc...

Examples
--------

Value = 6\ :sub:`10`

+-----+----+----+----+---+---+---+---+
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
+-----+----+----+----+---+---+---+---+
| 0   | 0  | 0  | 0  | 0 | 1 | 1 | 0 |
+-----+----+----+----+---+---+---+---+

| (128 x 0) + (64 x 0) + (32 x 0) + (16 x 0) + (8 x 0) + (4 x 1) + (2 x 1) + (1 x 0) = 00000110\ :sub:`2`
| 00000110\ :sub:`2` = 6\ :sub:`10`

----

Value = 21\ :sub:`10`

+-----+----+----+----+---+---+---+---+
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
+-----+----+----+----+---+---+---+---+
| 0   | 0  | 0  | 1  | 0 | 1 | 0 | 1 |
+-----+----+----+----+---+---+---+---+

| (128 x 0) + (64 x 0) + (32 x 0) + (16 x 1) + (8 x 0) + (4 x 1) + (2 x 0) + (1 x 1) = 00010101\ :sub:`2`
| 00010101\ :sub:`2` = 21\ :sub:`10`

----

Value = 255\ :sub:`10`

+-----+----+----+----+---+---+---+---+
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
+-----+----+----+----+---+---+---+---+
| 1   | 1  | 1  | 1  | 1 | 1 | 1 | 1 |
+-----+----+----+----+---+---+---+---+

| (128 x 1) + (64 x 1) + (32 x 1) + (16 x 1) + (8 x 1) + (4 x 1) + (2 x 1) + (1 x 1) = 11111111\ :sub:`2`
| 11111111\ :sub:`2` = 255\ :sub:`10`

.. code-block:: python
    
    """
    Python example to demonstrate how to convert from
    Decimal (base 10) to Binary (base 2) and back
    """

    decimal_num = 255
    print(f"Decimal: {decimal_num}, Binary: {bin(decimal_num)}")

    """
    Output
    Decimal: 255, Binary: 0b11111111
    Notice the 0b prefix, this is how python references Binary numbers
    You can also use the 0b prefix to use Binary literals
    """

    new_num_as_binary = 0b10101010
    # or new_num_as_binary = bin(170)
    # or new_num_as_binary = int('10101010', 2) <- 2 here means the base of the string 
    print(f"Decimal: {new_num_as_binary}, Binary: {bin(new_num_as_binary)}")

    """
    Output
    Decimal: 170, Binary: 0b10101010
    """

Base\ :sub:`16` (HEX / Hexadecimal)
***********************************

Base\ :sub:`16` (HEX / Hexadecimal) is the number system common when representing large numbers in computers. Base\ :sub:`16`  can be used to represent
large numbers with fewer digits and 16 is divisible by 2 (Base\ :sub:`2` [Binary] is used in Computers)

Symbols are: 0123456789ABCDEF (Total 16)

+-------------+---------+--------+
| Hexadecimal | Decimal | Binary |
+-------------+---------+--------+
| 0           | 0       | 0000   |
+-------------+---------+--------+
| 1           | 1       | 0001   |
+-------------+---------+--------+
| 2           | 2       | 0010   |
+-------------+---------+--------+
| 3           | 3       | 0011   |
+-------------+---------+--------+
| 4           | 4       | 0100   |
+-------------+---------+--------+
| 5           | 5       | 0101   |
+-------------+---------+--------+
| 6           | 6       | 0110   |
+-------------+---------+--------+
| 7           | 7       | 0111   |
+-------------+---------+--------+
| 8           | 8       | 1000   |
+-------------+---------+--------+
| 9           | 9       | 1001   |
+-------------+---------+--------+
| A           | 10      | 1010   |
+-------------+---------+--------+
| B           | 11      | 1011   |
+-------------+---------+--------+
| C           | 12      | 1100   |
+-------------+---------+--------+
| D           | 13      | 1101   |
+-------------+---------+--------+
| E           | 14      | 1110   |
+-------------+---------+--------+
| F           | 15      | 1111   |
+-------------+---------+--------+


Numbers are represented in an overflow system, with each column being 16 times larger than the last, due to base\ :sub:`16`. ::

        1 = 16 ^ 0 =    1
       10 = 16 ^ 1 =   16
      100 = 16 ^ 2 =  256
     1000 = 16 ^ 3 = 4096
    etc...

Examples
--------

Value = 6\ :sub:`10`

+------+-----+----+---+
| 4096 | 256 | 16 | 1 |
+------+-----+----+---+
| 0    | 0   | 0  | 6 |
+------+-----+----+---+

| (4096 x 0) + (256 x 0) + (16 x 0) + (1 x 6) = 0006\ :sub:`16`
| 0006\ :sub:`16` = 6\ :sub:`10`

----

Value = 21\ :sub:`10`

+------+-----+----+---+
| 4096 | 256 | 16 | 1 |
+------+-----+----+---+
| 0    | 0   | 1  | 5 |
+------+-----+----+---+

| (4096 x 0) + (256 x 0) + (16 x 1) + (1 x 5) = 0015\ :sub:`16`
| 0015\ :sub:`16` = 21\ :sub:`10`

----

Value = 255\ :sub:`10`

+------+-----+----+---+
| 4096 | 256 | 16 | 1 |
+------+-----+----+---+
| 0    | 0   | F  | F |
+------+-----+----+---+

| (4096 x 0) + (256 x 0) + (16 x 15) + (1 x 15) = 00FF\ :sub:`16`
| 00FF\ :sub:`16` = 255\ :sub:`10`

As you can see Hex is more efficient in symbolising longer numbers, compare the number 255\ :sub:`10` in the various bases. ::

    11111111 Base  2 (Binary)  8 Symbols/Characters
    255      Base 10 (Decimal) 3 Symbols/Characters
    FF       Base 16 (Hex)     2 Symbols/Characters

.. code-block:: python
    
    """
    Python example to demonstrate how to convert from
    Decimal (base 10) to Hexadecimal (base 16) and back
    """

    decimal_num = 255
    print(f"Decimal: {decimal_num}, Hexadecimal: {hex(decimal_num)}")

    """
    Output
    Decimal: 255, Hexadecimal: 0xff
    Notice the 0x prefix, this is how python references Hexadecimal numbers
    You can also use the 0x prefix to use Hexadecimal literals
    """

    new_num_as_binary = 0xaa
    # or new_num_as_binary = bin(170)
    # or new_num_as_binary = int('aa', 16) <- 16 here means the base of the string
    print(f"Decimal: {new_num_as_binary}, Hexadecimal: {hex(new_num_as_binary)}")

    """
    Output
    Decimal: 170, Hexadecimal: 0xaa
    """

Base\ :sub:`64`
***************

Base\ :sub:`64` is the number system used mostly in email for sending binary email attachments.
The binary data (Bytes) is required to be encoded into 7-Bit :ref:`computer-number-systems-ascii`
as the email protocol (SMTP) can only support 7-Bit ASCII.
See `Wikipedia - Base64 <https://en.wikipedia.org/wiki/Base64>`_ for more details.

Symbols are: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/ (Total 64)

    If you are unclear what a Byte sequence in Python is refere here :ref:`computer-number-systems-byte-string-prefix`.

.. code-block:: python
    
    """
    Python example to demonstrate how to convert from
    a Byte Array to and from Base64
    """

    import base64
    byte_sequence = b'Hello World!'
    b64_sequence = base64.b64encode(byte_sequence)
    print(f"byte_sequence: {byte_sequence}")
    print(f"byte_sequence in HEX: {byte_sequence.hex()}")
    print(f"b64_sequence in Base64: {b64_sequence}")

    """
    Output
    byte_sequence: b'Hello World!'
    byte_sequence in HEX: 48656c6c6f20576f726c6421
    b64_sequence in Base64: b'SGVsbG8gV29ybGQh'
    """

    decoded_byte_sequence = base64.b64decode(b64_sequence)
    print(f"decoded_byte_sequence: {decoded_byte_sequence}")

    """
    Output
    decoded_byte_sequence: b'Hello World!'
    """

Base\ :sub:`58`
***************

Base\ :sub:`58` is the number system we mostly use, probably because we have 10 digits on our hands.

Symbols are: 0 1 2 3 4 5 6 7 8 9 (Total 10)

Numbers are represented in an overflow system, with each column being 10 times larger than the last, due to base\ :sub:`10`. ::

    Units     = 10 ^ 0 =   1
    Tens      = 10 ^ 1 =  10
    Hundredes = 10 ^ 2 = 100
    etc...
