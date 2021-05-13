{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "80fe1554-3f82-4aac-9b5f-596a52bbd680",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "def get_predictions(carat_weight, cut, color, clarity, polish, symmetry, report):\n",
    "    url = 'http://localhost:8000/predict?carat_weight={carat_weight}&cut={cut}&color={color}&clarity={clarity}&polish={polish}&symmetry={symmetry}&report={report}'\\\n",
    "    .format(carat_weight = carat_weight, cut = cut,\\\n",
    "     color = color, clarity = clarity, polish = polish, symmetry = symmetry, report = report)\n",
    "    \n",
    "    x = requests.post(url)\n",
    "    print(x.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "641ce5f8-f613-443a-b112-6c0c5afb7e4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"prediction\":23198}\n"
     ]
    }
   ],
   "source": [
    "get_predictions(2.2, \"Ideal\", \"E\", \"SI1\", \"VG\", \"ID\", \"GIA\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48233492-121a-4e9c-9e50-131a7ac3d078",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
