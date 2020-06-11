{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyforest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df=pd.read_csv('heart.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>male</th>\n",
       "      <th>age</th>\n",
       "      <th>education</th>\n",
       "      <th>currentSmoker</th>\n",
       "      <th>cigsPerDay</th>\n",
       "      <th>BPMeds</th>\n",
       "      <th>prevalentStroke</th>\n",
       "      <th>prevalentHyp</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>totChol</th>\n",
       "      <th>sysBP</th>\n",
       "      <th>diaBP</th>\n",
       "      <th>BMI</th>\n",
       "      <th>heartRate</th>\n",
       "      <th>glucose</th>\n",
       "      <th>TenYearCHD</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>195.0</td>\n",
       "      <td>106.0</td>\n",
       "      <td>70.0</td>\n",
       "      <td>26.97</td>\n",
       "      <td>80.0</td>\n",
       "      <td>77.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>46</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>250.0</td>\n",
       "      <td>121.0</td>\n",
       "      <td>81.0</td>\n",
       "      <td>28.73</td>\n",
       "      <td>95.0</td>\n",
       "      <td>76.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>48</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>245.0</td>\n",
       "      <td>127.5</td>\n",
       "      <td>80.0</td>\n",
       "      <td>25.34</td>\n",
       "      <td>75.0</td>\n",
       "      <td>70.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>61</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1</td>\n",
       "      <td>30.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>225.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>95.0</td>\n",
       "      <td>28.58</td>\n",
       "      <td>65.0</td>\n",
       "      <td>103.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>46</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1</td>\n",
       "      <td>23.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>285.0</td>\n",
       "      <td>130.0</td>\n",
       "      <td>84.0</td>\n",
       "      <td>23.10</td>\n",
       "      <td>85.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>0</td>\n",
       "      <td>65</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>193.0</td>\n",
       "      <td>123.0</td>\n",
       "      <td>76.5</td>\n",
       "      <td>29.33</td>\n",
       "      <td>60.0</td>\n",
       "      <td>96.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>0</td>\n",
       "      <td>63</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>239.0</td>\n",
       "      <td>134.0</td>\n",
       "      <td>80.0</td>\n",
       "      <td>26.64</td>\n",
       "      <td>88.0</td>\n",
       "      <td>126.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>205.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>60.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>60.0</td>\n",
       "      <td>72.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>0</td>\n",
       "      <td>56</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>296.0</td>\n",
       "      <td>180.0</td>\n",
       "      <td>90.0</td>\n",
       "      <td>23.72</td>\n",
       "      <td>75.0</td>\n",
       "      <td>120.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>0</td>\n",
       "      <td>56</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>15.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>269.0</td>\n",
       "      <td>121.0</td>\n",
       "      <td>75.0</td>\n",
       "      <td>22.36</td>\n",
       "      <td>50.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 16 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    male  age  education  currentSmoker  cigsPerDay  BPMeds  prevalentStroke  \\\n",
       "0      1   39        4.0              0         0.0     0.0                0   \n",
       "1      0   46        2.0              0         0.0     0.0                0   \n",
       "2      1   48        1.0              1        20.0     0.0                0   \n",
       "3      0   61        3.0              1        30.0     0.0                0   \n",
       "4      0   46        3.0              1        23.0     0.0                0   \n",
       "..   ...  ...        ...            ...         ...     ...              ...   \n",
       "95     0   65        3.0              0         0.0     0.0                0   \n",
       "96     0   63        4.0              1        20.0     0.0                0   \n",
       "97     0   40        2.0              0         0.0     0.0                0   \n",
       "98     0   56        1.0              0         0.0     0.0                0   \n",
       "99     0   56        1.0              1        15.0     0.0                0   \n",
       "\n",
       "    prevalentHyp  diabetes  totChol  sysBP  diaBP    BMI  heartRate  glucose  \\\n",
       "0              0         0    195.0  106.0   70.0  26.97       80.0     77.0   \n",
       "1              0         0    250.0  121.0   81.0  28.73       95.0     76.0   \n",
       "2              0         0    245.0  127.5   80.0  25.34       75.0     70.0   \n",
       "3              1         0    225.0  150.0   95.0  28.58       65.0    103.0   \n",
       "4              0         0    285.0  130.0   84.0  23.10       85.0     85.0   \n",
       "..           ...       ...      ...    ...    ...    ...        ...      ...   \n",
       "95             0         0    193.0  123.0   76.5  29.33       60.0     96.0   \n",
       "96             0         1    239.0  134.0   80.0  26.64       88.0    126.0   \n",
       "97             0         0    205.0  100.0   60.0    NaN       60.0     72.0   \n",
       "98             1         0    296.0  180.0   90.0  23.72       75.0    120.0   \n",
       "99             0         0    269.0  121.0   75.0  22.36       50.0     66.0   \n",
       "\n",
       "    TenYearCHD  \n",
       "0            0  \n",
       "1            0  \n",
       "2            0  \n",
       "3            1  \n",
       "4            0  \n",
       "..         ...  \n",
       "95           0  \n",
       "96           0  \n",
       "97           1  \n",
       "98           0  \n",
       "99           0  \n",
       "\n",
       "[100 rows x 16 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male                 0\n",
       "age                  0\n",
       "education          105\n",
       "currentSmoker        0\n",
       "cigsPerDay          29\n",
       "BPMeds              53\n",
       "prevalentStroke      0\n",
       "prevalentHyp         0\n",
       "diabetes             0\n",
       "totChol             50\n",
       "sysBP                0\n",
       "diaBP                0\n",
       "BMI                 19\n",
       "heartRate            1\n",
       "glucose            388\n",
       "TenYearCHD           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['education'].fillna(value=np.median(df['education'].dropna()),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male                 0\n",
       "age                  0\n",
       "education            0\n",
       "currentSmoker        0\n",
       "cigsPerDay          29\n",
       "BPMeds              53\n",
       "prevalentStroke      0\n",
       "prevalentHyp         0\n",
       "diabetes             0\n",
       "totChol             50\n",
       "sysBP                0\n",
       "diaBP                0\n",
       "BMI                 19\n",
       "heartRate            1\n",
       "glucose            388\n",
       "TenYearCHD           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['cigsPerDay'].fillna(value=np.median(df['cigsPerDay'].dropna()),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['BPMeds'].fillna(value=np.mean(df['BPMeds'].dropna()),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['totChol'].fillna(value=np.mean(df['totChol'].dropna()),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['heartRate'].fillna(value=np.mean(df['heartRate'].dropna()),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['BMI'].fillna(value=np.mean(df['BMI'].dropna()),inplace=True)\n",
    "df['glucose'].fillna(value=np.mean(df['glucose'].dropna()),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male               0\n",
       "age                0\n",
       "education          0\n",
       "currentSmoker      0\n",
       "cigsPerDay         0\n",
       "BPMeds             0\n",
       "prevalentStroke    0\n",
       "prevalentHyp       0\n",
       "diabetes           0\n",
       "totChol            0\n",
       "sysBP              0\n",
       "diaBP              0\n",
       "BMI                0\n",
       "heartRate          0\n",
       "glucose            0\n",
       "TenYearCHD         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "sns.distplot(df['age'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "sns.distplot(df['education'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "sns.countplot(df['male'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "sns.countplot(df['currentSmoker'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "sns.distplot(df['cigsPerDay'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "sns.countplot(df['prevalentStroke'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "sns.distplot(df['prevalentHyp'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAeoAAAFzCAYAAADxBEqxAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAgAElEQVR4nO3deXSU153n//dXpRXtICHQhkAGs5gdYwx4d4jJ5kw2O78s3UmmSSZ2ks50uieZ9LR7OvOb7p4sEzubm7iTbp/JYo7TntCxs9lp42BsQGBAYTM7Umll0QZorTt/aGlZFlCIkm4tn5cPB1XVU1UfPfLRh3ufW89jzjlEREQkOiX5DiAiIiKXp6IWERGJYipqERGRKKaiFhERiWIqahERkSimohYREYliyb4DjKagoMBVVFT4jiEiIjIhdu3adcY5VzjaY1FZ1BUVFVRVVfmOISIiMiHM7NTlHtPUt4iISBRTUYuIiEQxFbWIiEgUU1GLiIhEMRW1iIhIFFNRi4iIRDEVtYiISBRTUYuIiEQxFbWIiEgUU1GLiIhEMRW1iIhIFFNRi4iIRDEVtYiISBSLyqtnSezbuGvjZR/bsHzDBCYREYltGlGLiIhEMRW1iIhIFNPUt0SVK02Zg6bNRSTxaEQtIiISxVTUIiIiUUxFLSIiEsV0jFq8ONB8gH2N+yjLKaM8t5zp2dNJTtL/jiIiI+k3o0yoho4GHnz6QTbt34TDDd0/JWMKG9955YVkIiKJSEUtE+bpA0/z/PHnmZQyiS+t/RIfWPABGjoaONV6iid2P8F7N72XO2bcwfvnv5+UQIrvuCIiUUFFLRNiR3AHvz3+W1aXreb/PvB/KcwsBGAxiwH44yV/zJdf+DJfe+VrHDt3jM+t+hw5aTk+I4uIRAUtJpNxd+7SOX5c/WNm5c/iwws/PFTSw6UGUvnquq/ymZWfob6jnmcOPeMhqYhI9FFRy7gKuRA/3PNDQi7Ex5d8nEBS4Irb3zT1Ju6ZeQ/barZxsuXkxIQUEYliKmoZV88ff57Xz77OAwseGHUkPZq3zX4bOWk5PLX/KZxzV3+CiEgcU1HLuGnvaufnh3/OkqIlrC5bHfbzMlIyePfcd3P8/HG2B7ePY0IRkeinxWQybl6pfYXeUC/3z70fMxu6/2rn8wa4tfRWtpzcwjMHn2HJtCWkJ6ePZ1QRkailEbWMC+ccW09vpTK/kuLs4mt+fpIl8cBND9DS1cJLp14ah4QiIrFBRS3j4ui5ozReaGRt+doxv0ZlfiUzcmewq35XBJOJiMQWFbWMi62nt5KenM7y6cuv63WWTV/GyZaTnLt0LkLJRERii4paIu78pfPsqt/FypKVpCWnXddrLZ22FIA9DXsiEU1EJOaoqCXiflz9Y3pCPdxWftt1v1ZRVhHF2cXsrt8dgWQiIrFHRS0R5Zzj+7u/T3luOeW55RF5zWXTlnH03FHautoi8noiIrFERS0RtbdxL3sb97K2bOyLyEZaOn0pDqfpbxFJSCpqiahfHvklAEumLYnYa5ZklzB10lRea3gtYq8pIhIrVNQSUb89/lsWFy0mNz03Yq9pZiydvpRDZw5x/tL5iL2uiEgsUFFLxFzovsDW01tZV7ku4q+9dNpSQi7E5sObI/7aIiLRTEUtEbPl1BZ6Qj3jUtQVeRXkp+fzr6//a8RfW0QkmqmoJWJ+c+w3pCenX9fZyC7HzJg9ZTYv17ysK2qJSEIJ66IcZnYf8CgQAJ5wzv3diMfnAj8ElgFfds59LdznSmwa7cIam/ZvYlb+LJ7c++S4vGdlfiU7gjs42XKSmfkzx+U9RESizVVH1GYWAL4DrAfmAx80s/kjNjsHfBb42hieK3Hg/KXz1HfUM79g/H68lfmVAGyr2TZu7yEiEm3CmfpeCRx1zh13znUDPwXuH76Bc67JObcT6LnW50p8OHDmAADzC8evqEtySshKzVJRi0hCCaeoS4CaYbdrB+4Lx/U8V2LIweaD5KTljOmSluFKsiRWla5iW62KWkQSRzhFbaPcF+5qnrCfa2YbzKzKzKqam5vDfHmJBiEX4uCZg8wvmI/ZaD/yyFldupp9jfto72of1/cREYkW4SwmqwXKht0uBerCfP2wn+uc2whsBFixYoWW9caQ2rZaOro7mFc4b9zfq6WzhZAL8Vcv/hXzCt74fhuWbxj39xcRmWjhjKh3ArPNbKaZpQIPAuGedeJ6nisx4vCZwwBvKs7xMCt/FoZx7NyxcX8vEZFocNURtXOu18weBn5N/0esfuCc229mnxp4/HEzmwZUATlAyMz+FJjvnGsb7bnj9c2IHydaTjAlY0pETxt6ORkpGRRnF3PsvIpaRBJDWJ+jds49Bzw34r7Hh33dQP+0dljPlfhyouUEs/JnTdj7VeZXsqNuByEXIsl0zh4RiW/6LSfXpbWzlXOXzlGRVzFh7zlr8iw6ezupb6+fsPcUEfFFRS3X5WTrSQBm5k3cmcJuyL8BQNPfIpIQVNRyXU6cP0GSJVGeWz5h71kwqYDs1GyOnz8+Ye8pIuKLilquy8mWk5Rkl5AaSJ2w9zQzKvMrNaIWkYSgopYxC7lQ/wUyJnDae9CMvBk0XWjiUs+lCX9vEZGJpKKWMWu60MSl3ksTupBs0IzcGQCcbj094e8tIjKRVNQyZidaTgB4ueTkjLz+oj7VemrC31tEZCKpqGXMTp4/SVogjWlZ0yb8vbNSs5icMVkjahGJeypqGbMTLSeoyKvwdtKRGbkzNKIWkbinopYx6enrobat1svx6UHlueVaUCYicU9FLWNS01ZDn+vzWtRaUCYiiUBFLWNysuUkMLFnJBtJC8pEJBGoqGVMTrWcIjctl/yMfG8ZslKzmJIxRSNqEYlrKmoZk9r2WspyynzHoDy3nFMtGlGLSPxSUcs16+nrob69npKcEt9R+heUXdSCMhGJXypquWaHzhyiz/VRmjPqJcgnlBaUiUi8U1HLNdvXuA+Akmz/I2otKBOReKeilmu2r3EfAQt4OSPZSIMLylTUIhKvVNRyzfY17WN69nQCSQHfUYD+49SnWzT1LSLxSUUt12xf4z5Ks/0fnx40uKCstbPVdxQRkYhTUcs1OXPxDHXtdVGx4nvQ4NnRdtfv9htERGQcqKjlmlQ3VgNExYrvQeW55QBU1VV5TiIiEnkqarkm0bTie9DggrJd9bt8RxERiTgVtVyTfY37KJxUSE5aju8ob1CeW66iFpG4pKKWa7KvaR+LihZhZr6jvMGMvBkcPXeUls4W31FERCJKRS1h6wv18YemP7CoaJHvKG8yeIYyLSgTkXijopawHT13lM7ezqgs6sEFZbvqNP0tIvFFRS1hG1xIFo1FnZWaxYzcGTpOLSJxR0UtYdvXuI8kS2J+4XzfUUa1oniFilpE4k6y7wASvTbu2viG2//6+r9SlFnEk3uf9JToypZPX87PDv6Mls4W8tLzfMcREYkIjaglbMH2IMXZxb5jXNby4uWAFpSJSHxRUUtYuvu6OXvxbHQX9fT+otaCMhGJJypqCUtDRwMOx/Ss6b6jXNaUSVOoyKugql6nEhWR+KGilrDUt9cDMD07eosa+kfVGlGLSDxRUUtY6jvqSbIkpmZO9R3lipZPX86x88d0hjIRiRsqaglLfXs9UzOnkpwU3R8UWFG8AoCdwZ2ek4iIRIaKWsJS31Ef1cenB91SegtJlsS2mm2+o4iIRISKWq6qp6+H5ovNUX98GiAnLYeFUxfycs3LvqOIiESEilququlCEyEXiokRNcCasjW8UvsKvaFe31FERK6bilquqr4jNlZ8D1pTvoaO7g6qG6t9RxERuW4qarmq+vZ6DKMos8h3lLCsKVsDoOlvEYkLKmq5qvqOegomFZAaSPUdJSzlueWUZJeoqEUkLqio5arqO+pjZtobwMxYW76Wl0+rqEUk9qmo5Yr6Qn00djTGzEKyQWvK1lDTVsPp1tO+o4iIXBcVtVxR88Vm+lxfTI2ooX9BGaBRtYjEPBW1XNHQOb5jbES9qGgRmSmZOk4tIjFPRS1XNPjRrGlZ0zwnuTbJScmsKl2lohaRmBdWUZvZfWZ22MyOmtkXR3nczOyxgcf3mdmyYY993sz2m9kfzOwnZpYeyW9Axld9ez1TMqaQnhx7P7a15WvZ17iPtq4231FERMbsqkVtZgHgO8B6YD7wQTObP2Kz9cDsgT8bgO8NPLcE+Cywwjl3ExAAHoxYehl3sXKO79GsKVtDyIV4tfZV31FERMYsnBH1SuCoc+64c64b+Clw/4ht7geedP1eBfLMbPC3ezKQYWbJwCSgLkLZZZyFXIiGjgamZcfWtPegVaWrCFiAl0695DuKiMiYhVPUJUDNsNu1A/dddRvnXBD4GnAaqAdanXO/Ge1NzGyDmVWZWVVzc3O4+WUcnb14lp5QT8yOqLPTsllRvIJ/O/lvvqOIiIxZOEVto9znwtnGzPLpH23PBIqBTDP78Ghv4pzb6Jxb4ZxbUVhYGEYsGW9D5/iO0aIGuHvm3ewI7qCju8N3FBGRMQmnqGuBsmG3S3nz9PXltrkXOOGca3bO9QD/Aqwee1yZSLG64nu4uyruojfUy9bTW31HEREZk3CKeicw28xmmlkq/YvBNo/YZjPw0YHV36von+Kup3/Ke5WZTTIzA+4BDkYwv4yj+vZ6ctJyyEzN9B1lzNaUryElKYXfnfid7ygiImOSfLUNnHO9ZvYw8Gv6V23/wDm338w+NfD448BzwNuAo8BF4GMDj203s6eB3UAv8BqwcTy+EYm8ho6GmJr23rhr9P+1KvIqdJxaRGLWVYsawDn3HP1lPPy+x4d97YCHLvPcR4BHriOjeOCco76jnlUlq3xHuW43FtzIc0ee4/yl8+Rn5PuOIyJyTXRmMhlVsD1IZ29nzJ3jezQ3TrmRkAvpY1oiEpNU1DKqg839Swliaer7cmbmzSQjOUPT3yISk8Ka+pbEc6D5AEBcjKhTAilU5FXw9IGnmV848qR6/TYs3zDBqUREwqMRtYzq4JmDZKZkkp2a7TtKRNxYcCPB9iDtXe2+o4iIXBMVtYzqQPMBpmVNo/9TdbFv7pS5ALx+9nXPSUREro2KWkZ18MzBuJj2HlSeW056cjqHzh7yHUVE5JqoqOVNmi80c+bimbhYSDYokBTghvwbOHL2iO8oIiLXREUtb3LwTPys+B5u9pTZ1HfU6/rUIhJTVNTyJvG04nu4OVPmAGhULSIxRUUtb3Kw+SBZqVnkp8fXWbxm5M4gLZDG6+e0oExEYoeKWt7kwJkDzC2YGzcrvgcFkgLMyp/F0bNHfUcREQmbilre5GDzwcueGCTWzZkyh2B7kAvdF3xHEREJi4pa3qC1s5Vge5B5BfN8RxkXsyfPxuE4ck7HqUUkNqio5Q0Onen/nHG8jqgr8ipISUrRiU9EJGaoqOUNBld8x+uIOiWQwsz8mRpRi0jMUFHLGxw8c5C0QBoz82f6jjJu5kyeQ01rDZd6LvmOIiJyVSpqeYMDzQeYM2UOyUnxe2G1OVPm4HAcPafV3yIS/VTU8gYHz8Tviu9BM/NnErCAPk8tIjFBRS1DLvZc5MT5E3F7fHpQaiCVirwKnaFMRGKCilqGHD5zGIeL+xE1QGV+JTVtNfSGen1HERG5IhW1DBm8GMe8wvgeUUP/x7R6Q73UttX6jiIickUqahlyoPkAAQswe/Js31HG3eCq9pMtJ/0GERG5ChW1DDl45iCVkytJS07zHWXc5afnk5OWo6IWkainopYhB5oPJMTxaQAzoyKvQkUtIlFPRS0AdPd1c/Tc0bhf8T1cRV4FDR0NOvGJiEQ1FbUAcPTcUXpDvQkzogaoyK3A4TjVesp3FBGRy1JRC9B/aUuI33N8j6YirwLQgjIRiW4qagH+/WIccwvmek4ycTJTM5k6aaqKWkSimopagP4V3zNyZ5CZmuk7yoTSgjIRiXYqagESa8X3cBV5FZzvPE9de53vKCIio1JRC32hPg6fPZxQx6cHVeRXALAzuNNvEBGRy1BRCydbTtLZ25mQI+qynDKSLIkdwR2+o4iIjEpFLQl1ju+RUgOplGSXsKNORS0i0UlFLfyh6Q8ACTmiBpiZN5OdwZ2EXMh3FBGRN1FRC9VN1ZTllJGXnuc7ihflueW0drVq9beIRCUVtVDdWM3CooW+Y3hTmlMKwN6GvZ6TiIi8mYo6wfX09XDozCEWTk3coi7JKcEw9jaqqEUk+qioE9zhs4fpCfUkdFGnBlKZPWW2ilpEolKy7wDi1zdf/SbQX9gbd230nMafxUWLqaqr8h1DRORNNKJOcMH2IEmWxLSsab6jeLW4aDEnWk7Q1tXmO4qIyBuoqBNcsC3ItKxpJCcl9uTK4mmLAdjXuM9zEhGRN1JRJ7i69jpKskt8x/BucVF/UWvlt4hEGxV1AmvrauPspbMUZxf7juJdaU4p+en5WlAmIlFHRZ3ABs9IVpKjEbWZsXjaYhW1iEQdFXUCq26sBtDU94DFRYupbqymL9TnO4qIyBAVdQKrbqomPTmdKRlTfEeJCouLFnOp9xLHzh/zHUVEZIiKOoFVN1VTnF2MmfmOEhUGV35rQZmIRJOwitrM7jOzw2Z21My+OMrjZmaPDTy+z8yWDXssz8yeNrNDZnbQzG6N5DcgY+Oco7qxWtPew8wvnE/AAjpOLSJR5apFbWYB4DvAemA+8EEzG3k9xPXA7IE/G4DvDXvsUeBXzrm5wGLgYARyy3Wqa6/jfOd5FfUw6cnpzC2Yq6IWkagSzoh6JXDUOXfcOdcN/BS4f8Q29wNPun6vAnlmNt3McoDbgX8EcM51O+daIphfxqi6aWAhmVZ8v8HiaYs19S0iUSWcoi4Baobdrh24L5xtZgHNwA/N7DUze8LMMkd7EzPbYGZVZlbV3Nwc9jcgY6MV36NbXLSYmrYazl065zuKiAgQXlGPttLIhblNMrAM+J5zbilwAXjTMW4A59xG59wK59yKwsLCMGLJ9RhcSJaZOuq/mxLW4BnKdCpREYkW4RR1LVA27HYpUBfmNrVArXNu+8D9T9Nf3OJZdVN1Ql/a8nIWFvXvk8GTwYiI+BZOUe8EZpvZTDNLBR4ENo/YZjPw0YHV36uAVudcvXOuAagxsxsHtrsHOBCp8DI2vaFeDjYfVFGPYnrWdPLT84cODYiI+HbVSyY553rN7GHg10AA+IFzbr+ZfWrg8ceB54C3AUeBi8DHhr3EZ4AfDZT88RGPiQdHzh6hq6+LhUUL6ezt9B0nqpgZC4sWDi22ExHxLaxrGzrnnqO/jIff9/iwrx3w0GWeuwdYcR0ZJcIGS2jh1IXsrNvpOU30WTh1IU/ufRLnnE4GIyLeJfZFiBNUdWM1AQswr3CeinrAxl0bh75u6Wyhvbudv936txRMKmDD8g0ek4lIotMpRBPQvqZ9zJ4ym/TkdN9RotLgR9aC7UHPSUREVNQJqbpRK76vZPD63ME2FbWI+KeiTjDtXe2caDmhor6CjJQMpmRMoa595KcQRUQmnoo6wexv3g/8++eFZXTF2cWa+haRqKCiTjCDnw/WiPrKSrJLaOhooDfU6zuKiCQ4FXWCqW6qJjMlk5n5M31HiWolOSWEXIjGjkbfUUQkwamoE0x1UzU3Tb2JJNOP/kq08ltEooV+WycQ55xWfIepKKuIJEvSym8R8U4nPIlzw0/k0drZytlLZ2nvbn/D/fJmyUnJTMuaphG1iHinEXUCGSwdXYM6PCXZJSpqEfFORZ1ABqdxS3JU1OEozi7m3KVztHW1+Y4iIglMRZ1Agu1BctJyyErN8h0lJgz+g0bXphYRn1TUCSTYHtS09zUY3Fe6NrWI+KSiThAhF6K+vV7T3tdgSsYU0pPTdW1qEfFKRZ0gmi400RPq0Yj6GpgZxdnFKmoR8UpFnSCGFpKpqK9JSXYJ1Y3VOOd8RxGRBKWiThDB9iCGMT17uu8oMaUku4Tzned1JS0R8UZFnSCC7UGmZk4lNZDqO0pMGTymr+lvEfFFRZ0g6trqNO09BsXZxYA+oiUi/qioE0BXbxfNF5spzin2HSXmZKVmMT1rukbUIuKNijoB1HfU43AaUY/RwqKF+iy1iHijok4AWvF9fRZOXciB5gP0hnp9RxGRBKSiTgDB9iApSSkUZhb6jhKTFk5dSFdfF0fPHfUdRUQSkIo6AQTbgxRnF5Nk+nGPxcKi/ut3a/pbRHzQb+4EEGwL6tSh12FewTySLEkLykTECxV1nGvraqO9u13Hp69DRkoGN0y+QR/REhEvVNRxLtiuhWSRsHDqQo2oRcQLFXWcG1rxranv67Jw6kKOnTvGhe4LvqOISIJRUce5uvY6slOzyUnL8R0lpi0sWojDcaD5gO8oIpJgVNRxLtgWHDoNpozdwqkDK781/S0iE0xFHcdCLkRdR52mvSNgVv4sMpIz9BEtEZlwKuo4dvz8cbr7urWQLAICSQEWFS1iT+Me31FEJMGoqOPY4OhPRR0ZS6ctZXf9bkIu5DuKiCQQFXUc29e4D8N0jDpClk1fRltXGyfOn/AdRUQSiIo6jlU3VVMwqYC05DTfUeLCsunLANhdv9tzEhFJJMm+A8j4qW6q1rR3BGzctRGAnr4ekiyJH7z2A853ngdgw/INPqOJSALQiDpOXeq5xNFzR7XiO4JSAimUZJdwuu207ygikkBU1HHqQPMBQi6kEXWEleeWc7r1NM4531FEJEGoqOPU4Ik5NKKOrLLcMjq6O2jpbPEdRUQShIo6TlU3VpOenM7UzKm+o8SV8txyAE63avpbRCaGijpOVTdVM79wPkmmH3EklWaXYpiKWkQmjH6Lx6nqpuqh81NL5KQlpzEta5oWlInIhFFRx6EzF8/Q0NGgoh4nZbllGlGLyIRRUcehwVOHLixSUY+H8txyWjpbaOtq8x1FRBKAijoODa741oh6fJTnaEGZiEwcFXUcqm6sZkrGFKZlTfMdJS6V5ZYBUNNW4zmJiCSCsIrazO4zs8NmdtTMvjjK42Zmjw08vs/Mlo14PGBmr5nZLyIVXC6vuqmahUULMTPfUeLSpJRJFE4q1IhaRCbEVYvazALAd4D1wHzgg2Y2f8Rm64HZA382AN8b8fjngIPXnVauKuRC/KHpD5r2HmflueWcbDnpO4aIJIBwRtQrgaPOuePOuW7gp8D9I7a5H3jS9XsVyDOz6QBmVgq8HXgigrnlMk62nORCzwUV9TiblT+Lc5fOEWwL+o4iInEunKIuAYYfjKsduC/cbb4J/AUQutKbmNkGM6sys6rm5uYwYslotOJ7YlTmVwLwSu0rnpOISLwLp6hHO9A58ooEo25jZu8Ampxzu672Js65jc65Fc65FYWFhWHEktEMrvheULjAc5L4VpZbRkpSCttqtvmOIiJxLpyirgXKht0uBerC3GYN8C4zO0n/lPndZvZ/xpxWrqq6qZqZeTPJTsv2HSWuJSclMyNvhopaRMZdOEW9E5htZjPNLBV4ENg8YpvNwEcHVn+vAlqdc/XOuS8550qdcxUDz/udc+7DkfwG5I2qG6s17T1BKvMr2V2/m0s9l3xHEZE4dtWids71Ag8Dv6Z/5fYm59x+M/uUmX1qYLPngOPAUeD7wKfHKa9cQVdvF6+ffV0LySZI5eRKekI97Kq/6pEdEZExSw5nI+fcc/SX8fD7Hh/2tQMeusprvAi8eM0J5ao27toIQE1rDX2uj8YLjUP3yfgZXFC2rWYba8vXek4jIvFKZyaLI8H2/o8KlWSPXJQv4yErNYs5U+boOLWIjCsVdRwJtgVJTkqmKLPId5SEsbpsNdtqttE/qSQiEnkq6jgSbA8yLWsagaSA7ygJY3XpapovNnPs/DHfUUQkTqmo40iwPahp7wm2umw1gKa/RWTcqKjjxIXuC7R0tqioJ9i8wnnkpuWqqEVk3Kio48TQQrIcFfVESrIkbi27VUUtIuNGRR0ntOLbnzVla/hD0x84e/Gs7ygiEodU1HGirq2OSSmTyEvP8x0l4bxl1ltwOJ4//rzvKCISh1TUcSLYHqQ4uxiz0a6PIuNpRfEK8tPz+fWxX/uOIiJxSEUdB5xzWvHtUSApwL2z7uU3x36jz1OLSMSpqOPAuUvn6Ozt1EIyj9ZVriPYHuRA8wHfUUQkzqio40Btey2ghWQ+ratcB8Bvjv3GcxIRiTcq6jgQbNOKb9/Kc8uZWzBXx6lFJOJU1HGgpq2GwkmFZKRk+I6S0NbNWseWU1t0fWoRiSgVdRyoba2lLKfMd4yE99Yb3kpnbydbT2/1HUVE4oiKOsa1d7XTdLGJ0txS31ES3h0z7iA1kKrpbxGJKBV1jNvXuA9AI+ookJmaydrytVpQJiIRpaKOcXsa9gAq6mixbtY6qpuqhxb4iYhcLxV1jNvTsIfMlEydOjRKvPPGdwLwzKFnPCcRkXihoo5xexr3UJZbplOHRon5hfNZULiATfs3+Y4iInFCRR3DekO9VDdWa9o7ynxgwQfYenqrpr9FJCJU1DHs8JnDdPV1qaijzAcWfACH4+kDT/uOIiJxQEUdw4YWkuWqqKPJ3IK5LCpaxKYDmv4Wkeunoo5hexr2kBZIoyizyHcUGeGBBQ+wrWYbNa01vqOISIxL9h1Axm5P4x4WFi0kkBTwHSVhbdy1cdT7Qy4EwNMHnubzt35+IiOJSJzRiDpGOefY07CHJUVLfEeRUUzNnEp5bjlP7X/KdxQRiXEq6hhV117HmYtnWDJNRR2tlk9fzvbgdk62nPQdRURimIo6Rg0uJFNRR68VxSsA+HH1jz0nEZFYpqKOUYNFvahokeckcjkFkwq4q+Iuntj9xNAxaxGRa6WijlFV9VXMnjyb7LRs31HkCv5k2Z9wouUEvzvxO99RRCRGqahjkHOO7bXbuaX0Ft9R5Cr+w7z/wOSMyTyx+wnfUUQkRqmoY1CwPUh9Rz0ri1f6jiJXkZ6czkcWfYRnDj3DmYtnfMcRkRikoo5BO4I7ADSijhF/suxP6O7r5sm9T/qOIiIxSCc8iUE7gjtISUphcdFi31HkKgZPiDIrfxZf3fZVMlMyh650tmH5Bp/RRCRGaEQdg7YHt7Nk2hLSktN8R5EwrS1fS3GqLXMAABWJSURBVENHA8fOH/MdRURijIo6xvSF+qiqq2JliY5Px5IV01eQnpzOllNbfEcRkRijoo4xh84coqO7g1tKdHw6lqQlp7GmbA276nbR0tniO46IxBAVdYwZXEimEXXsuaviLkIupFG1iFwTFXWM2R7cTm5aLrOnzPYdRa5RYWYhi4oW8dKpl+jp6/EdR0RihIo6xuwI7uDmkptJMv3oYtE9M++ho7tjaGZERORq9Ns+hlzqucS+xn06Ph3D5kyZQ2l2Kb878Tucc77jiEgMUFHHkNcaXqPP9en4dAwzM+6eeTe17bW8ePJF33FEJAaoqGPI4HTpzcU3e04i12NlyUqyUrN4dPujvqOISAxQUceQ7cHtlOWUMT17uu8och1SAincPuN2Nh/ezLFzOgGKiFyZijpGOOd4+fTL3Fp2q+8oEgF3zLiDQFKAb+34lu8oIhLlVNQx4kTLCWraarhjxh2+o0gE5KXn8cCCB/jBaz+gravNdxwRiWIq6hix5WT/STJU1PHjc7d8jvbudn742g99RxGRKBbW1bPM7D7gUSAAPOGc+7sRj9vA428DLgJ/7JzbbWZlwJPANCAEbHTOaQXNGGzcvZGs1Cy2nt7KyzUv+44jEXBzyc3cWnor39rxLR5e+TCBpIDvSCISha46ojazAPAdYD0wH/igmc0fsdl6YPbAnw3A9wbu7wX+zDk3D1gFPDTKcyUMR84eYc7kOUOXSJT48Ker/pRj54/x7JFnfUcRkSgVzoh6JXDUOXccwMx+CtwPHBi2zf3Ak67/DA6vmlmemU13ztUD9QDOuXYzOwiUjHiuXMXJlpOcvXSWt8x6i+8oEkEbd22kL9RHfno+f/Hbv6Cho2HoMV2rWkQGhXOMugSoGXa7duC+a9rGzCqApcD20d7EzDaYWZWZVTU3N4cRK3EMHp+eM2WO5yQSaYGkAHdW3Mnhs4epaau5+hNEJOGEU9SjzbWOPPfhFbcxsyzgZ8CfOudGXeLqnNvonFvhnFtRWFgYRqzEseXUFjJTMvX56Th1W/ltpAZSef74876jiEgUCqeoa4GyYbdLgbpwtzGzFPpL+kfOuX8Ze9TEteXUFmZPma0LccSpzNRMVpetZmdwp65VLSJvEs5v/p3AbDObaWapwIPA5hHbbAY+av1WAa3OufqB1eD/CBx0zn0joskTRE1rDcfPH2fOZE17x7N7Z95LyIV0/m8ReZOrFrVzrhd4GPg1cBDY5Jzbb2afMrNPDWz2HHAcOAp8H/j0wP1rgI8Ad5vZnoE/b4v0NxHPtpwaOD5doKKOZ4WZhSyetpiXTr1EV2+X7zgiEkXC+hy1c+45+st4+H2PD/vaAQ+N8rytjH78WsK05eQW8tPzKckeuX5P4s1bZr2FPQ17eKX2FT5zy2d8xxGRKKGDnlHuxVMvctuM23R8OgFU5ldSkVfBC8dfIORCvuOISJTQb/8oduzcMY6eO8o9M+/xHUUmgJlx76x7abrYxC9e/4XvOCISJVTUUWzwbFVvn/12z0lkoiybtozJGZP5+itf9x1FRKKEijqKPXvkWeYWzKVycqXvKDJBAkkB7q64m5dOvURVXZXvOCISBVTUUaqju4MXT76o0XQCWlu+luzUbP73q//bdxQRiQIq6ij1/PHn6e7rVlEnoIyUDP7jsv/Ipv2bqGnVaUVFEp2KOko9+/qz5KTlsLZ8re8o4sFnb/ksIRfiWzu+5TuKiHimoo5CzjmePfIsb618KymBFN9xxIOKvAreN/99bNy1kfaudt9xRMQjFXUUeq3hNeo76jXtneD+86r/TGtXKxt3bfQdRUQ8UlFHoWdffxbDWD97ve8o4tEtpbdw98y7+V/b/hcXey76jiMinqioo9AvjvyCm0tuZmrmVN9RxLNH7niEpgtNGlWLJLCwzvUt42/wF3FbVxs7gzt555x36pezcPuM27mz4k7+/uW/55PLP0lGSobvSCIywTSijjJVdVU4HEumLfEdRaLEI3c8QkNHA9/f/X3fUUTEAxV1lNkR3EFpdiklObpalvS7s+JObp9xO3//8t/T2dvpO46ITDAVdRRputDEiZYTrCxZ6TuKRJlH7niEuvY6/qHqH3xHEZEJpmPUUWRHcAeGcXPJzb6jiGcj1yc455hXMI8vvvBFuvu6+fM1f+4pmYhMNI2oo4Rzjh3BHcyePJvJGZN9x5EoY2Z88KYP0hvqZdOBTb7jiMgEUlFHiVOtp2i80Khpb7msoqwi3nbD26iqq+JXR3/lO46ITBAVdZTYEdxBclIyy6Yv8x1Foti6ynUUZRbx6Wc/rZOgiCQIFXUU6Av1sbNuJzcV3kRmaqbvOBLFUgIpfGjhhzjRcoL/9rv/5juOiEwAFXUUeP7487R1tWnaW8JyY8GNfGr5p/jGq9/guzu/6zuOiIwzrfqOAo/teIzs1GwWFS3yHUVixGPrHyPYHuTh5x5mcsZkHrzpwaHHrnRGuw3LN0xEPBGJII2oPTt05hDPHXmOO2bcoUtaSthSAik89b6nuG3GbXzkmY9ocZlIHFNRe/bY9sdIDaRyR8UdvqNIjMlIyWDzg5u5aepNvOsn7+JvtvwNPX09vmOJSISpqD06d+kc/7z3n/nQwg+Rk5bjO47EoNz0XF746Au8f8H7eeTFR1j5xEpqWmt8xxKRCFJRe7Rx10Yu9lzk86s+7zuKxLDJGZP50Xt+xDMPPEN9ez3/c+v/5J/2/BPNF5p9RxORCFBRe9LT18O3d3ybe2bew8Kihb7jSBx499x3c+ChA9xVcRdVdVX81Yt/xZN7n+T8pfO+o4nIddCqb0827d9EsD3IP7xDF1mQyJmcMZkPLPgAb618K786+iteOv0SVXVVvGPOO7hn5j2+44nIGKioPejq7eKRFx9hQeEC1s9e7zuOxKHc9FweuOkB7p55N0/tf4qfHfwZ22q2sXT6UlaVrvIdT0Sugaa+Pfj2jm9z7Pwxvr7u6ySZfgQyfgozC3l45cN8+uZP093Xze0/vJ3v7PgOzjnf0UQkTBpRT7AzF8/wlZe+wvob1vPWG97qO47EqCud1GQ0i4sWc0P+Dbxw4gUe/uXDvBp8lcff/rhOWSsSAzScm2B//eJf09HdwdfWfc13FEkwmamZbP7gZr5y11f40b4fsfaHawm2BX3HEpGrUFFPoIPNB3m86nE+ufyTzC+c7zuOJKAkS+Ivb/9Lnv3/nuXYuWPc8sQt7GnY4zuWiFyBpr4nSMiFeM+m95AaSGVW/qxrnroUiaT1s9ez9eNbefuP387aH6zlqfc9xdvnvN13LBEZhYp6gnxt29c4dOYQH1r4IbLTsn3HkQQ18h+In1n5Gb6949u88yfv5F03votnHngGM/OUTkRGo6nvCbC9djtf/t2XWTZ9GbeV3+Y7jsiQvPQ8/nz1n7OieAU/P/xz3rvpvbR1tfmOJSLDqKjHWWtnKx/82Qcpzi7mwws/rNGKRJ205DQ+sfQTvH/++9l8eDMrv7+SV2pe8R1LRAaoqMeRc45P/uKTnG49zU/e+xN9FEailplx76x7ef6jz3Ox5yJrfrCGh559iNbOVt/RRBKeinoc/Zfn/wtP7X+K/3H3/2B12WrfcUSu6s6KO9n/6f189pbP8viux5n3nXl889VvajpcxCOLxjMUrVixwlVVVfmOMSaDi3V+dfRXPHPoGe6ccScP3vSgprwlJmxYvmHo66q6Kj7/68+z9fRWslOz+fjSj/P++e9nefFy0pPT3/C84YvUOns7qW+vJ9gepKGjgZbOFialTKLxQiMAk1ImMSllEiXZJSwuWkxdex0z8maMeqnX4XlE4pmZ7XLOrRjtMa36Hge/P/V7njn0DDcX38wDNz2gkpaYtKJ4Bb//2O+pqqvi0e2P8t2d3+XR7Y+SkpTC8uLlVOZXkhpIJTWQyt6GvTRfbObsxbO0dLUMvUZKUgp56XncWHAjCwoXYGZc6rnExZ6LbA9u56n9TwFgGJWTK1k2bRlLpy9lcsZkX9+2SNTRiDrCHnz6QTbt38SCwgX8p5v/E8lJ+reQxIf3znsvW09vZVvNNl6ueZn6jnp6+nro7uumJ9RDQUYBBZkFFE4qpDi7mJLsEqZMmnLF89lf6rlEbVsth84cYnfDbura6zCMRUWLuGvmXXxj3Tf0D11JCFcaUauoI6Qv1Mfnf/15vrXjWywpWsInln2C1ECq71giMaWxo5FXal9h6+mttHe3M79wPp9Z+Rk+sugjWowpcU1FPc5aO1v58DMf5hev/4K3zHoL75n3Hl0VS+Q69PT1UFVXxd7GvbzW8Bp56Xl8YukneOjmh5iZP9N3PJGIu1JRq02u0y+P/JKbvncTzx15ju++7bu8b/77VNIi1yklkMKtZbeya8Mutn5sK2+tfCvffPWbVD5Wyf0/vZ8Xjr+gS3VKwtAB1DFqvtDMF377BZ7c+yQLChfwsw/8jJUlK3UOb5EIMjPWlK9hTfkaattqebzqcTbu2sjmw5spzSll3ax1rKtcxx0Vd1CUWaTj2RKXwpr6NrP7gEeBAPCEc+7vRjxuA4+/DbgI/LFzbnc4zx1NNE99Hz13lK9v+zr/tPef6A318qW1X+LLt32ZtOQ04NqvEywi16anr4dd9bvY27CX4y3HaensX2U+JWMKC6YuYF7BPEpzSinJLqEkp4TJGZPJS88jNy2X1EAqgaQAAQvQE+rhYs9FLnRf4GLPxf6ve4Z93X2Brr4u0pPTyUzJJCs1i8LMQqZlTWNq5lStQZGIuq6PZ5lZAPgO8BagFthpZpudcweGbbYemD3w5xbge8AtYT43qjnnOHLuCL888kuePfIszx9/npRACh9d9FG+sPoL3Fhwo++IIgklJZDCqtJVrCpdRV+oj5OtJzl5/iR1HXXUttWyq24XF3oujHuOyRmTmZY1behPUWbRqLcLJhUQSAqMex6JX+FMfa8EjjrnjgOY2U+B+4HhZXs/8KTrH56/amZ5ZjYdqAjjuRPOOUfIhegJ9Qx9prOju4MzF8/QdKGJho4GXj/7OgfOHGB/036C7UEA5hbM5b4b7uOuirvITc9ly6ktbDm1xee3IpLQAkkBKvMrqcyvfMP9PX09tHS20NrVOjRCvtRziV7XS8iFcM4RsACpyf2fA09N6v87LTlt6LPhqYFUkpOShz6C1tnXSUdXB21dbbR1tdHa1UpbVxunWk5R3VhNa1cr3X3db8poGNlp2eSm5TK/cP5QkU/JmEJeeh556XnkZ+QPfZ2dmk1KIIWUpJShvyNZ9CEXoi/UR2+olz7X96av+9zA7VG+Hr5tclJy/z4LpL1h3w2/Hcn1Os65y2Yc/Bld6U9PqIeUpJQ3ZR2ZOyWQQsACQzMvg3/7PKwSTlGXADXDbtfSP2q+2jYlYT53XN347Rs53Xp66H/OkAvhuPp0/6SUScwtmMudFXeyumw1629Yz8z8mZraFokBKYEUCjMLKcwsnND37eztpL2rfajEW7ta33D73KVzHGg+QOOFxlFL/XIMIyWQgvHvZTHy99jIw5ijPd7n+sbwXY1dkiUNZR4suuHfw8j7hpehYTjcUBmHXGiiYo/KMAJJAZIsiYAF+OpbvspDKx+akPcOp6hH+2fEyKa73DbhPLf/Bcw2AIPnC+wws8NhZBs3F7nI7oH/fsSPfEa5VgXAGd8h4pz28fjTPh7G4egm/GIP07jv4xB+yzWSHI5eeoduP/yXD/MwD1/tadeyj2dc7oFwiroWKBt2uxSoC3Ob1DCeC4BzbiOg4ep1MrOqyy1IkMjQPh5/2sfjT/t4/EVqH4dzAGEnMNvMZppZKvAgsHnENpuBj1q/VUCrc64+zOeKiIjIZVx1RO2c6zWzh4Ff0/8Rqx845/ab2acGHn8ceI7+j2Ydpf/jWR+70nPH5TsRERGJQ2Gd8MQ59xz9ZTz8vseHfe2AUY+qj/ZcGVc6fDD+tI/Hn/bx+NM+Hn8R2cdRea5vERER6aeTUouIiEQxFXWMMrMyM/s3MztoZvvN7HMD9082s9+a2ZGBv/N9Z41VZpZuZjvMbO/APv7vA/drH0eYmQXM7DUz+8XAbe3jCDKzk2ZWbWZ7zKxq4D7t4wgaONHX02Z2aOD38q2R2scq6tjVC/yZc24esAp4yMzmA18EXnDOzQZeGLgtY9MF3O2cWwwsAe4b+FSD9nHkfQ44OOy29nHk3eWcWzLs40Lax5H1KPAr59xcYDH9/z9HZB+rqGOUc65+8MInzrl2+v+nKKH/FK3/PLDZPwPv9pMw9rl+HQM3Uwb+OLSPI8rMSoG3A08Mu1v7ePxpH0eImeUAtwP/COCc63bOtRChfayijgNmVgEsBbYDRQOfYWfg76n+ksW+gSnZPUAT8FvnnPZx5H0T+At4w2mstI8jywG/MbNdA2eBBO3jSJoFNAM/HDiE84SZZRKhfayijnFmlgX8DPhT51yb7zzxxjnX55xbQv9Z9Vaa2U2+M8UTM3sH0OSc2+U7S5xb45xbRv+VDh8ys9t9B4ozycAy4HvOuaXABSJ4KEFFHcPMLIX+kv6Rc+5fBu5uHLhyGQN/N/nKF08GprFeBO5D+ziS1gDvMrOTwE+Bu83s/6B9HFHOubqBv5uAZ+i/KqL2ceTUArUDM24AT9Nf3BHZxyrqGGX9l5n5R+Cgc+4bwx7aDPzRwNd/BPx8orPFCzMrNLO8ga8zgHuBQ2gfR4xz7kvOuVLnXAX9pxj+nXPuw2gfR4yZZZpZ9uDXwDrgD2gfR4xzrgGoMbMbB+66h/7LOUdkH+uEJzHKzNYCvweq+fdje/+V/uPUm4By4DTwfufcOS8hY5yZLaJ/AUiA/n/UbnLO/Y2ZTUH7OOLM7E7gC865d2gfR46ZzaJ/FA39U7Q/ds79/9rHkWVmS+hfEJkKHKf/VNpJRGAfq6hFRESimKa+RUREopiKWkREJIqpqEVERKKYilpERCSKqahFRESimIpaJIGYWd/AFZT2mtluM1s9cH+FmTkz+8qwbQvMrMfMvj1w+6/N7Au+soskKhW1SGK5NHAFpcXAl4C/HfbYceAdw26/H9g/keFE5M1U1CKJKwc4P+z2JeCgmQ1eBvEB+k/WICIeJfsOICITKmPgamDpwHTg7hGP/xR40MwagD6gDiie2IgiMpyKWiSxXBq4Ghhmdivw5Igrgv0K+ArQCDzlIZ+IjKCpb5EE5Zx7BSgACofd1w3sAv6M/iuziYhnGlGLJCgzm0v/BUfOApOGPfR1YItz7mz/RdpExCcVtUhiGTxGDWDAHznn+oYXsnNuP1rtLRI1dPUsERGRKKZj1CIiIlFMRS0iIhLFVNQiIiJRTEUtIiISxVTUIiIiUUxFLSIiEsVU1CIiIlFMRS0iIhLF/h/2psLNzQltdAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "sns.distplot(df['BMI'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAeoAAAFzCAYAAADxBEqxAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAgAElEQVR4nO3dd3wVdf798dc7ldBCixpIkAABKUovIiqChSiKXVAX0fUXXcVVd1e/WNa2rmVX17IqiKKuFcEGrigWBBVBCb1jaNKUAFIDqZ/fH/fqxpiQCySZyb3n6SOP3DvzmTsnI+Qwc+fOmHMOERER8acorwOIiIhI+VTUIiIiPqaiFhER8TEVtYiIiI+pqEVERHxMRS0iIuJjMV4HKEuTJk1cixYtvI4hIiJSLebMmbPVOZdU1jxfFnWLFi3IysryOoaIiEi1MLN15c3ToW8REREfU1GLiIj4mIpaRETEx1TUIiIiPqaiFhER8TEVtYiIiI+pqEVERHxMRS0iIuJjKmoREREfU1GLiIj4mIpaRETEx1TUIiIiPqaiFhER8bGQ7p5lZgOBJ4Bo4Hnn3EOl5ltw/plALjDcOTfXzNoCb5YY2hK4yzn3eGWEFzlYY+aMKXdeZrfMakwiIhKaCovazKKBp4HTgA3AbDOb5JxbWmJYBpAe/OoFjAJ6OedWAJ1LvM5G4N1K/QlERETCWCiHvnsC2c651c65fGAcMLjUmMHAyy5gFtDAzJJLjRkArHLOlXvPTREREfm1UIq6GbC+xPMNwWkHO2YI8MbBBhQREYlkoRS1lTHNHcwYM4sDzgEmlLsSs0wzyzKzrJycnBBiiYiIhL9QinoDkFrieQqw6SDHZABznXM/lrcS59wY51x351z3pKSkEGKJiIiEv1CKejaQbmZpwT3jIcCkUmMmAcMsoDew0zm3ucT8oeiwt4iIyEGr8Kxv51yhmY0AphD4eNYLzrklZnZtcP5oYDKBj2ZlE/h41pU/L29mtQmcMX5N5ccXEREJbyF9jto5N5lAGZecNrrEYwdcX86yuUDjw8goIiISsXRlMhERER9TUYuIiPiYilpERMTHVNQiIiI+pqIWERHxMRW1iIiIj6moRUREfExFLSIi4mMqahERER9TUYuIiPiYilpERMTHVNQiIiI+pqIWERHxMRW1iIiIj6moRUREfExFLSIi4mMqahERER9TUYuIiPiYilpERMTHVNQiIiI+pqIWERHxMRW1iIiIj6moRUREfExFLSIi4mMqahERER9TUYuIiPiYilpERMTHVNQiIiI+pqIWERHxMRW1iIiIj6moRUREfExFLSIi4mMqahERER9TUYuIiPiYilpERMTHQipqMxtoZivMLNvMRpYx38zsyeD8hWbWtcS8Bmb2lpktN7NlZnZ8Zf4AIiIi4azCojazaOBpIANoDww1s/alhmUA6cGvTGBUiXlPAB85544BOgHLKiG3iIhIRAhlj7onkO2cW+2cywfGAYNLjRkMvOwCZgENzCzZzOoDJwFjAZxz+c65HZWYX0REJKyFUtTNgPUlnm8ITgtlTEsgB3jRzOaZ2fNmVucw8oqIiESUUIraypjmQhwTA3QFRjnnugB7gd+8xw1gZplmlmVmWTk5OSHEEhERCX+hFPUGILXE8xRgU4hjNgAbnHPfBKe/RaC4f8M5N8Y519051z0pKSmU7CIiImEvlKKeDaSbWZqZxQFDgEmlxkwChgXP/u4N7HTObXbO/QCsN7O2wXEDgKWVFV5ERCTcxVQ0wDlXaGYjgClANPCCc26JmV0bnD8amAycCWQDucCVJV7iBuC1YMmvLjVPREREDqDCogZwzk0mUMYlp40u8dgB15ez7Hyg+2FkFBERiVi6MpmIiIiPqahFRER8TEUtIiLiYypqERERH1NRi4iI+JiKWkRExMdU1CIiIj6mohYREfExFbWIiIiPqahFRER8TEUtIiLiYypqERERH1NRi4iI+JiKWkRExMdU1CIiIj6mohYREfExFbWIiIiPqahFRER8TEUtIiLiYypqERERH1NRi4iI+JiKWkRExMdU1CIiIj6mohYREfExFbWIiIiPqahFRER8TEUtIiLiYypqERERH1NRi4iI+JiKWkRExMdU1CIiIj6mohYREfExFbWIiIiPqahFRER8TEUtIiLiYyEVtZkNNLMVZpZtZiPLmG9m9mRw/kIz61pi3lozW2Rm880sqzLDi4iIhLuYigaYWTTwNHAasAGYbWaTnHNLSwzLANKDX72AUcHvPzvFObe10lKLiIhEiFD2qHsC2c651c65fGAcMLjUmMHAyy5gFtDAzJIrOauIiEjECaWomwHrSzzfEJwW6hgHfGxmc8wss7yVmFmmmWWZWVZOTk4IsURERMJfKEVtZUxzBzHmBOdcVwKHx683s5PKWolzboxzrrtzrntSUlIIsURERMJfKEW9AUgt8TwF2BTqGOfcz9+3AO8SOJQuIiIiIQilqGcD6WaWZmZxwBBgUqkxk4BhwbO/ewM7nXObzayOmdUDMLM6wOnA4krMLyIiEtYqPOvbOVdoZiOAKUA08IJzbomZXRucPxqYDJwJZAO5wJXBxY8E3jWzn9f1unPuo0r/KURERMJUhUUN4JybTKCMS04bXeKxA64vY7nVQKfDzCgiIhKxdGUyERERH1NRi4iI+JiKWkRExMdU1CIiIj6mohYREfGxkM76FpEDGzNnTLnzMruVe+VcEZEKaY9aRETEx1TUIiIiPqaiFhER8TEVtYiIiI+pqEVERHxMRS0iIuJjKmoREREfU1GLiIj4mIpaRETEx1TUIiIiPqaiFhER8TEVtYiIiI+pqEVERHxMRS0iIuJjKmoREREfU1GLiIj4mIpaRETEx1TUIiIiPqaiFhER8TEVtYiIiI+pqEVERHxMRS0iIuJjKmoREREfU1GLiIj4mIpaRETEx1TUIiIiPqaiFhER8TEVtYiIiI+pqEVERHwsJpRBZjYQeAKIBp53zj1Uar4F558J5ALDnXNzS8yPBrKAjc65QZWUXSLYmDljyp2X2S2zGpOIiFStCveogyX7NJABtAeGmln7UsMygPTgVyYwqtT8G4Flh51WREQkwoRy6LsnkO2cW+2cywfGAYNLjRkMvOwCZgENzCwZwMxSgLOA5ysxt4iISEQIpaibAetLPN8QnBbqmMeBW4HiA63EzDLNLMvMsnJyckKIJSIiEv5CKWorY5oLZYyZDQK2OOfmVLQS59wY51x351z3pKSkEGKJiIiEv1CKegOQWuJ5CrApxDEnAOeY2VoCh8z7m9mrh5xWREQkwoRS1LOBdDNLM7M4YAgwqdSYScAwC+gN7HTObXbO3eacS3HOtQguN9U5d3ll/gAih6KouIiCogKvY4iIVKjCj2c55wrNbAQwhcDHs15wzi0xs2uD80cDkwl8NCubwMezrqy6yCKH58c9PzIqaxQFxQXc2udWEmsleh1JRKRcIX2O2jk3mUAZl5w2usRjB1xfwWtMA6YddEKRSrTox0WMnTeWKIuioLiAZ2Y/w5/7/Jm46Divo4mIlElXJpOI8a+Z/+Lp2U/TpHYT7jjxDq7ucjXrdq5j7NyxFLsDfihBRMQzKmqJCEtzlnLLJ7fQ6ahO3HrCrTSu3ZhOR3Xi4g4XM//H+by19C2vI4qIlCmkQ98iNd3tn91O3bi6/O643/3qMHf/tP5s3rOZz9Z8xpqf1pDWMM3DlCIiv6U9agl7M76fwcQVExl5wkjqxtX9zfwzWp0BwISlE6o7mohIhVTUEtacc9z66a0k103mxt43ljmmSe0mtEhswfgl46s5nYhIxVTUEtYmrZjE1+u/5t5+91I7tna547o37c6czXPI3p5djelERCqmopawVVhcyMjPRtK2cVuu7HLgj/Z3Te4KwIQlOvwtIv6iopaw9dL8l1i+dTkPDniQmKgDnzfZuHZjeqf0ZvxSHf4WEX9RUUtYyi3I5e5pd9M7pTfnHnNuSMtc0uES5v8wn5XbVlZxOhGR0KmoJSw9+c2TbNq9iYdPfRizsm7u9lsXtr8QQCeViYivqKgl7GzL3cZDXz3EoDaDOOnok0JeLqV+CieknqCiFhFfUVFL2HngywfYnb+bBwc8eNDLXtLhEhZtWcTyrcurIJmIyMFTUUtY2Zq7ladmP8UVna6g4xEdD3r5wccMBmDyd5MrGCkiUj1U1BI2nHO8uvBV4qLjuLffvYf0Gs0Tm9OuSTs+yv6oktOJiBwaFbWEjZkbZrJs6zIeGvAQqYmph/w6Ga0zmL5uOnvz91ZiOhGRQ6OilrCwc/9OJiydQKuGrfhDjz8c1msNbD2Q/KJ8pq+bXknpREQOnYpawsK4xePIL8pnWKdhRNnh/bE+8egTSYhJ0OFvEfEFFbXUeHM3z2XuD3M5u83ZHFX3qMN+vVoxtTgl7RQVtYj4gu5HLTXa3vy9vLH4DVLrp3Jay9MAGDNnzGG/bkbrDCZ/N5lV21fRqlGrw349EZFDpT1qqdEmLJ3Anvw9DOs0jOio6Ep73YGtBwJor1pEPKeilhprac5SZm6YyRmtzqB5YvNKfe3WjVrTqmErPlqlohYRb6mopUbaX7ifVxe+ypF1juSs9LOqZB0DWw9k6pqp5BXmVcnri4iEQkUtNdL7K99n+77tDOs0jNjo2CpZR0brDHILcvny+y+r5PVFREKhopYaZ92OdUxbO40+qX1o3ah1la2nX4t+1I6tzTvL3qmydYiIVERFLTXOfdPvA2BQm0FVup46cXU4p+05jF8ynoKigipdl4hIeVTUUqOs2LqC/yz4DycdfRKNEhpV+fqGdhzKtn3b+HT1p1W+LhGRsqiopUa5e9rdxMfEk9E6o1rWN7D1QBrWasjri1+vlvWJiJSmopYaY8EPC3hzyZvc1Osm6sfXr5Z1xkXHcUG7C3hv+XvkFuRWyzpFREpSUUuNcde0u0iMT+Qvff5Sreu99NhL2ZO/h/+u/G+1rldEBFTUUkMs37qcSSsmcVPvm2iY0LBa133S0SeRXDeZNxa/Ua3rFREBFbXUEE/MeoL46Hiu63Fdta87OiqaIR2HMPm7yezYv6Pa1y8ikU1FLb63LXcb/1nwHy479jKOqHOEJxmGdhxKflE+by9925P1i0jkUlGL742ZM4Z9hfu4qfdNnmXo3rQ7xzQ5hie/fZJiV+xZDhGJPCpq8bWCogKemv0UA9IGcOyRx3qWw8z460l/ZeGPC5mwZIJnOUQk8qioxdcmLJ3Apt2buLn3zV5H4ZIOl9AhqQN3TbuLwuJCr+OISIQIqajNbKCZrTCzbDMbWcZ8M7Mng/MXmlnX4PRaZvatmS0wsyVmdm9l/wASvpxzPDbrMdo0bkNGevVc4ORAoqOi+dspf2PltpW8uvBVr+OISISosKjNLBp4GsgA2gNDzax9qWEZQHrwKxMYFZyeB/R3znUCOgMDzax3JWWXMPf1+q/J2pTFjb1uJMr8cfDn3GPOpVtyN+6dfi/5RflexxGRCBATwpieQLZzbjWAmY0DBgNLS4wZDLzsnHPALDNrYGbJzrnNwJ7gmNjgl6u09OJ7Y+aMOeD8zG6Z5c57bNZjNKzVkCs6XVHZsQ6ZmXF///vJeC2DsXPH8ocefzis1zvQ9jnQthGRyBHKbkozYH2J5xuC00IaY2bRZjYf2AJ84pz7pqyVmFmmmWWZWVZOTk6o+SVMrflpDe8uf5fMbpnUiavjdZxfOaPVGfRt3pf7vriPPfl7Kl5AROQwhFLUVsa00nvF5Y5xzhU55zoDKUBPM+tY1kqcc2Occ92dc92TkpJCiCXh7Klvn8Iwru9xvddRfsPM+Odp/+SHPT/w8FcPex1HRMJcKEW9AUgt8TwF2HSwY5xzO4BpwMCDTikRZXfebp6f9zwXdbiI1MTUihfwQO+U3gztOJRHZj7C+p3rK15AROQQhVLUs4F0M0szszhgCDCp1JhJwLDg2d+9gZ3Ouc1mlmRmDQDMLAE4FVheifklDL0w7wV25e3yxUeyDuTBAQ8CcPvU2z1OIiLhrMKids4VAiOAKcAyYLxzbomZXWtm1waHTQZWA9nAc8DPF2ROBj43s4UECv8T55xuQSTlKiou4slvn+T4lOPp2ayn13EO6OgGR/On3n/i1YWvsnbHWq/jiEiYCuWsb5xzkwmUcclpo0s8dsBv3kx0zi0EuhxmRokg7y5/l9U/reahAQ95HSUkI/uO5Pl5zzNh6QT+cvxfMCvrdA0RkUPnjw+nihC4wMn9X9xPm8ZtOL/d+V7HCUm9+HrcddJdZG/PZs2ONV7HEZEwFNIetUh1fN73/ZXvs+DHBbw0+CWio6Ir5TWrw7BOw/jzx39m+rrptGzY0us4IhJmtEctvuCc429f/I20BmlceuylXsc5KPXi69E7pTdZm7L0uWoRqXQqavGFKaumkLUpi9v63kZsdKzXcQ7ayUefTGFxIV+v/9rrKCISZlTU4jnnHPdNv4/U+qlc0dk/lws9GM3qN6N1o9Z8se4L3a9aRCqVilo8N3XNVGZumMnIviOJi47zOs4hO/nok8nJzWH5Vl0qQEQqj4paPOWc446pd9CsXjOu6nKV13EOS5ejulAvrh7T1073OoqIhBEVtXhq0opJfLPxG+7pdw+1Ymp5HeewxEbHckLqCSz4cQE/7fvJ6zgiEiZU1OKZYlfMHVPvoE3jNgzvPNzrOJWiT2ofHI65m+d6HUVEwoSKWjzzzcZvWJKzhL+d8jdiosLjI/1H1j2SlHopzP1BRS0ilUNFLZ4oKCrg/RXv0zW5Kxe2v9DrOJWqS3IXVm1fxc79O72OIiJhQEUtnvjq+6/Ytm8bD/R/gCgLrz+GXZO74nDM+2Ge11FEJAyE129IqRHyi/KZnD2Z9EbpnN7qdK/jVLqm9ZqSXDdZ71OLSKVQUUu1+2LdF+zK28U5bc8J27tNdUnuwsptK9mdt9vrKCJSw6mopVrlFebxUfZHHNPkGNo0buN1nCrz8+Hv+T/M9zqKiNRwKmqpVtPXTWd3/m7ObnO211GqVEq9FI6ofYTO/haRw6ailmqzv3A/U1ZNoX1Se1o3au11nCplZnRN7sryrcvZvm+713FEpAZTUUu1mbZ2Gnvy94T93vTPuiR3odgV897y97yOIiI1mIpaqkV+UT6frP6EjkkdadmwpddxqsXRiUfTpHYT3lzyptdRRKQGU1FLtZjx/Qz25O8hIz3D6yjVxszo0bQHn63+jC17t3gdR0RqKBW1VLmi4iI+Wf0JrRq2Cvv3pkvr0bQHRa6It5a+5XUUEamhwuMCy+JrszfNZtu+bQzpOOSglhszZ0wVJao+zeo3o0NSB8YtHsd1Pa7zOo6I1EDao5YqVeyKmbJqCk3rNaXjER29juOJIR2H8OX3X7Jh1wavo4hIDaSiliq1eMtiNu3exBmtzgi7a3qH6pIOlwAwfsl4j5OISE0Umb85pdpMWTWFxgmN6dG0h9dRPJPeOJ1uyd0Yt3ic11FEpAZSUUuV+er7r8jens2pLU8lOira6zieGtpxKLM3zSZ7e7bXUUSkhlFRS5V5eMbD1I2rS9/mfb2O4rmLO1wMwOuLXvc4iYjUNCpqqRKLtyzmvyv/S/8W/YmLjvM6judSE1M5vdXpPD37aXILcr2OIyI1iIpaqsQ/ZvyDOrF16Nein9dRfOPOE+9ky94tPDfnOa+jiEgNoqKWSrduxzpeX/Q613S7hjpxdbyO4xsnHn0iJx19Ev/4+h/kFeZ5HUdEaggVtVS6R2c+SpRFcfPxN3sdxXfuPPFONu3exEvzX/I6iojUECpqqVQ5e3N4fu7zXH7c5aTUT/E6ju+c2vJUejXrxUMzHqKgqMDrOCJSA+gSolKpHvjyAfKK8vi/E/7P6yi+ZGbcedKdnP3G2by26LUqWUdFl17N7JZZJesVkaqhPWqpNOt2rOOZrGe4svOVtG3S1us4vnVW+ll0OaoLd0y9g537d3odR0R8TnvUUmnunnY3hnH3yXeHvEw43HjjYJkZLw5+kePHHs+YuWO4uffNxETpr6KIlC2kPWozG2hmK8ws28xGljHfzOzJ4PyFZtY1OD3VzD43s2VmtsTMbqzsH0D8YfGWxby84GVG9BxBamKq13F8r9NRnRh7zliyt2czYekEr+OIiI9VWNRmFg08DWQA7YGhZta+1LAMID34lQmMCk4vBP7snGsH9AauL2NZCQN3Tr2TevH1uK3vbV5HqTGGHjuUU1ueyrS105i5YabXcUTEp0LZo+4JZDvnVjvn8oFxwOBSYwYDL7uAWUADM0t2zm12zs0FcM7tBpYBzSoxv/jA1+u/ZuKKidza51Ya127sdZwa5fxjzqdt47a8uvBVlm1d5nUcEfGhUIq6GbC+xPMN/LZsKxxjZi2ALsA3Za3EzDLNLMvMsnJyckKIJX5Q7Iq54cMbSK6bzI299c7GwYqOiuaabtdwRJ0jGDV7FGt+WuN1JBHxmVCK2sqY5g5mjJnVBd4GbnLO7SprJc65Mc657s657klJSSHEEj/4ct2XzN08l3+d8S/qxtX1Ok6NVCeuDjf1uol68fX497f/ZuOujV5HEhEfCaWoNwAlzw5KATaFOsbMYgmU9GvOuXcOPar4ze683by34j1OaXEKl3S4xOs4NVpircRfzv5+4psn2LF/h9eRRMQnQinq2UC6maWZWRwwBJhUaswkYFjw7O/ewE7n3GYzM2AssMw5969KTS6ee3f5u+wv3M9TZz5F4H+1HI4mtZtwY68byS3I5cX5L1Lsir2OJCI+UGFRO+cKgRHAFAIng413zi0xs2vN7NrgsMnAaiAbeA64Ljj9BOB3QH8zmx/8OrOyfwipfqt+WsWM9TM4Ne1U2ifpRP7K0qx+My7pcAnLty7nXzP1b1sRCfGCJ865yQTKuOS00SUeO+D6Mpb7irLfv5YarNgVM37xeBrEN+CsNmd5HSfs9G3el8U5i7n9s9vpn9afrsldvY4kIh7SJUTloM3ZNIe1O9cy+JjB1Iqp5XWcsGNm/O6433FEnSO49O1L2Zu/1+tIIuIhXbdQDkpBUQHvLn+XlHop9E7pDUTmZUCrWt24urx83ssMeHkA906/l3+c9g+vI4mIR7RHLQdl2rppbNu3jQvaX0CU6Y9PVeqf1p8rO1/J47MeZ+W2lV7HERGP6DethGxv/l4mfzeZ9kntdQJZNXlwwIMkxCZw00c3ETgVREQijYpaQvZh9ofsK9jHBe0u8DpKxDiy7pHcffLdfJj9IR9894HXcUTEAypqCUluQS7T102nZ7OepNRP8TpORBnRcwTHNDmGmz66ibzCPK/jiEg1U1FLSGaun0l+UT6ntjzV6ygRJy46jicHPsmqn1bx6MxHvY4jItVMRS0VKnbFTFs3jZYNW9I8sbnXcSLSaa1O4/x253P/F/ezdsdar+OISDVSUUuFPln1CVv2buGUFqd4HSWiPX7G40RZFH/88I9eRxGRaqSilgo9Nfsp6sfX1xWyPJaamMo9/e7h/ZXvM3H5RK/jiEg1UVHLAa35aQ0frPyAE5ufSEyUro/jtRt73UjHIzryx4/+qCuWiUQIFbUc0KisUURZFCc2P9HrKALERscy6qxRfL/ze+6dfq/XcUSkGqiopVx5hXmMnTeW89udT8OEhl7HkaC+zfuS2TWTR75+hI9Xfex1HBGpYipqKdcnqz9h+77tDO883OsoUspjAx+jfVJ7Ln/ncjbt3uR1HBGpQipqKdf4JeNpWKuhPjvtQ7VjazPhognkFuQy9O2hFBYXeh1JRKqIzg6SMuUV5jFxxUQubHchcdFxXsfxhUO9S1hV3V2sXVI7Rg8aze/e/R13fX4XDwx4oErWIyLe0h61lOnjVR+zK28XF3e42OsocgCXH3c5V3e5mge/epA3Fr3hdRwRqQLao5YyjV86nkYJjeif1t/rKFKBp858ipXbV3LlxCt15TiRMKQ9avmN/YX7mbh8Iucdcx6x0bFex5EKxMfE887F79A8sTnnvnkuOXtzvI4kIpVIRS2/MSV7Crvzd+uwdw3SuHZjPrj0A4pdMf/+9t/sK9jndSQRqSQqavmN8UvH0zihsa7tXcOkN07n3UveJSc3h5cWvIRzzutIIlIJVNTyK/sK9jFpxSTOb3e+DnvXQCcdfRLntzuf+T/M59M1n3odR0QqgU4mk1/5ZPUn7Mnfw4XtL/Q6ihyiU9NOJXt7Nu8se4e0Bmm0btQ65GUP9FGyzG6ZlRFPRA6S9qjlVyYun0j9+Pr0a9HP6yhyiMyM4Z2G0zihMc/NeY7debu9jiQih0FFLb8oKi7i/ZXvc2b6mbrISQ2XEJvANd2vYU/BHt5YrM9Xi9RkOvQtv5i1YRY5uTkMbjvY6yieqKoriHkltX4qg9oM4r3l7zF381zdT1ykhtIetfxi4oqJxEbFktE6w+soUklOb3k6zROb8/qi19mTv8frOCJyCFTU8ouJKybSr0U/Emsleh1FKkl0VDRXdLqC3IJc3lzyptdxROQQqKgFgOVbl7Ny28qIPewdzlLqp5CRnsG3G79lwY8LvI4jIgdJRS1A4GxvgHPanuNxEqkKGa0zSKmXwmsLX2PH/h1exxGRg6CTyQQIHPbumtyV1MRUr6NIFYiJimFYp2E8NOMh/jTlT7ww+IVqW7c+my1yeLRHLfy450dmbZilw95h7ugGR3N6q9N5cf6LfJT9kddxRCREKmph0opJOJyKOgIMSh9EuybtyHw/k115u7yOIyIhUFELE5ZOoFXDVhx35HFeR5EqFhsdywuDX2Dj7o3c9NFNunGHSA0QUlGb2UAzW2Fm2WY2soz5ZmZPBucvNLOuJea9YGZbzGxxZQaXyrE1dytT10zl4g4XY2Zex5Fq0DulN7f1vY0X57/I07Of9jqOiFSgwqI2s2jgaSADaA8MNbP2pYZlAOnBr0xgVIl5LwEDKyOsVL73lr9HkSviovYXeR1FqtF9p9zH2W3O5qaPbuLT1brLloifhbJH3RPIds6tds7lA+OA0m9mDgZedgGzgAZmlgzgnPsC2F6ZoaXyjF8ynlYNW9H5qM5eR5FqFGVRvHb+axzT5BgumnAR3237zutIIlKOUIq6GbC+xPMNwfPxXe4AABReSURBVGkHO0Z85ufD3he1v0iHvSNQvfh6TBo6iWiL5szXz2TNT2u8jiQiZQilqMv6DV76DJRQxhx4JWaZZpZlZlk5OTkHs6gcop8Pe1/c4WKvo4hHWjZsyaShk9iWu43eY3uzdsdaryOJSCmhFPUGoORVMFKATYcw5oCcc2Occ92dc92TkpIOZlE5RD+f7a3D3pGtT2ofZlw1g9qxtXl05qMs/HGh15FEpIRQrkw2G0g3szRgIzAEuLTUmEnACDMbB/QCdjrnNldqUqlU23K38dnqz7ilzy067F0DVfYtOdsltWPm72fS6/lePDP7Gc5pew4DWw8kyvQJThGvVfi30DlXCIwApgDLgPHOuSVmdq2ZXRscNhlYDWQDzwHX/by8mb0BzATamtkGM/t9Jf8Mcgh+Odu7g872loCj6h7FX47/Cz2a9mDiiok8Pftp9ubv9TqWSMQL6VrfzrnJBMq45LTRJR474Ppylh16OAGlary04CXSG6XT5aguXkeRclT2XnMo4mPiuarLVbRq1IrxS8bz9y//zh96/IHU+roGvIhXdFwrAi3espivvv+KzG6ZOuwtv2Fm9GvRj1v63EKRK+KRrx9hac5Sr2OJRCwVdQR6NutZ4qPjGd55uNdRxMfSGqYx8oSRNE5ozL+//Tf/mf8fryOJRCQVdYTZk7+Hlxe+zEUdLqJJ7SZexxGfa5jQkFv63EKbxm0YPnE4D3/1sNeRRCKO7kcdYcYtHseuvF1c2+3aigeLAAmxCdzQ8wa++v4rRn42kn2F+7j75Lv1tolINVFRR5jRWaPpeERH+qT28TqK1CAxUTG8ct4rxMfEc+/0e8krzOOBAQ+orEWqgYo6gszeOJs5m+fw9JlP6xesHLToqGjGnjOW+Oh4HprxELvzd/P4wMeJidKvEZGqpL9hEWRU1ijqxNbh8uMu9zqK1FBRFsWos0ZRL64ej8x8hFU/rWLcBeNIrJXodTSRsKWTySJE9vZsXln4Cld0uoL68fW9jiM1mJnxz9P/ybODnuXT1Z9y/NjjWbV9ldexRMKW9qgjxF8//ytx0XHcedKdXkcRj1XWhVQyu2WS3iidC8ZfQJdnuzCy70hu7n0zCbEJlfL6IhKgoo4AczfPZdzicdze93aS6yWXO86LK2FJzXZK2ilkZWbxpyl/4o6pdzA6azT397+foR2HEhsd63U8kbCgQ98R4PbPbqdRQiNuPeFWr6NIGGrZsCXvDXmPz6/4nKQ6SVzx3hUc/fjR3DPtHjbu2uh1PJEaT0Ud5j5f8zlTVk3htr636YQfqVL9WvRj9v+bzftD36fzUZ25b/p9tHiiBW8ueZPcglyv44nUWCrqMFZUXMT/ffp/pNRPYUTPEV7HkQgQZVEMajOIyZdN5rsbvuOqzlfx+ZrPuevzu/jq+68odsVeRxSpcfQedRh75OtHmL1pNq+e9yq1Ymp5HUciTKtGrXj27GdJqpPEuMXjeGXhKyzJWcLVXa4mOira63giNYb2qMPQmDljuHPqndwx9Q66JndlT/4exswZo5PFxBPNE5tzS59bOL/d+czdPJdn5zxLQVGB17FEagwVdRjKL8rnhXkvUDeuLpcde5muQiaeMzPOaHUGQzoOYcGPCxiVNYr8onyvY4nUCCrqMPTusnfZvGczwzsPp25cXa/jiPzilBan8LvjfsfSnKWMmTNG71mLhEBFHWbeXPwmU9dOpX+L/rRPau91HJHf6Nu8Lxd3uJhFWxbx9y/+7nUcEd/TyWRh5PM1nzPsvWG0btSa89udX+YYvU8th+pAf3Yyu2Ue1Gud0uIU1u5Yy93T7qZHsx4MbD3wcOOJhC3tUYeJRT8u4tw3z6V1o9Zc1/06XRVKfM3MuPy4yzn2yGO59O1LWfPTGq8jifiW9qjDwNoda8l4LYO6cXX58LIP+Sj7I68jiVQoLjqOty9+m+5junPB+AuYcdWMarlOeGUeGRCpDtqjruEW/riQPmP7sLdgLx9e9iHNE5t7HUkkZK0bteaV815h3g/zuG7ydTjnvI4k4jsq6hps+trpnPTiSURZFF9d+RXHHXmc15FEDtrZbc/mzhPv5KX5L/Hc3Oe8jiPiOyrqGur1Ra9zxqtn0LReU77+/dd0OKKD15FEDtk9/e7h9Fanc8OHN/Dtxm+9jiPiK3qPuobJLcjlxg9v5Pl5z9O6UWuu7nq13pOWGi86KprXz3+dbmO6ccH4C/j6qq9JTUz1OpaIL2iPugZZsmUJPZ/ryfPznmdg64H8qfefdEETCRuNazfm3UveZVfeLga8PIDNuzd7HUnEF1TUNUBeYR73TLuHrmO6smXvFj667CPOO+Y83dhAwk6X5C58eNmHbNq9iQEvD2DL3i1eRxLxnA59+9TPHyFZuW0lry16jR/2/ECPpj24uMPFrNu5zuN0IlWnT2ofPrj0AzJey+C0V07jg0s/IKV+itexRDyjPWqf2pq7lTFzxvDozEcpKCrghp43cHXXq6kfX9/raCJV7uQWJzNxyESyt2fT4ZkOjJ07Vh/dkoilPWqf2ZW3iwe+fIBHZz6KYQxKH8TprU4nPibe62gi5aqKS9Oe1uo0Fl67kKvfv5qr37+a8UvHc8/J99ArpRdRduB9DOccq35aRdamLJbmLGXZ1mWs3LaSwuJCduftJjoqmiPrHEn7pPa0a9KOxFqJlZ5fpLKoqH2iqLiIsfPG8tfP/8qWvVvondKbc9ueS8OEhl5HE/HMZ2s+45IOl5BcN5l3lr1Dn1V9SIxPpPNRnbn8uMupH1+fenH1yC/KZ82ONaz5aQ3Lty1n9sbZ/LT/JwCiLIpWDVvRtklbasXUYuW2lRQUFbAkZwnfbPwGgLQGaZzW8jSKuhTp3A/xHfPj4aTu3bu7rKwsr2NUC+ccH3z3Abd/djuLtiyib/O+PHbGY8zdPNfraCK+kluQy6IfFzH/h/kszllc5v2s68TWoXWj1vRo2oNeKb3o3rQ77Zq0+9URqZ/3/otdMRt2bWBpzlJmfD+DLblbaN2oNbf0uYXhnYcTFx1XbT+biJnNcc51L3Oeitobzjk+Xf0pf/38r3yz8RtaNmzJw6c+zAXtLsDMdJcrkQMoKCrgnLbnsCtvF7vydhETFUNawzQaJzTGzA64bFl/t4pdMfM2z2PuD3PJ2pRFWoM07u13L5cee6n2sKVaHKiodTJZNSsoKuCNRW/Qe2xvTn/1dDbv2cxzZz/H8uuXc2H7Cyv8JSMiEBsdS2piKh2O6MDxqcfTo1kPmtRucsh/f6Isim5Nu/Ht1d8y+dLJNKjVgGHvDeO40cfx8oKXy9x7F6kuKupqsmLrCu6ddi9pT6Rx6TuXsmP/Dp458xlWjljJ1V2v1m0pRXzAzMhIzyArM4sJF00gyqK44r0rSHsijYe+ekgXYRFPhHQymZkNBJ4AooHnnXMPlZpvwflnArnAcOfc3FCWDVf5Rflkbcpi6pqpvL3sbeb/MB/DGNByAM8OepaM9IwKz1wVkUNzuG8dRVkUF7a/kAvaXcDHqz7m0ZmPcttnt3H7Z7dzfOrxnHfMeZza8lTaJ7U/7PeyddtNqUiF71GbWTSwEjgN2ADMBoY655aWGHMmcAOBou4FPOGc6xXKsmWpSe9RO+fYsX8H2duzWbxlMYu2LGLBjwuYtWEWuQW5APRq1ouhHYdyUYeLaFqv6S/L6n1oEX85UDHeO+1e5v4wl3mb57F+13oAYqJiaFqvKSc2P5Fm9ZrRrH4zjqhzBHVi65AQm0B8dDz5RfnkFeWxv3A/+wv3k1f4v8f7C/czY/0MCooLKCwqpKC4gGJXTFx0HHHRcfRJ7UOd2DrUjq1N7dja1IuvR2J8IvXj65NYK/g9PpFaMbX0tlkNd6D3qEPZo+4JZDvnVgdfbBwwGChZtoOBl12g9WeZWQMzSwZahLCsJ5xzOBzFrphiV0xRcRH7Cvexr2Af+wr3kVuQ+8vjn/b9RE5uDltzt5KzN+eXx5v3bGbtjrXsytv1y+vGRsWSXC+ZXs160aZxG+7vfz9Najfx8CcVkVAd6B/PyfWSOaveWZyVfhbbcrexesdqvt/5Pet3rmfG+hls2r3pkN/Ljo2KJTY6lpioGKKIIr84n/yifKasmhLS8lEWRUJMAgmxCSTEJJDWMI3E+ETqxdf7VdGX/EqISfjlcXxMPDFRMURbdOB7VOD7oUwL5Uhh6d+9xa6YIlf0y/OSj0vPq2iswxFt0URHRRNlUb88jrbg8+Dj0vMPNDbKojz9h1AoRd0MWF/i+QYCe80VjWkW4rJVqu1TbVm/c/0vfyh+/nIc2tnudePqklQ7iSa1m9A8sTknH30ym/dspklCE5rWa0pSnaRf/UF9Z9k7lfWjiIhPNK7dmMa1G9OjaQ8gsCfunGPbvm1s2buFfQWBf+znFeURFx1HrZha1IqpRXx0fOB7TDwJMQnUiqnFS/NfKrcEioqLKCguCOyVB/fE9xUGdiD2F+z/1fN9Bft+2Us3jA27NrArbxe5Bbm/fBUUF1TnZgorhv2q5P9x6j+4vuf11bLuUIq6rD9BpVuuvDGhLBt4AbNM4OfjTnvMbEUI2SpTE2BrRYP2BP9bw5pqiOQ7IW2jCKbtc2Bhu32u4ZrKeqmw3UaVxLPt43AUBv8DGHHHCEYwojJXcXR5M0Ip6g1AyRvDpgCbQhwTF8KyADjnxgCevWlrZlnlvT8gAdpGB6btc2DaPhXTNjqwSN0+oZx2PBtIN7M0M4sDhgCTSo2ZBAyzgN7ATufc5hCXFRERkXJUuEftnCs0sxHAFAIfsXrBObfEzK4Nzh8NTCZwxnc2gY9nXXmgZavkJxEREQlDIX2O2jk3mUAZl5w2usRjB5T5rnpZy/qUPitVMW2jA9P2OTBtn4ppGx1YRG4fX17rW0RERAJ0aSwREREfi9iiNrNoM5tnZv8NPm9kZp+Y2XfB7xF9I+jgRWveMrPlZrbMzI7XNvofM7vZzJaY2WIze8PMakX69jGzF8xsi5ktLjGt3G1iZreZWbaZrTCzM7xJXX3K2T7/DP4dW2hm75pZgxLzIn77lJj3FzNzZtakxLSI2T4RW9TAjcCyEs9HAp8559KBz4LPI9kTwEfOuWOATgS2lbYRYGbNgD8C3Z1zHQmcKDkEbZ+XgIGlppW5TcysPYFt1iG4zDPBSw6Hs5f47fb5BOjonDuOwOWWbwNtn5LMLJXAZai/LzEtorZPRBa1maUAZwHPl5g8GPhP8PF/gHOrO5dfmFl94CRgLIBzLt85twNto5JigAQziwFqE7g+QERvH+fcF8D2UpPL2yaDgXHOuTzn3BoCnxjpWS1BPVLW9nHOfeycKww+nUXgWhOg7VPSY8Ct/PpiWRG1fSKyqIHHCfyPLy4x7cjgZ78Jfj/Ci2A+0RLIAV4Mvj3wvJnVQdsIAOfcRuARAv/C30zgugEfo+1TlvK2SXmXHY5kVwEfBh9r+wBmdg6w0Tm3oNSsiNo+EVfUZjYI2OKcm+N1Fh+LAboCo5xzXYC9RN5h3HIF32cdDKQBTYE6Zna5t6lqnJAvLxwJzOwOoBB47edJZQyLqO1jZrWBO4C7yppdxrSw3T4RV9TACcA5ZrYWGAf0N7NXgR+Dd/wi+H2LdxE9twHY4Jz7Jvj8LQLFrW0UcCqwxjmX45wrAN4B+qDtU5bytkkolyaOCGZ2BTAIuMz97/Oy2j7QisA/hhcEf1+nAHPN7CgibPtEXFE7525zzqU451oQOBlhqnPucgKXNr0iOOwKYKJHET3nnPsBWG9mbYOTBhC4Nam2UcD3QG8zq22B2x4NIHCynbbPb5W3TSYBQ8ws3szSgHTgWw/yecrMBgL/B5zjnMstMSvit49zbpFz7gjnXIvg7+sNQNfg76eI2j4hXZksQjwEjDez3xP4RXyRx3m8dgPwWvAa7asJXBY2Cm0jnHPfmNlbwFwChyvnEbhiUl0iePuY2RtAP6CJmW0A7qacv1fByxCPJ/APwELgeudckSfBq0k52+c2IB74JPBvPmY5567V9glsH+fc2LLGRtr20ZXJREREfCziDn2LiIjUJCpqERERH1NRi4iI+JiKWkRExMdU1CIiIj6mohapQcysRVl3F6qE1+1sZmeWeD7czHLMbH7w7k43h/Aaw82saWVnE4l0KmqRCBe8sUhn4MxSs950znUmcDW/O4J3MTqQ4QQuqSoilUgXPBGpeaLN7DkCly3dSOC6402Bp4EkIBf4f8655WZ2NnAnEAdsI3CZyh/N7J7gMi2ArUBfAncD6ws8WHJlzrltZpYNJBO4Yt1dwNlAAvA1cA1wAdCdwEVy9gHHA+2BfxG4EMxWYPjPN+gQkdBpj1qk5kkHnnbOdQB2ECjJMcANzrluwF+AZ4JjvwJ6B2+uMo7AXeN+1g0Y7Jy7lMCND950znV2zr1ZcmVm1hyoBSwMTnrKOdcjeC/uBGCQc+4tIIvAPwQ6E7ha1L+BC4OZXgD+XqlbQSRCaI9apOZZ45ybH3w8h8BecR9gQvAylBC4LCUEblbwZvCGGHHAmhKvM8k5t+8A67nEzE4B2hLYQ98fnH6Kmd1K4D7cjYAlwPullm0LdOR/l8aMJnBLUBE5SCpqkZonr8TjIuBIYEdwT7a0fwP/cs5NMrN+wD0l5u2tYD1vOudGmNnxwAdm9iGBPfhngO7OufXBQ+i1yljWgCXOueND+YFEpHw69C1S8+0C1pjZRQAW0Ck4L5HA+9jwv7tYlWU3UK+sGc65mcArwI38r5S3mlld4MJyXmMFkBQsecws1sw6HNRPJSKAilokXFwG/N7MFhA4FD04OP0eAofEvyRwQld5PgfaBz+OdUkZ8x8mcAe1IuA5YBHwHjC7xJiXgNFmNp/Aoe4LgYeDmeYTODwvIgdJd88SERHxMe1Ri4iI+JiKWkRExMdU1CIiIj6mohYREfExFbWIiIiPqahFRER8TEUtIiLiYypqERERH/v/M5GolBpXaVUAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "sns.distplot(df['heartRate'],color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>male</th>\n",
       "      <th>age</th>\n",
       "      <th>education</th>\n",
       "      <th>currentSmoker</th>\n",
       "      <th>cigsPerDay</th>\n",
       "      <th>BPMeds</th>\n",
       "      <th>prevalentStroke</th>\n",
       "      <th>prevalentHyp</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>totChol</th>\n",
       "      <th>sysBP</th>\n",
       "      <th>diaBP</th>\n",
       "      <th>BMI</th>\n",
       "      <th>heartRate</th>\n",
       "      <th>glucose</th>\n",
       "      <th>TenYearCHD</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>male</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.028979</td>\n",
       "      <td>0.017205</td>\n",
       "      <td>0.197596</td>\n",
       "      <td>0.315630</td>\n",
       "      <td>-0.052204</td>\n",
       "      <td>-0.004546</td>\n",
       "      <td>0.005313</td>\n",
       "      <td>0.015708</td>\n",
       "      <td>-0.069974</td>\n",
       "      <td>-0.035989</td>\n",
       "      <td>0.057933</td>\n",
       "      <td>0.081506</td>\n",
       "      <td>-0.116601</td>\n",
       "      <td>0.005818</td>\n",
       "      <td>0.088428</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>age</th>\n",
       "      <td>-0.028979</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.163547</td>\n",
       "      <td>-0.213748</td>\n",
       "      <td>-0.191847</td>\n",
       "      <td>0.121980</td>\n",
       "      <td>0.057655</td>\n",
       "      <td>0.307194</td>\n",
       "      <td>0.101258</td>\n",
       "      <td>0.260270</td>\n",
       "      <td>0.394302</td>\n",
       "      <td>0.206104</td>\n",
       "      <td>0.135283</td>\n",
       "      <td>-0.012819</td>\n",
       "      <td>0.116850</td>\n",
       "      <td>0.225256</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>education</th>\n",
       "      <td>0.017205</td>\n",
       "      <td>-0.163547</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.018273</td>\n",
       "      <td>0.007618</td>\n",
       "      <td>-0.010610</td>\n",
       "      <td>-0.035150</td>\n",
       "      <td>-0.081021</td>\n",
       "      <td>-0.038136</td>\n",
       "      <td>-0.022479</td>\n",
       "      <td>-0.128273</td>\n",
       "      <td>-0.061719</td>\n",
       "      <td>-0.135518</td>\n",
       "      <td>-0.053700</td>\n",
       "      <td>-0.033700</td>\n",
       "      <td>-0.053383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>currentSmoker</th>\n",
       "      <td>0.197596</td>\n",
       "      <td>-0.213748</td>\n",
       "      <td>0.018273</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.760239</td>\n",
       "      <td>-0.048632</td>\n",
       "      <td>-0.032988</td>\n",
       "      <td>-0.103260</td>\n",
       "      <td>-0.044295</td>\n",
       "      <td>-0.046285</td>\n",
       "      <td>-0.130230</td>\n",
       "      <td>-0.107746</td>\n",
       "      <td>-0.167276</td>\n",
       "      <td>0.062348</td>\n",
       "      <td>-0.054157</td>\n",
       "      <td>0.019456</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cigsPerDay</th>\n",
       "      <td>0.315630</td>\n",
       "      <td>-0.191847</td>\n",
       "      <td>0.007618</td>\n",
       "      <td>0.760239</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.044826</td>\n",
       "      <td>-0.032244</td>\n",
       "      <td>-0.065046</td>\n",
       "      <td>-0.036150</td>\n",
       "      <td>-0.026816</td>\n",
       "      <td>-0.088375</td>\n",
       "      <td>-0.056687</td>\n",
       "      <td>-0.092332</td>\n",
       "      <td>0.073866</td>\n",
       "      <td>-0.056650</td>\n",
       "      <td>0.058859</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>BPMeds</th>\n",
       "      <td>-0.052204</td>\n",
       "      <td>0.121980</td>\n",
       "      <td>-0.010610</td>\n",
       "      <td>-0.048632</td>\n",
       "      <td>-0.044826</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.115003</td>\n",
       "      <td>0.259243</td>\n",
       "      <td>0.051571</td>\n",
       "      <td>0.078909</td>\n",
       "      <td>0.252047</td>\n",
       "      <td>0.192490</td>\n",
       "      <td>0.099552</td>\n",
       "      <td>0.015175</td>\n",
       "      <td>0.048905</td>\n",
       "      <td>0.086774</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>prevalentStroke</th>\n",
       "      <td>-0.004546</td>\n",
       "      <td>0.057655</td>\n",
       "      <td>-0.035150</td>\n",
       "      <td>-0.032988</td>\n",
       "      <td>-0.032244</td>\n",
       "      <td>0.115003</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.074830</td>\n",
       "      <td>0.006949</td>\n",
       "      <td>0.000067</td>\n",
       "      <td>0.057009</td>\n",
       "      <td>0.045190</td>\n",
       "      <td>0.024840</td>\n",
       "      <td>-0.017676</td>\n",
       "      <td>0.018055</td>\n",
       "      <td>0.061810</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>prevalentHyp</th>\n",
       "      <td>0.005313</td>\n",
       "      <td>0.307194</td>\n",
       "      <td>-0.081021</td>\n",
       "      <td>-0.103260</td>\n",
       "      <td>-0.065046</td>\n",
       "      <td>0.259243</td>\n",
       "      <td>0.074830</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.077808</td>\n",
       "      <td>0.163041</td>\n",
       "      <td>0.696755</td>\n",
       "      <td>0.615751</td>\n",
       "      <td>0.300572</td>\n",
       "      <td>0.147222</td>\n",
       "      <td>0.082924</td>\n",
       "      <td>0.177603</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>diabetes</th>\n",
       "      <td>0.015708</td>\n",
       "      <td>0.101258</td>\n",
       "      <td>-0.038136</td>\n",
       "      <td>-0.044295</td>\n",
       "      <td>-0.036150</td>\n",
       "      <td>0.051571</td>\n",
       "      <td>0.006949</td>\n",
       "      <td>0.077808</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.040092</td>\n",
       "      <td>0.111283</td>\n",
       "      <td>0.050329</td>\n",
       "      <td>0.086250</td>\n",
       "      <td>0.048993</td>\n",
       "      <td>0.605705</td>\n",
       "      <td>0.097317</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>totChol</th>\n",
       "      <td>-0.069974</td>\n",
       "      <td>0.260270</td>\n",
       "      <td>-0.022479</td>\n",
       "      <td>-0.046285</td>\n",
       "      <td>-0.026816</td>\n",
       "      <td>0.078909</td>\n",
       "      <td>0.000067</td>\n",
       "      <td>0.163041</td>\n",
       "      <td>0.040092</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.207609</td>\n",
       "      <td>0.163903</td>\n",
       "      <td>0.114789</td>\n",
       "      <td>0.090676</td>\n",
       "      <td>0.044583</td>\n",
       "      <td>0.081624</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sysBP</th>\n",
       "      <td>-0.035989</td>\n",
       "      <td>0.394302</td>\n",
       "      <td>-0.128273</td>\n",
       "      <td>-0.130230</td>\n",
       "      <td>-0.088375</td>\n",
       "      <td>0.252047</td>\n",
       "      <td>0.057009</td>\n",
       "      <td>0.696755</td>\n",
       "      <td>0.111283</td>\n",
       "      <td>0.207609</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.784002</td>\n",
       "      <td>0.325247</td>\n",
       "      <td>0.182174</td>\n",
       "      <td>0.134608</td>\n",
       "      <td>0.216429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>diaBP</th>\n",
       "      <td>0.057933</td>\n",
       "      <td>0.206104</td>\n",
       "      <td>-0.061719</td>\n",
       "      <td>-0.107746</td>\n",
       "      <td>-0.056687</td>\n",
       "      <td>0.192490</td>\n",
       "      <td>0.045190</td>\n",
       "      <td>0.615751</td>\n",
       "      <td>0.050329</td>\n",
       "      <td>0.163903</td>\n",
       "      <td>0.784002</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.376544</td>\n",
       "      <td>0.181246</td>\n",
       "      <td>0.058647</td>\n",
       "      <td>0.145299</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>BMI</th>\n",
       "      <td>0.081506</td>\n",
       "      <td>0.135283</td>\n",
       "      <td>-0.135518</td>\n",
       "      <td>-0.167276</td>\n",
       "      <td>-0.092332</td>\n",
       "      <td>0.099552</td>\n",
       "      <td>0.024840</td>\n",
       "      <td>0.300572</td>\n",
       "      <td>0.086250</td>\n",
       "      <td>0.114789</td>\n",
       "      <td>0.325247</td>\n",
       "      <td>0.376544</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.067544</td>\n",
       "      <td>0.082109</td>\n",
       "      <td>0.074680</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>heartRate</th>\n",
       "      <td>-0.116601</td>\n",
       "      <td>-0.012819</td>\n",
       "      <td>-0.053700</td>\n",
       "      <td>0.062348</td>\n",
       "      <td>0.073866</td>\n",
       "      <td>0.015175</td>\n",
       "      <td>-0.017676</td>\n",
       "      <td>0.147222</td>\n",
       "      <td>0.048993</td>\n",
       "      <td>0.090676</td>\n",
       "      <td>0.182174</td>\n",
       "      <td>0.181246</td>\n",
       "      <td>0.067544</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.089341</td>\n",
       "      <td>0.022898</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>glucose</th>\n",
       "      <td>0.005818</td>\n",
       "      <td>0.116850</td>\n",
       "      <td>-0.033700</td>\n",
       "      <td>-0.054157</td>\n",
       "      <td>-0.056650</td>\n",
       "      <td>0.048905</td>\n",
       "      <td>0.018055</td>\n",
       "      <td>0.082924</td>\n",
       "      <td>0.605705</td>\n",
       "      <td>0.044583</td>\n",
       "      <td>0.134608</td>\n",
       "      <td>0.058647</td>\n",
       "      <td>0.082109</td>\n",
       "      <td>0.089341</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.120406</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>TenYearCHD</th>\n",
       "      <td>0.088428</td>\n",
       "      <td>0.225256</td>\n",
       "      <td>-0.053383</td>\n",
       "      <td>0.019456</td>\n",
       "      <td>0.058859</td>\n",
       "      <td>0.086774</td>\n",
       "      <td>0.061810</td>\n",
       "      <td>0.177603</td>\n",
       "      <td>0.097317</td>\n",
       "      <td>0.081624</td>\n",
       "      <td>0.216429</td>\n",
       "      <td>0.145299</td>\n",
       "      <td>0.074680</td>\n",
       "      <td>0.022898</td>\n",
       "      <td>0.120406</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     male       age  education  currentSmoker  cigsPerDay  \\\n",
       "male             1.000000 -0.028979   0.017205       0.197596    0.315630   \n",
       "age             -0.028979  1.000000  -0.163547      -0.213748   -0.191847   \n",
       "education        0.017205 -0.163547   1.000000       0.018273    0.007618   \n",
       "currentSmoker    0.197596 -0.213748   0.018273       1.000000    0.760239   \n",
       "cigsPerDay       0.315630 -0.191847   0.007618       0.760239    1.000000   \n",
       "BPMeds          -0.052204  0.121980  -0.010610      -0.048632   -0.044826   \n",
       "prevalentStroke -0.004546  0.057655  -0.035150      -0.032988   -0.032244   \n",
       "prevalentHyp     0.005313  0.307194  -0.081021      -0.103260   -0.065046   \n",
       "diabetes         0.015708  0.101258  -0.038136      -0.044295   -0.036150   \n",
       "totChol         -0.069974  0.260270  -0.022479      -0.046285   -0.026816   \n",
       "sysBP           -0.035989  0.394302  -0.128273      -0.130230   -0.088375   \n",
       "diaBP            0.057933  0.206104  -0.061719      -0.107746   -0.056687   \n",
       "BMI              0.081506  0.135283  -0.135518      -0.167276   -0.092332   \n",
       "heartRate       -0.116601 -0.012819  -0.053700       0.062348    0.073866   \n",
       "glucose          0.005818  0.116850  -0.033700      -0.054157   -0.056650   \n",
       "TenYearCHD       0.088428  0.225256  -0.053383       0.019456    0.058859   \n",
       "\n",
       "                   BPMeds  prevalentStroke  prevalentHyp  diabetes   totChol  \\\n",
       "male            -0.052204        -0.004546      0.005313  0.015708 -0.069974   \n",
       "age              0.121980         0.057655      0.307194  0.101258  0.260270   \n",
       "education       -0.010610        -0.035150     -0.081021 -0.038136 -0.022479   \n",
       "currentSmoker   -0.048632        -0.032988     -0.103260 -0.044295 -0.046285   \n",
       "cigsPerDay      -0.044826        -0.032244     -0.065046 -0.036150 -0.026816   \n",
       "BPMeds           1.000000         0.115003      0.259243  0.051571  0.078909   \n",
       "prevalentStroke  0.115003         1.000000      0.074830  0.006949  0.000067   \n",
       "prevalentHyp     0.259243         0.074830      1.000000  0.077808  0.163041   \n",
       "diabetes         0.051571         0.006949      0.077808  1.000000  0.040092   \n",
       "totChol          0.078909         0.000067      0.163041  0.040092  1.000000   \n",
       "sysBP            0.252047         0.057009      0.696755  0.111283  0.207609   \n",
       "diaBP            0.192490         0.045190      0.615751  0.050329  0.163903   \n",
       "BMI              0.099552         0.024840      0.300572  0.086250  0.114789   \n",
       "heartRate        0.015175        -0.017676      0.147222  0.048993  0.090676   \n",
       "glucose          0.048905         0.018055      0.082924  0.605705  0.044583   \n",
       "TenYearCHD       0.086774         0.061810      0.177603  0.097317  0.081624   \n",
       "\n",
       "                    sysBP     diaBP       BMI  heartRate   glucose  TenYearCHD  \n",
       "male            -0.035989  0.057933  0.081506  -0.116601  0.005818    0.088428  \n",
       "age              0.394302  0.206104  0.135283  -0.012819  0.116850    0.225256  \n",
       "education       -0.128273 -0.061719 -0.135518  -0.053700 -0.033700   -0.053383  \n",
       "currentSmoker   -0.130230 -0.107746 -0.167276   0.062348 -0.054157    0.019456  \n",
       "cigsPerDay      -0.088375 -0.056687 -0.092332   0.073866 -0.056650    0.058859  \n",
       "BPMeds           0.252047  0.192490  0.099552   0.015175  0.048905    0.086774  \n",
       "prevalentStroke  0.057009  0.045190  0.024840  -0.017676  0.018055    0.061810  \n",
       "prevalentHyp     0.696755  0.615751  0.300572   0.147222  0.082924    0.177603  \n",
       "diabetes         0.111283  0.050329  0.086250   0.048993  0.605705    0.097317  \n",
       "totChol          0.207609  0.163903  0.114789   0.090676  0.044583    0.081624  \n",
       "sysBP            1.000000  0.784002  0.325247   0.182174  0.134608    0.216429  \n",
       "diaBP            0.784002  1.000000  0.376544   0.181246  0.058647    0.145299  \n",
       "BMI              0.325247  0.376544  1.000000   0.067544  0.082109    0.074680  \n",
       "heartRate        0.182174  0.181246  0.067544   1.000000  0.089341    0.022898  \n",
       "glucose          0.134608  0.058647  0.082109   0.089341  1.000000    0.120406  \n",
       "TenYearCHD       0.216429  0.145299  0.074680   0.022898  0.120406    1.000000  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_mat=df.corr()\n",
    "corr_mat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "sns.heatmap(corr_mat)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x576 with 64 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from pandas.plotting import scatter_matrix\n",
    "atr=['TenYearCHD','age','prevalentHyp','diabetes','glucose','currentSmoker','cigsPerDay','education']\n",
    "scatter_matrix(df[atr],figsize=(16,8),alpha=0.3,color='g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "y=df['TenYearCHD'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, ..., 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(['TenYearCHD','education','totChol','currentSmoker','heartRate','glucose'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x=np.array(df)"
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
       "array([[  1.  ,  39.  ,   0.  , ..., 106.  ,  70.  ,  26.97],\n",
       "       [  0.  ,  46.  ,   0.  , ..., 121.  ,  81.  ,  28.73],\n",
       "       [  1.  ,  48.  ,  20.  , ..., 127.5 ,  80.  ,  25.34],\n",
       "       ...,\n",
       "       [  0.  ,  48.  ,  20.  , ..., 131.  ,  72.  ,  22.  ],\n",
       "       [  0.  ,  44.  ,  15.  , ..., 126.5 ,  87.  ,  19.16],\n",
       "       [  0.  ,  52.  ,   0.  , ..., 133.5 ,  83.  ,  21.47]])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4238, 10)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "sca=StandardScaler()\n",
    "x=sca.fit_transform(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.1531919 , -1.23495068, -0.75132224, ..., -1.19590711,\n",
       "        -1.08262515,  0.28694273],\n",
       "       [-0.86715836, -0.41825733, -0.75132224, ..., -0.51518725,\n",
       "        -0.15898843,  0.71932499],\n",
       "       [ 1.1531919 , -0.18491638,  0.92920959, ..., -0.22020864,\n",
       "        -0.24295541, -0.11350221],\n",
       "       ...,\n",
       "       [-0.86715836, -0.18491638,  0.92920959, ..., -0.06137401,\n",
       "        -0.9146912 , -0.93404582],\n",
       "       [-0.86715836, -0.65159829,  0.50907663, ..., -0.26558997,\n",
       "         0.34481341, -1.63175357],\n",
       "       [-0.86715836,  0.28176554, -0.75132224, ...,  0.0520793 ,\n",
       "         0.00894551, -1.06425185]])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=200)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "lr=LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male               0\n",
       "age                0\n",
       "cigsPerDay         0\n",
       "BPMeds             0\n",
       "prevalentStroke    0\n",
       "prevalentHyp       0\n",
       "diabetes           0\n",
       "sysBP              0\n",
       "diaBP              0\n",
       "BMI                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "param={'C':[0.0001,0.001,0.01,0.1,1,10,100,1000],\n",
    "      'penalty':['l1','l2'],\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "grid=GridSearchCV(lr,param_grid=param,cv=5,scoring='accuracy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n",
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n",
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n",
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n",
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n",
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n",
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n",
      "C:\\Users\\tejak\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:536: FitFailedWarning: Estimator fit failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "ValueError: Solver lbfgs supports only 'l2' or 'none' penalties, got l1 penalty.\n",
      "\n",
      "  FitFailedWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "GridSearchCV(cv=5, error_score=nan,\n",
       "             estimator=LogisticRegression(C=1.0, class_weight=None, dual=False,\n",
       "                                          fit_intercept=True,\n",
       "                                          intercept_scaling=1, l1_ratio=None,\n",
       "                                          max_iter=100, multi_class='auto',\n",
       "                                          n_jobs=None, penalty='l2',\n",
       "                                          random_state=None, solver='lbfgs',\n",
       "                                          tol=0.0001, verbose=0,\n",
       "                                          warm_start=False),\n",
       "             iid='deprecated', n_jobs=None,\n",
       "             param_grid={'C': [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000],\n",
       "                         'penalty': ['l1', 'l2']},\n",
       "             pre_dispatch='2*n_jobs', refit=True, return_train_score=False,\n",
       "             scoring='accuracy', verbose=0)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8519174041297936"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid.best_score_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=0.01, class_weight=None, dual=False, fit_intercept=True,\n",
       "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
       "                   multi_class='auto', n_jobs=None, penalty='l2',\n",
       "                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,\n",
       "                   warm_start=False)"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid.best_estimator_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'C': 0.01, 'penalty': 'l2'}"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid.best_params_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score,confusion_matrix\n",
    "from sklearn.model_selection import StratifiedKFold\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.model_selection import cross_val_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.85377358, 0.85495283, 0.8490566 , 0.84769776, 0.85242031])"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sk=StratifiedKFold(n_splits=5,random_state=200,shuffle=True)\n",
    "l=LogisticRegression()\n",
    "result=cross_val_score(l,x,y,cv=sk)\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "85.15802165244703"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result.mean()*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#l=LogisticRegression(C=0.01,penalty='l2',class_weight='balanced')\n",
    "#l.fit(x_train,y_train);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
       "                   multi_class='auto', n_jobs=None, penalty='l2',\n",
       "                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,\n",
       "                   warm_start=False)"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=l.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8466981132075472"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "acc=accuracy_score(y_test,y_pred)\n",
    "acc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[710,   7],\n",
       "       [123,   8]], dtype=int64)"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "con=confusion_matrix(y_test,y_pred)\n",
    "con"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "\n",
       "        if (window._pyforest_update_imports_cell) { window._pyforest_update_imports_cell('import matplotlib.pyplot as plt\\nimport pandas as pd\\nimport numpy as np\\nimport seaborn as sns'); }\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>710</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>123</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     0  1\n",
       "0  710  7\n",
       "1  123  8"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cmdf=pd.DataFrame(data=con,columns=[0,1],index=[0,1])\n",
    "cmdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(l,open('detect.pkl','wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "model=pickle.load(open('detect.pkl','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
