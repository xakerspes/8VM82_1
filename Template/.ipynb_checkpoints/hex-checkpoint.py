{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "import hexdump\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import struct\n",
    "file_in = '123.gr2'\n",
    "fd = open(file_in,'rb')\n",
    "numpy_data = np.fromfile(fd, dtype = np.dtype('B'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "l= list(i*i for i in range(0,500) if i%5==0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 71  82  48  50  72 232 116 111  52  50  86  71]\n",
      " [ 28 155 116 221  96   3 222   0 184   0 201   0]\n",
      " [ 38 155 116 221 194   3  30   1 246   0 223   0]\n",
      " [ 48 155 116 221 112   3 238   0 208   0 204   0]\n",
      " [ 58 155 116 221 157   3 212   0 175   0 203   0]\n",
      " [ 68 155 116 221  45   4 222   0  15   1 204   0]\n",
      " [ 78 155 116 221  28   5  32   1 103   1   3   1]\n",
      " [ 88 155 116 221  49   3 201   0 159   0 209   0]\n",
      " [ 98 155 116 221 105   2  54   1 100   0 219   0]\n",
      " [108 155 116 221 140   2 233   0 131   0 214   0]\n",
      " [118 155 116 221 149   2  66   1 103   0 206   0]\n",
      " [128 155 116 221  23   3  55   1 140   0 243   0]\n",
      " [138 155 116 221 113   3 224   0 193   0 238   0]\n",
      " [148 155 116 221  44   3 138   1 164   0  33   1]\n",
      " [158 155 116 221  23   3 207   0 149   0 213   0]\n",
      " [168 155 116 221 117   3 206   0 189   0 212   0]\n",
      " [178 155 116 221  96   3 220   0 205   0 201   0]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import urllib.request\n",
    "\n",
    "page = urllib.request.urlopen(\"http://mgr.imces.ru/stdpub/mgr-baikal/hsg-irkutsk/48E8746F34325647_170926_092325.gr2\")\n",
    "f = open(\"test.txt\", \"w\")\n",
    "content = page.read()\n",
    "numpy_data = np.frombuffer(content, dtype = np.dtype('B')).reshape(int(len(content)/12),12)\n",
    "f.close()\n",
    "\n",
    "print(numpy_data)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "a=np.array(numpy_data, dtype=np.uint32)\n",
    "s=0\n",
    "for i in range(3,-1,-1):\n",
    "    s = s+a[4,i]*pow(16,i*2)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Tuesday, September 26, 2017 04:24:10'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "datetime.fromtimestamp(s-2209032000).strftime(\"%A, %B %d, %Y %I:%M:%S\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(256, 512)\n"
     ]
    }
   ],
   "source": [
    "import struct\n",
    "testBytes = b'\\x00\\x01\\x00\\x02'\n",
    "testResult = struct.unpack('<HH', testBytes)\n",
    "print (testResult)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "testBytes = b'\\xF1\\x10'\n",
    "for i in range(len(content)):\n",
    "    int.from_bytes(content, byteorder='little',signed=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b'GR02'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "content[0:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "z=np.array(content[0:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int.from_bytes(z, byteorder='little',signed=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
