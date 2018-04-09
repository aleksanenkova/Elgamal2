# Message Encryption
To start, you need to generate a public key:

***

##### ` Генерация ключей`
Parameters **p** and **x** are entered from the keyboard
##### `Число p= 3361`
##### `Число x= 487`
##### `Открытым ключом является тройка (p,g,y):  [3361, 22, 947]`
##### `Закрытый ключ:  487`
Then you need to select the mode. In this case, you need to press the "1". An encryption table appears on the screen, with which you need to encrypt the message. The message is encrypted into a number format.
##### `Сообщение: "ВВЕДЕНИЕВКРИПТОГРАФИЮ" шифруется как "131316151626211613232921283227142911342145"`
In the next step, k and M are calculated. If a pair of numbers is greater than p, then the numbers in the pair are separated.


##### `k= 100`
##### `M=1313`

##### `k= 2256`
##### `M=1615`

##### `k= 2834`
##### `M=1626`

##### `k= 2789`
##### `M=2116`

##### `k= 1906`
##### `M=1323`

##### `k= 2053`
##### `M=2921`

##### `k= 298`
##### `M=2832`

##### `k= 2269`
##### `M=2714`

##### `k= 3332`
##### `M=2911`

##### `k= 420`
##### `M=342`

##### `k= 3220`
##### `M=145`
Next are the numbers **a** and **b**, which are cryptograms.  A cryptogram is written to a file **'cryptogram.txt'**

# Decrypting the message
To start, you need to generate a public key:
***

#### ` Генерация ключей`
Parameters **p** and **x** are entered from the keyboard
#### `Число p= 3361`
#### `Число x= 487`
#### `Открытым ключом является тройка (p,g,y):  [3361, 22, 947]`
#### `Закрытый ключ:  487`
Then you need to select the mode. In this case, you need to press the **"2"**. The screen displays a cryptogram
(**a** and **b**) and table for decrypt.
##### `448 225`
##### `1533 204`
##### `3349 253`
##### `1797 55`
##### `490 3019`
##### `978 3236`
##### `2365 2307`
##### `391 1731`
##### `1288 2279`
##### `30 2028`
##### `3263 395`
Knowing **a** and **b** we find the individual **M**:
##### `131316151626211613232921283227142911342145`
Next, read two digits and decrypt according to the decryption table:
##### `ВВЕДЕНИЕВКРИПТОГРAФИЮ`

