Computer Number Systems
=======================

A single digit in a computer is call a ``Bit``.
Bits are organised in to structures as multiples of Base\ :sub:`2` (Binary).
In the previous examples we have 8-Bits, which is called a ``Byte``.
The table blow shows as the number of Bits grows (multiples of base\ :sub:`2`) the names change.

Bits
****

+----------------+--------+
| Number of Bits | Name   |
+----------------+--------+
| 1              | Bit    |
+----------------+--------+
| 4              | Nibble |
+----------------+--------+
| 8              | Byte   |
+----------------+--------+


Bytes
*****

Once we get to 8 or more ``Bits`` the naming convention switches to ``Bytes``, which are made up of 8-Bits.
The table below shows as the number of Bytes grow the names change.

+-----------------+-------------+----------------+---------------+
| Number of Bytes | Name        | Number of Bits | Type          |
+-----------------+-------------+----------------+---------------+
| 1               | Byte        | 8              | Char          |
+-----------------+-------------+----------------+---------------+
| 2               | Word        | 16             | Int           | 
+-----------------+-------------+----------------+---------------+
| 8               | Double Word | 32             | Long Integer  | 
+-----------------+-------------+----------------+---------------+
| 16              | Quad Word   | 64             | Long Long Int |
+-----------------+-------------+----------------+---------------+

.. _computer-number-systems-ascii:

ASCII
*****

ASCII, stands for American Standard Code for Information Interchange. It is a 7-bit character code where each individual bit represents a unique character. 

ASCII Control Characters (0-31)
-------------------------------

The first 32 characters in the ASCII-table are unprintable control codes and are used to control peripherals such as printers.

+-----+----------+-----+--------+-----------------------------+
| DEC | BIN      | HEX | Symbol | Description                 |
+-----+----------+-----+--------+-----------------------------+
| 0   | 00000000 | 00  | NUL    | Null character              |
+-----+----------+-----+--------+-----------------------------+
| 1   | 00000001 | 01  | SOH    | Start of Heading            |
+-----+----------+-----+--------+-----------------------------+
| 2   | 00000010 | 02  | STX    | Start of Text               |
+-----+----------+-----+--------+-----------------------------+
| 3   | 00000011 | 03  | ETX    | End of Text                 |
+-----+----------+-----+--------+-----------------------------+
| 4   | 00000100 | 04  | EOT    | End of Transmission         |
+-----+----------+-----+--------+-----------------------------+
| 5   | 00000101 | 05  | ENQ    | Enquiry                     |
+-----+----------+-----+--------+-----------------------------+
| 6   | 00000110 | 06  | ACK    | Acknowledge                 |
+-----+----------+-----+--------+-----------------------------+
| 7   | 00000111 | 07  | BEL    | Bell, Alert                 |
+-----+----------+-----+--------+-----------------------------+
| 8   | 00001000 | 08  | BS     | Backspace                   |
+-----+----------+-----+--------+-----------------------------+
| 9   | 00001001 | 09  | HT     | Horizontal Tab              |
+-----+----------+-----+--------+-----------------------------+
| 10  | 00001010 | 0A  | LF     | Line Feed                   |
+-----+----------+-----+--------+-----------------------------+
| 11  | 00001011 | 0B  | VT     | Vertical Tabulation         |
+-----+----------+-----+--------+-----------------------------+
| 12  | 00001100 | 0C  | FF     | Form Feed                   |
+-----+----------+-----+--------+-----------------------------+
| 13  | 00001101 | 0D  | CR     | Carriage Return             |
+-----+----------+-----+--------+-----------------------------+
| 14  | 00001110 | 0E  | SO     | Shift Out                   |
+-----+----------+-----+--------+-----------------------------+
| 15  | 00001111 | 0F  | SI     | Shift In                    |
+-----+----------+-----+--------+-----------------------------+
| 16  | 00010000 | 10  | DLE    | Data Link Escape            |
+-----+----------+-----+--------+-----------------------------+
| 17  | 00010001 | 11  | DC1    | Device Control One (XON)    |
+-----+----------+-----+--------+-----------------------------+
| 18  | 00010010 | 12  | DC2    | Device Control Two          |
+-----+----------+-----+--------+-----------------------------+
| 19  | 00010011 | 13  | DC3    | Device Control Three (XOFF) |
+-----+----------+-----+--------+-----------------------------+
| 20  | 00010100 | 14  | DC4    | Device Control Four         |
+-----+----------+-----+--------+-----------------------------+
| 21  | 00010101 | 15  | NAK    | Negative Acknowledge        |
+-----+----------+-----+--------+-----------------------------+
| 22  | 00010110 | 16  | SYN    | Synchronous Idle            |
+-----+----------+-----+--------+-----------------------------+
| 23  | 00010111 | 17  | ETB    | End of Transmission Block   |
+-----+----------+-----+--------+-----------------------------+
| 24  | 00011000 | 18  | CAN    | Cancel                      |
+-----+----------+-----+--------+-----------------------------+
| 25  | 00011001 | 19  | EM     | End of medium               |
+-----+----------+-----+--------+-----------------------------+
| 26  | 00011010 | 1A  | SUB    | Substitute                  |
+-----+----------+-----+--------+-----------------------------+
| 27  | 00011011 | 1B  | ESC    | Escape                      |
+-----+----------+-----+--------+-----------------------------+
| 28  | 00011100 | 1C  | FS     | File Separator              |
+-----+----------+-----+--------+-----------------------------+
| 29  | 00011101 | 1D  | GS     | Group Separator             |
+-----+----------+-----+--------+-----------------------------+
| 30  | 00011110 | 1E  | RS     | Record Separator            |
+-----+----------+-----+--------+-----------------------------+
| 31  | 00011111 | 1F  | US     | Unit Separator              |
+-----+----------+-----+--------+-----------------------------+


