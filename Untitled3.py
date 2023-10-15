{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bbd5d215-c0b5-4b11-9dde-91f03c50d759",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np, pandas as pd, matplotlib.pyplot as plt\n",
    "import unittest\n",
    "import requests\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "3a2a96c2-55c4-41d7-8a89-479c04b1293e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   0  1  2   3\n",
      "0  1  2  3   4\n",
      "1  5  6  7   8\n",
      "2  7  8  9  10\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame({'0': [1,5,7], '1': [2,6,8], '2': [3,7,9], '3': [4,8,10]})\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "4bfd1b6c-fe1d-4e6e-a5c9-f4ae0cc80480",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = [2, 4, 6, 8, 10]\n",
    "array = np.asarray(a)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "c7a550d9-3ef1-4ab9-abab-2d4c0e36df6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "array=np.asarray(a)\n",
    "sum=np.sum(array)\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "7e02ccf2-4b1a-4a6b-9549-8242aaa6a5e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
    "sum = a.sum(axis=0)[1]\n",
    "sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "a7aa6eeb-4c61-4d01-ad53-07a2edd00810",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 0 0]\n",
      " [0 0 0]\n",
      " [0 0 0]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "n = 3\n",
    "zeros = np.zeros((n, n), dtype=int)\n",
    "print(zeros)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "e1636b13-fb75-4084-81ac-bfdfaea7dd30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 1 1]\n",
      " [1 1 1]\n",
      " [1 1 1]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "n = 3\n",
    "ones=np.ones((n,n), dtype=int)\n",
    "print(ones)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "05b6be38-5f11-4910-820a-b1d9099a37fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0.75275718  9.6419745  -5.3294215   7.13130251 13.00099875 -3.48426038\n",
      "  2.13168104]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "sd = 4.0\n",
    "m = 5\n",
    "s = 7\n",
    "random_numbers = np.random.normal(sd, m, s)\n",
    "print(random_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "44afc8c1-7129-4fe5-a76d-578c15f98bae",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "url = 'https://raw.githubusercontent.com/data602sps/assignments/master/Sacramentorealestatetransactions.csv'\n",
    "df = pd.read_csv(url)\n",
    "row_count = df.shape[0]\n",
    "avg_sq_ft = df['sq__ft'].mean()\n",
    "df_zip_95670 = df.loc[df['zip'] == 95670]\n",
    "df_zip_not_95610 = df.loc[df['zip'] != 95610]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "82a9e702-dfc5-4ae8-b75d-2745b2ddd7f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "985\n"
     ]
    }
   ],
   "source": [
    "print(row_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "14051e5d-58ee-4c62-bd8c-27bf1cd66ade",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 0 0]\n",
      " [0 1 0]\n",
      " [0 0 1]]\n"
     ]
    }
   ],
   "source": [
    "identity_matrix=np.identity(n, dtype=int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "a6ca92d1-7e17-4534-bffc-4c796f519fc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0]\n",
      " [1]\n",
      " [2]]\n"
     ]
    }
   ],
   "source": [
    "array_1d = np.arange(n)\n",
    "array_reshaped = array_1d.reshape((3, n//3))\n",
    "print(array_reshaped)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "ac896a3b-eb37-4100-9593-fcc317141996",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 0 1 0 1 0]\n",
      " [0 0 0 0 0 0]\n",
      " [1 0 1 0 1 0]\n",
      " [0 0 0 0 0 0]\n",
      " [1 0 1 0 1 0]\n",
      " [0 0 0 0 0 0]]\n"
     ]
    }
   ],
   "source": [
    "checkerboard_matrix=np.zeros((2*n,2*n),dtype=int)\n",
    "checkerboard_matrix[0::2,::2] = 1\n",
    "checkerboard_matrix[::2,0::2] = 1 \n",
    "print(checkerboard_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "551d625d-6d58-45e6-bc11-c7ed8919e5bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2010-01-01    Ellipsis\n",
      "2010-01-02    Ellipsis\n",
      "2010-01-03    Ellipsis\n",
      "2010-01-04    Ellipsis\n",
      "2010-01-05    Ellipsis\n",
      "                ...   \n",
      "2015-07-03    Ellipsis\n",
      "2015-07-04    Ellipsis\n",
      "2015-07-05    Ellipsis\n",
      "2015-07-06    Ellipsis\n",
      "2015-07-07    Ellipsis\n",
      "Freq: D, Length: 2014, dtype: object\n"
     ]
    }
   ],
   "source": [
    "s = pd.Series(..., index = pd.date_range('1/1/2010', periods = 2014))\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "272c2a8b-bbe0-4706-8311-7302b016e781",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array from 0 to 9:\n",
      "[0 1 2 3 4 5 6 7 8]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.arange(9)\n",
    "print(\"Array from 0 to 9:\")\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "598d0de6-e704-4bbd-b072-6d6716681fb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "array = np.array([i for i in range(10)])\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "85d9e853-135b-46b9-b0b8-1e7b574b802a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 3, 5, 7, 9])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])\n",
    "a[a % 2 == 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9a4a4af1-8072-4691-a509-76c9714c8262",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original arrays [1 2 3 2 3 4 3 4 5 6]   [ 7  2 10  2  7  4  9  4  9  8]\n",
      "Common values [2 4]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    " \n",
    "a = np.array([1,2,3,2,3,4,3,4,5,6])\n",
    "b = np.array([7,2,10,2,7,4,9,4,9,8]) \n",
    "print(\"Original arrays\", a, ' ', b) \n",
    "c = np.intersect1d(a, b) \n",
    "print(\"Common values\", c) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f36ecb05-2cd1-4bdd-ba4c-078408b9e5a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([1, 2, 3, 4, 5])\n",
    "b = np.array([5, 6, 7, 8, 9])\n",
    "result = np.setdiff1d(a, b)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06ba8cc7-9db1-4f7d-80c0-2b60e13d91dc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78c1ae4f-a9ad-4172-ab82-2059797f225a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
