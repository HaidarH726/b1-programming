{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "77fb41b0-e3fc-4e54-8950-fe3150279544",
   "metadata": {},
   "outputs": [],
   "source": [
    "# testing out python\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d800c349-0c1c-44ec-afd1-826d7efbf1ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Haidar is a new student in HTW \n"
     ]
    }
   ],
   "source": [
    "print(\" Haidar is a new student in HTW \" )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f0ec5238-246f-4287-b85d-3067e981109b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Haidar is 19 years old\n",
      "Haidar is True\n",
      "Haidar is a student in HTW berlin university\n"
     ]
    }
   ],
   "source": [
    "Name = 'Haidar'\n",
    "student_in = 'HTW'\n",
    "age = 19\n",
    "online = True\n",
    "offline = False\n",
    "\n",
    "print (Name, \"is\" ,(age), \"years old\" )\n",
    "\n",
    "print(f\"{Name} is {online}\")\n",
    "\n",
    "print(f\"{Name} is a student in {student_in} berlin university\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1b97b772-e220-4170-91c7-c2a8df566136",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Profit: $25000\n",
      "margin: %50.0\n",
      "markup: %100.0\n"
     ]
    }
   ],
   "source": [
    "revenue = 50000\n",
    "cost = 25000\n",
    "\n",
    "# calculate profit \n",
    "\n",
    "profit = revenue - cost\n",
    "margin = (profit / revenue) * 100\n",
    "markup = (profit / cost) * 100\n",
    "\n",
    "# Display results\n",
    "\n",
    "print(f\"Profit: ${profit}\")\n",
    "print(f\"margin: %{margin}\")\n",
    "print(f\"markup: %{markup}\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cdf0c9e-f5f1-4e7e-ac6a-a1844276d9b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