ASCII Printable Characters (32-127)
-----------------------------------

Codes 32-127 are common for all the different variations of the ASCII table, they are called printable characters, represent letters, digits, punctuation marks, and a few miscellaneous symbols.

+-----+----------+-----+--------+----------------------------------------+
| DEC | BIN      | HEX | Symbol | Description                            |
+-----+----------+-----+--------+----------------------------------------+
| 32  | 00100000 | 20  | SP     | Space                                  |
+-----+----------+-----+--------+----------------------------------------+
| 33  | 00100001 | 21  | !      | Exclamation mark                       |
+-----+----------+-----+--------+----------------------------------------+
| 34  | 00100010 | 22  | "      | Double quotes                          |
+-----+----------+-----+--------+----------------------------------------+
| 35  | 00100011 | 23  | #      | Number sign                            |
+-----+----------+-----+--------+----------------------------------------+
| 36  | 00100100 | 24  | $      | Dollar                                 |                  
+-----+----------+-----+--------+----------------------------------------+
| 37  | 00100101 | 25  | %      | Per cent sign                          |
+-----+----------+-----+--------+----------------------------------------+
| 38  | 00100110 | 26  | &      | Ampersand                              |
+-----+----------+-----+--------+----------------------------------------+
| 39  | 00100111 | 27  | '      | Single quote                           |
+-----+----------+-----+--------+----------------------------------------+
| 40  | 00101000 | 28  | (      | Open parenthesis                       |
+-----+----------+-----+--------+----------------------------------------+
| 41  | 00101001 | 29  | )      | Close parenthesis                      |
+-----+----------+-----+--------+----------------------------------------+
| 42  | 00101010 | 2A  | \*     | Asterisk                               |
+-----+----------+-----+--------+----------------------------------------+
| 43  | 00101011 | 2B  | \+     | Plus                                   |
+-----+----------+-----+--------+----------------------------------------+
| 44  | 00101100 | 2C  | ,      | Comma                                  |
+-----+----------+-----+--------+----------------------------------------+
| 45  | 00101101 | 2D  | \-     | Hyphen-minus                           |
+-----+----------+-----+--------+----------------------------------------+
| 46  | 00101110 | 2E  | .      | Period, dot or full stop               |
+-----+----------+-----+--------+----------------------------------------+
| 47  | 00101111 | 2F  | /      | Slash or divide                        |
+-----+----------+-----+--------+----------------------------------------+
| 48  | 00110000 | 30  | 0      | Zero                                   |
+-----+----------+-----+--------+----------------------------------------+
| 49  | 00110001 | 31  | 1      | One                                    |
+-----+----------+-----+--------+----------------------------------------+
| 50  | 00110010 | 32  | 2      | Two                                    |
+-----+----------+-----+--------+----------------------------------------+
| 51  | 00110011 | 33  | 3      | Three                                  |
+-----+----------+-----+--------+----------------------------------------+
| 52  | 00110100 | 34  | 4      | Four                                   |
+-----+----------+-----+--------+----------------------------------------+
| 53  | 00110101 | 35  | 5      | Five                                   |
+-----+----------+-----+--------+----------------------------------------+
| 54  | 00110110 | 36  | 6      | Six                                    |
+-----+----------+-----+--------+----------------------------------------+
| 55  | 00110111 | 37  | 7      | Seven                                  |
+-----+----------+-----+--------+----------------------------------------+
| 56  | 00111000 | 38  | 8      | Eight                                  |
+-----+----------+-----+--------+----------------------------------------+
| 57  | 00111001 | 39  | 9      | Nine                                   |
+-----+----------+-----+--------+----------------------------------------+
| 58  | 00111010 | 3A  | :      | Colon                                  |
+-----+----------+-----+--------+----------------------------------------+
| 59  | 00111011 | 3B  | ;      | Semicolon                              |
+-----+----------+-----+--------+----------------------------------------+
| 60  | 00111100 | 3C  | <      | Less than                              |
+-----+----------+-----+--------+----------------------------------------+
| 61  | 00111101 | 3D  | =      | Equals                                 |
+-----+----------+-----+--------+----------------------------------------+
| 62  | 00111110 | 3E  | >      | Greater than                           |
+-----+----------+-----+--------+----------------------------------------+
| 63  | 00111111 | 3F  | ?      | Question mark                          |
+-----+----------+-----+--------+----------------------------------------+
| 64  | 01000000 | 40  | @      | At sign                                |
+-----+----------+-----+--------+----------------------------------------+
| 65  | 01000001 | 41  | A      | Uppercase A                            |
+-----+----------+-----+--------+----------------------------------------+
| 66  | 01000010 | 42  | B      | Uppercase B                            |
+-----+----------+-----+--------+----------------------------------------+
| 67  | 01000011 | 43  | C      | Uppercase C                            |
+-----+----------+-----+--------+----------------------------------------+
| 68  | 01000100 | 44  | D      | Uppercase D                            |
+-----+----------+-----+--------+----------------------------------------+
| 69  | 01000101 | 45  | E      | Uppercase E                            |
+-----+----------+-----+--------+----------------------------------------+
| 70  | 01000110 | 46  | F      | Uppercase F                            |
+-----+----------+-----+--------+----------------------------------------+
| 71  | 01000111 | 47  | G      | Uppercase G                            |
+-----+----------+-----+--------+----------------------------------------+
| 72  | 01001000 | 48  | H      | Uppercase H                            |
+-----+----------+-----+--------+----------------------------------------+
| 73  | 01001001 | 49  | I      | Uppercase I                            |
+-----+----------+-----+--------+----------------------------------------+
| 74  | 01001010 | 4A  | J      | Uppercase J                            |
+-----+----------+-----+--------+----------------------------------------+
| 75  | 01001011 | 4B  | K      | Uppercase K                            |
+-----+----------+-----+--------+----------------------------------------+
| 76  | 01001100 | 4C  | L      | Uppercase L                            |
+-----+----------+-----+--------+----------------------------------------+
| 77  | 01001101 | 4D  | M      | Uppercase M                            |
+-----+----------+-----+--------+----------------------------------------+
| 78  | 01001110 | 4E  | N      | Uppercase N                            |
+-----+----------+-----+--------+----------------------------------------+
| 79  | 01001111 | 4F  | O      | Uppercase O                            |
+-----+----------+-----+--------+----------------------------------------+
| 80  | 01010000 | 50  | P      | Uppercase P                            |
+-----+----------+-----+--------+----------------------------------------+
| 81  | 01010001 | 51  | Q      | Uppercase Q                            |
+-----+----------+-----+--------+----------------------------------------+
| 82  | 01010010 | 52  | R      | Uppercase R                            |
+-----+----------+-----+--------+----------------------------------------+
| 83  | 01010011 | 53  | S      | Uppercase S                            |
+-----+----------+-----+--------+----------------------------------------+
| 84  | 01010100 | 54  | T      | Uppercase T                            |
+-----+----------+-----+--------+----------------------------------------+
| 85  | 01010101 | 55  | U      | Uppercase U                            |
+-----+----------+-----+--------+----------------------------------------+
| 86  | 01010110 | 56  | V      | Uppercase V                            |
+-----+----------+-----+--------+----------------------------------------+
| 87  | 01010111 | 57  | W      | Uppercase W                            |
+-----+----------+-----+--------+----------------------------------------+
| 88  | 01011000 | 58  | X      | Uppercase X                            |
+-----+----------+-----+--------+----------------------------------------+
| 89  | 01011001 | 59  | Y      | Uppercase Y                            |
+-----+----------+-----+--------+----------------------------------------+
| 90  | 01011010 | 5A  | Z      | Uppercase Z                            |
+-----+----------+-----+--------+----------------------------------------+
| 91  | 01011011 | 5B  | [      | Opening bracket                        |
+-----+----------+-----+--------+----------------------------------------+
| 92  | 01011100 | 5C  | \\     | Backslash                              |
+-----+----------+-----+--------+----------------------------------------+
| 93  | 01011101 | 5D  | ]      | Closing bracket                        |
+-----+----------+-----+--------+----------------------------------------+
| 94  | 01011110 | 5E  | ^      | Caret - circumflex                     |
+-----+----------+-----+--------+----------------------------------------+
| 95  | 01011111 | 5F  | _      | Underscore                             |
+-----+----------+-----+--------+----------------------------------------+
| 96  | 01100000 | 60  | \`     | Grave accent                           |
+-----+----------+-----+--------+----------------------------------------+
| 97  | 01100001 | 61  | a      | Lowercase a                            |
+-----+----------+-----+--------+----------------------------------------+
| 98  | 01100010 | 62  | b      | Lowercase b                            |
+-----+----------+-----+--------+----------------------------------------+
| 99  | 01100011 | 63  | c      | Lowercase c                            |
+-----+----------+-----+--------+----------------------------------------+
| 100 | 01100100 | 64  | d      | Lowercase d                            |
+-----+----------+-----+--------+----------------------------------------+
| 101 | 01100101 | 65  | e      | Lowercase e                            |
+-----+----------+-----+--------+----------------------------------------+
| 102 | 01100110 | 66  | f      | Lowercase f                            |
+-----+----------+-----+--------+----------------------------------------+
| 103 | 01100111 | 67  | g      | Lowercase g                            |
+-----+----------+-----+--------+----------------------------------------+
| 104 | 01101000 | 68  | h      | Lowercase h                            |
+-----+----------+-----+--------+----------------------------------------+
| 105 | 01101001 | 69  | i      | Lowercase i                            |
+-----+----------+-----+--------+----------------------------------------+
| 106 | 01101010 | 6A  | j      | Lowercase j                            |
+-----+----------+-----+--------+----------------------------------------+
| 107 | 01101011 | 6B  | k      | Lowercase k                            |
+-----+----------+-----+--------+----------------------------------------+
| 108 | 01101100 | 6C  | l      | Lowercase l                            |
+-----+----------+-----+--------+----------------------------------------+
| 109 | 01101101 | 6D  | m      | Lowercase m                            |
+-----+----------+-----+--------+----------------------------------------+
| 110 | 01101110 | 6E  | n      | Lowercase n                            |
+-----+----------+-----+--------+----------------------------------------+
| 111 | 01101111 | 6F  | o      | Lowercase o                            |
+-----+----------+-----+--------+----------------------------------------+
| 112 | 01110000 | 70  | p      | Lowercase p                            |
+-----+----------+-----+--------+----------------------------------------+
| 113 | 01110001 | 71  | q      | Lowercase q                            |
+-----+----------+-----+--------+----------------------------------------+
| 114 | 01110010 | 72  | r      | Lowercase r                            |
+-----+----------+-----+--------+----------------------------------------+
| 115 | 01110011 | 73  | s      | Lowercase s                            |
+-----+----------+-----+--------+----------------------------------------+
| 116 | 01110100 | 74  | t      | Lowercase t                            |
+-----+----------+-----+--------+----------------------------------------+
| 117 | 01110101 | 75  | u      | Lowercase u                            |
+-----+----------+-----+--------+----------------------------------------+
| 118 | 01110110 | 76  | v      | Lowercase v                            |
+-----+----------+-----+--------+----------------------------------------+
| 119 | 01110111 | 77  | w      | Lowercase w                            |
+-----+----------+-----+--------+----------------------------------------+
| 120 | 01111000 | 78  | x      | Lowercase x                            |
+-----+----------+-----+--------+----------------------------------------+
| 121 | 01111001 | 79  | y      | Lowercase y                            |
+-----+----------+-----+--------+----------------------------------------+
| 122 | 01111010 | 7A  | z      | Lowercase z                            |
+-----+----------+-----+--------+----------------------------------------+
| 123 | 01111011 | 7B  | {      | Opening brace                          |
+-----+----------+-----+--------+----------------------------------------+
| 124 | 01111100 | 7C  | \|     | Vertical bar                           |
+-----+----------+-----+--------+----------------------------------------+
| 125 | 01111101 | 7D  | }      | Closing brace                          |
+-----+----------+-----+--------+----------------------------------------+
| 126 | 01111110 | 7E  | ~      | Equivalency sign / tilde               |
+-----+----------+-----+--------+----------------------------------------+
| 127 | 01111111 | 7F  | DEL    | Delete                                 |
+-----+----------+-----+--------+----------------------------------------+

Hello World! Example
--------------------

When a computer represent a text string in memory it converts the charaters to ASCII and stores those Bytes in memory.

The text sring 'Hello World!' can be converted to ASCII Bytes using the above table:

+--------+-----+-----+
| Symbol | DEC | HEX |
+--------+-----+-----+
| H      | 72  | 48  |
+--------+-----+-----+
| e      | 101 | 65  |
+--------+-----+-----+
| l      | 108 | 6c  |
+--------+-----+-----+
| l      | 108 | 6c  |
+--------+-----+-----+
| o      | 111 | 6f  |
+--------+-----+-----+
| SP     | 32  | 20  |
+--------+-----+-----+
| W      | 87  | 57  |
+--------+-----+-----+
| o      | 111 | 6f  |
+--------+-----+-----+
| r      | 114 | 72  |
+--------+-----+-----+
| l      | 108 | 6c  |
+--------+-----+-----+
| d      | 100 | 64  |
+--------+-----+-----+
| !      | 33  | 21  |
+--------+-----+-----+

.. code-block:: python
    
    """
    Python example to demonstrate how to convert from
    a string to an ASCII bytearray 
    """

    text = "Hello World!"
    ascii = [ord(c) for c in text]
    ascii_hex = bytearray(ascii).hex()
    print(f"Text: {text}")
    print(f"ASCII: {ascii}")
    print(f"ASCII in HEX: {ascii_hex}")

    """
    Output
    Text: Hello World!
    ASCII: [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
    ASCII in HEX: 48656c6c6f20576f726c6421
    """

Endianness
**********

In computing, endianness is the order or sequence of bytes of a word of digital data in computer memory.
Endianness is primarily expressed as ``Big-Endian`` (BE) or ``Little-Endian`` (LE). 
A big-endian system stores the most significant byte of a word at the smallest memory address and the least significant byte at the largest. 
A little-endian system, in contrast, stores the least-significant byte at the smallest address.

Big-Endian (BE)
---------------

Big-Endian means numbers are stored/ordered in the computers memory as you read
**left to right**, mapping to first memory address to last. 

*Note: the number is split into Bytes as the basic unit for computer memory*

Lets use the integer number 305419896 as an exmaple. 305419896\ :sub:`10` in Hexadecimal is 12345678\ :sub:`16`.  

The number is stored in memory with the **big-end** first (when split in to Bytes).

+--------------------+-------------+
| Memory Byte Number | Value (HEX) |
+--------------------+-------------+
| 0                  | 12          |
+--------------------+-------------+
| 1                  | 34          |
+--------------------+-------------+
| 2                  | 56          |
+--------------------+-------------+
| 3                  | 78          |
+--------------------+-------------+

Little-Endian (LE)
------------------

Little-Endian means numbers are stored/ordered in the computers memory as you read
**right to left**, mapping to first memory address to last. 

*Note: the number is split into Bytes as the basic unit for computer memory*

Using the same integer number 305419896\ :sub:`10` in Hexadecimal is 12345678\ :sub:`16`.  

The number is stored in memory with the **little-end** first (when split in to Bytes).

+--------------------+-------------+
| Memory Byte Number | Value (HEX) |
+--------------------+-------------+
| 0                  | 78          |
+--------------------+-------------+
| 1                  | 56          |
+--------------------+-------------+
| 2                  | 34          |
+--------------------+-------------+
| 3                  | 12          |
+--------------------+-------------+

It is important to note that both systems, Big-Endian and Little-Endian, the number is the same value the computer is just
storing the value in a different order, as shown in the following table

+---------------+------+------+------+------+----------+-----------+
| Byte Number   |  0   |  1   |  2   |  3   |  HEX     | DEC       | 
+---------------+------+------+------+------+----------+-----------+
| Big-Endian    |  12  |  34  |  56  |  78  | 12345678 | 305419896 |
+---------------+------+------+------+------+----------+-----------+
| Little-Endian |  78  |  56  |  34  |  12  | 12345678 | 305419896 | 
+---------------+------+------+------+------+----------+-----------+

Python Byte Arrays
******************

Python supports various ways to store Bytes in memory.

.. _computer-number-systems-byte-string-prefix:

Byte String Prefix
------------------

.. code-block:: python

    '''
    Bytes string prefix =  "b" or "B" or "br" or "Br" or "bR" or "BR"
    '''

    byte_sequence = b"Hello World!"
    print(f"byte_sequence: {byte_sequence}")
    print(f"byte_sequence in HEX: {byte_sequence.hex()}")

    """
    Output
    byte_sequence: b'Hello World!'
    byte_sequence in HEX: 48656c6c6f20576f726c6421
    """

    '''
    Byte HEX values can be escaped by \x 
    eg 255 base 10 = FF base 16 = \xFF
    '''

    byte_sequence = b"\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21"
    print(f"byte_sequence: {byte_sequence}")
    print(f"byte_sequence in HEX: {byte_sequence.hex()}")

    """
    Output
    byte_sequence: b'Hello World!'
    byte_sequence in HEX: 48656c6c6f20576f726c6421
    """

Bytes Object
------------

String
^^^^^^

.. code-block:: python

    '''
    Bytes created from a iterable of ints, string, bytes or buffer objects.
    > String example
    '''

    byte_sequence = bytes("Hello World!", "utf8")
    print(f"byte_sequence: {byte_sequence}")
    print(f"byte_sequence in HEX: {byte_sequence.hex()}")

    """
    Output
    byte_sequence: b'Hello World!'
    byte_sequence in HEX: 48656c6c6f20576f726c6421
    """

Integer,  Big-Endian
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    '''
    Bytes created from a iterable of ints, string, bytes or buffer objects.
    > Integer example stored as 4-Bytes, Big-Endian and unsigned
    '''

    byte_sequence = int(305419896).to_bytes(length=4, byteorder='big', signed=False)
    print(f"byte_sequence: {byte_sequence}")
    print(f"byte_sequence in HEX: {byte_sequence.hex()}")

    """
    Output
    byte_sequence: b'\x124Vx'
    byte_sequence in HEX: 12345678
    """

Integer,  Little-Endian
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    '''
    Bytes created from a iterable of ints, string, bytes or buffer objects.
    > Integer example stored as 4-Bytes, Little-Endian and unsigned
    '''

    byte_sequence = int(305419896).to_bytes(length=4, byteorder='little', signed=False)
    print(f"byte_sequence: {byte_sequence}")
    print(f"byte_sequence in HEX: {byte_sequence.hex()}")

    """
    Output
    byte_sequence: b'xV4\x12'
    byte_sequence in HEX: 78563412
    """

From Hex
^^^^^^^^

.. code-block:: python

    '''
    Create a bytes object from a string of hexadecimal numbers.
    '''

    byte_sequence = bytes.fromhex("12345678")
    print(f"byte_sequence: {byte_sequence}")
    print(f"byte_sequence in HEX: {byte_sequence.hex()}")

    """
    Output
    byte_sequence: b'\x124Vx'
    byte_sequence in HEX: 12345678
    """
