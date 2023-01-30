{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "48bd8072",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "5\n",
      "9\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "#greatest of 3 numbers\n",
    "n1=int(input())\n",
    "n2=int(input())\n",
    "n3=int(input())\n",
    "if(n1>n2):\n",
    "    if(n1>n3):\n",
    "        print(n1)\n",
    "    else:\n",
    "        print(n3)\n",
    "elif(n2>n1):\n",
    "    if(n2>n3):\n",
    "        print(n2)\n",
    "    else:\n",
    "        print(n3)\n",
    "else:\n",
    "    print(n3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a703d0ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "5\n",
      "8\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "#greatest of 3 numbers\n",
    "n1=int(input())\n",
    "n2=int(input())\n",
    "n3=int(input())\n",
    "lrg=0\n",
    "if n1>n2 and n1>n3:\n",
    "    print(n1)\n",
    "elif n2>n1 and n2>n3:\n",
    "    print(n2)\n",
    "else:\n",
    "    print(n3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2c8e8ee5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "1 \n",
      "\n",
      "1 2 \n",
      "\n",
      "1 2 3 \n",
      "\n",
      "1 2 3 4 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "for i in range(1,n):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,end=\" \")\n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "58c73337",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "* \n",
      "\n",
      "* * \n",
      "\n",
      "* * * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "for i in range(1,n):\n",
    "    for j in range(1,i+1):\n",
    "        print(\"*\",end=\" \")\n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c0eb9879",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "120\n"
     ]
    }
   ],
   "source": [
    "#factorial\n",
    "n=int(input())\n",
    "s=1\n",
    "for i in range(1,n+1):\n",
    "    s=s*i\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e66354af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#fibonacci series\n",
    "n=int(input())\n",
    "n1=0\n",
    "n2=1\n",
    "print(n1)\n",
    "print(n2)\n",
    "for i in range(2,n+1):\n",
    "    s=n1+n2\n",
    "    print(s)\n",
    "    n1=n2\n",
    "    n2=s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0be7c055",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "not prime\n"
     ]
    }
   ],
   "source": [
    "#3)prime or not\n",
    "n=int(input())\n",
    "c=0\n",
    "for i in range(2,n):\n",
    "    if n%i==0:\n",
    "        c=c+1\n",
    "if(c==0):\n",
    "    print(\"prime\")\n",
    "else:\n",
    "    print(\"not prime\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a9106786",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('',), ('a', 'b'), ('a', 'b', 'c')]\n"
     ]
    }
   ],
   "source": [
    "#4)to remove an empty tuples from the list of tuples\n",
    "l=[(),(),('',),('a','b'),('a','b','c')]\n",
    "l=[t for t in l if t]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b9df8351",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.25\n"
     ]
    }
   ],
   "source": [
    "#5)to calculate the average of the elements in a list\n",
    "l=[2,4,6,1]\n",
    "s=0\n",
    "for i in l:\n",
    "    s=s+i\n",
    "a=s/len(l)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "677f1e86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['green', 'white', 'black']\n"
     ]
    }
   ],
   "source": [
    "#6)0,4,5 to print a specific list after removing \n",
    "l=['red','green','white','black','pink','yellow']\n",
    "l.remove(l[5])\n",
    "l.remove(l[4])\n",
    "l.remove(l[0])\n",
    "print(l)\n",
    "\n",
    "#l=[green,white,black]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2d87549c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['green', 'white', 'black', 'pink', 'yellow']\n"
     ]
    }
   ],
   "source": [
    "l=['red','green','white','black','pink','yellow']\n",
    "l.pop(0)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "29b4863c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]\n"
     ]
    }
   ],
   "source": [
    "#7)to generate all permutations of a list in python\n",
    "import itertools\n",
    "print(list(itertools.permutations([1,2,3])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cc6ec7af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36\n"
     ]
    }
   ],
   "source": [
    "#8)to calculate the product ,multiplying all the numbers of a given tuple\n",
    "t=(1,3,6,2)\n",
    "m=1\n",
    "for i in t:\n",
    "    m=m*i\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "f45ce4ea",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SAIVAR~1\\AppData\\Local\\Temp/ipykernel_14512/3134677018.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"abccdaa\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m     \u001b[1;32mfor\u001b[0m \u001b[0mj\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m         \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m==\u001b[0m\u001b[0mj\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m             \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "#9)counting repeating characters in a string\n",
    "str=\"abccdaa\"\n",
    "for i in str:\n",
    "    for j in range(i+1,len(str)):\n",
    "        if(i==j):\n",
    "            c=c+1\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "95e19f4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pujitha\n"
     ]
    }
   ],
   "source": [
    "#10)reverse a string if its length is a multiple of 4\n",
    "s=input()\n",
    "n=len(s)\n",
    "if n%4==0:\n",
    "    print(s[::-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07e8a0bc",
   "metadata": {},
   "source": [
    "# DAY-5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "596efc40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "puja\n",
      "42\n"
     ]
    }
   ],
   "source": [
    "class student:\n",
    "    name=\"puja\"\n",
    "    rollno=42\n",
    "    \n",
    "obj=student()\n",
    "print(obj.name)\n",
    "print(obj.rollno)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a3ce5f9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "puja\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'student' object has no attribute '__rollno'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SAIVAR~1\\AppData\\Local\\Temp/ipykernel_8608/1841094812.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mstudent\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__rollno\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'student' object has no attribute '__rollno'"
     ]
    }
   ],
   "source": [
    "#rollno as private variable\n",
    "class student:\n",
    "    name=\"puja\"\n",
    "    __rollno=42\n",
    "    \n",
    "obj=student()\n",
    "print(obj.name)\n",
    "print(obj.__rollno)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e1c58930",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "puja\n",
      "42\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "#getter and setter method to access private variables\n",
    "class student:\n",
    "    name=\"puja\"\n",
    "    __rollno=42\n",
    "    \n",
    "    def get_rollno(self):\n",
    "        return self.__rollno\n",
    "    def set_rollno(self,new_value):\n",
    "        self.__rollno=new_value\n",
    "    \n",
    "obj=student()\n",
    "print(obj.name)\n",
    "print(obj.get_rollno())\n",
    "print(obj.set_rollno(42))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c95a1a8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "enter name: pujitha\n",
      "enter password: 42\n",
      "enter name: preethi\n",
      "enter password: 39\n",
      "enter name: sony\n",
      "enter password: 51042\n",
      "{'pujitha': '42', 'preethi': '39', 'sony': '51042'}\n"
     ]
    }
   ],
   "source": [
    "#read names and pasword from user and sstore into dict and print them\n",
    "n=int(input())\n",
    "dic={}\n",
    "for i in range(n):\n",
    "    name=input(\"enter name: \")\n",
    "    password=input(\"enter password: \")\n",
    "    \n",
    "    dic[name]=password\n",
    "print(dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5fa8fed8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "enter name: puja\n",
      "enter password: 42\n",
      "enter name: sony\n",
      "enter password: 24\n",
      "[{'puja': '42'}, {'sony': '24'}]\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "arr=[]\n",
    "for i in range(n):\n",
    "    name=input(\"enter name: \")\n",
    "    password=input(\"enter password: \")\n",
    "    arr.append({name:password})\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a6b57f82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "enter name: a\n",
      "enter password: 123\n",
      "enter name: b\n",
      "enter password: 456\n",
      "enter name: c\n",
      "enter password: 789\n",
      "[{'a': '123'}, {'b': '456'}, {'c': '789'}]\n",
      "name: b\n",
      "password: 456\n",
      "valid password\n"
     ]
    }
   ],
   "source": [
    "# if user is in dic then validate there password\n",
    "n=int(input())\n",
    "arr=[]\n",
    "for i in range(n):\n",
    "    name=input(\"enter name: \")\n",
    "    password=input(\"enter password: \")\n",
    "    arr.append({name:password})\n",
    "print(arr)\n",
    "u1=input(\"name: \")\n",
    "p1=input(\"password: \")\n",
    "found=False\n",
    "for obj in arr:\n",
    "    try:\n",
    "        password=obj[u1]\n",
    "        found=True\n",
    "        if p1==password:\n",
    "            print(\"valid password\")\n",
    "        else:\n",
    "            print(\"invalid password\")\n",
    "    except:\n",
    "        pass\n",
    "if found==False:\n",
    "    print(\"user not found\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cce308ab",
   "metadata": {},
   "source": [
    "#STACKS"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d375e797",
   "metadata": {},
   "source": [
    "# STACK"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "15007112",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n",
      "[1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "stack=[]\n",
    "stack.append(1)\n",
    "stack.append(2)\n",
    "stack.append(3)\n",
    "stack.append(4)\n",
    "stack.append(5)\n",
    "print(stack)\n",
    "stack.pop()\n",
    "print(stack)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6df2e380",
   "metadata": {},
   "source": [
    "# QUEUE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9e61a89a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n",
      "[2, 3, 4, 5]\n",
      "[3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "queue=[]\n",
    "queue.append(1)\n",
    "queue.append(2)\n",
    "queue.append(3)\n",
    "queue.append(4)\n",
    "queue.append(5)\n",
    "print(queue)\n",
    "queue.pop(0)\n",
    "print(queue)\n",
    "queue.pop(0)\n",
    "print(queue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c5c9d8a",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
