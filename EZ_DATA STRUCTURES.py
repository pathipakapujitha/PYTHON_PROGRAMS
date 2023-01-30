{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f75ab080",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no of digits: 6\n",
      "digits are : 101111\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "#no of digits between 0\n",
    "size=int(input(\"no of digits: \"))\n",
    "max=0\n",
    "count=0\n",
    "flag=0\n",
    "str=input(\"digits are : \")\n",
    "arr=list(str)\n",
    "for i in range(0,size):\n",
    "    if arr[i]=='1':\n",
    "        count=count+1\n",
    "        flag=1\n",
    "    elif (arr[i]=='0' and flag==1):\n",
    "        count=0\n",
    "        flag=0\n",
    "    if count>max:\n",
    "        max=count\n",
    "print(max)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e3547112",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no of vehicles: 200\n",
      "no of wheels: 540\n",
      "4 wheel:  130\n",
      "2 wheel:  70\n"
     ]
    }
   ],
   "source": [
    "v=int(input(\"no of vehicles: \"))\n",
    "w=int(input(\"no of wheels: \"))\n",
    "if w&1==1 or w<2 or w<=v :\n",
    "    print(\"invalid\")\n",
    "else:\n",
    "    a=(4*v-w)//2\n",
    "t=v-a\n",
    "print(\"4 wheel: \",a)\n",
    "print(\"2 wheel: \",t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "81822a35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inorder traversaal of bst\n",
      "5\n",
      "10\n",
      "14\n",
      "15\n",
      "22\n",
      "24\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "class bt:\n",
    "    def __init__(self,data):\n",
    "        self.data=data\n",
    "        self.lc=None\n",
    "        self.rc=None\n",
    "def insert(root,newvalue):\n",
    "    if root is None:\n",
    "        root=bt(newvalue)\n",
    "        return root\n",
    "    if newvalue<root.data:\n",
    "        root.lc=insert(root.lc,newvalue)\n",
    "    else:\n",
    "        root.rc=insert(root.rc,newvalue)\n",
    "    return root\n",
    "def inorder(root):\n",
    "    if root==None:\n",
    "        return\n",
    "    inorder(root.lc)\n",
    "    print(root.data)\n",
    "    inorder(root.rc)\n",
    "root = insert(None,15)\n",
    "insert(root,10)\n",
    "insert(root,24)\n",
    "insert(root,5)\n",
    "insert(root,14)\n",
    "insert(root,22)\n",
    "insert(root,55)\n",
    "print(\"inorder traversaal of bst\")\n",
    "inorder(root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5048ea9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inorder traversaal of bst\n",
      "15\n",
      "10\n",
      "5\n",
      "14\n",
      "24\n",
      "22\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "#pre order\n",
    "class bt:\n",
    "    def __init__(self,data):\n",
    "        self.data=data\n",
    "        self.lc=None\n",
    "        self.rc=None\n",
    "def insert(root,newvalue):\n",
    "    if root is None:\n",
    "        root=bt(newvalue)\n",
    "        return root\n",
    "    if newvalue<root.data:\n",
    "        root.lc=insert(root.lc,newvalue)\n",
    "    else:\n",
    "        root.rc=insert(root.rc,newvalue)\n",
    "    return root\n",
    "def inorder(root):\n",
    "    if root==None:\n",
    "        return\n",
    "    print(root.data)\n",
    "    inorder(root.lc)\n",
    "    inorder(root.rc)\n",
    "root = insert(None,15)\n",
    "insert(root,10)\n",
    "insert(root,24)\n",
    "insert(root,5)\n",
    "insert(root,14)\n",
    "insert(root,22)\n",
    "insert(root,55)\n",
    "print(\"inorder traversaal of bst\")\n",
    "inorder(root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d31ee53c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inorder traversaal of bst\n",
      "5\n",
      "14\n",
      "10\n",
      "22\n",
      "55\n",
      "24\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "#post order\n",
    "class bt:\n",
    "    def __init__(self,data):\n",
    "        self.data=data\n",
    "        self.lc=None\n",
    "        self.rc=None\n",
    "def insert(root,newvalue):\n",
    "    if root is None:\n",
    "        root=bt(newvalue)\n",
    "        return root\n",
    "    if newvalue<root.data:\n",
    "        root.lc=insert(root.lc,newvalue)\n",
    "    else:\n",
    "        root.rc=insert(root.rc,newvalue)\n",
    "    return root\n",
    "def inorder(root):\n",
    "    if root==None:\n",
    "        return\n",
    "    inorder(root.lc)\n",
    "    inorder(root.rc)\n",
    "    print(root.data)\n",
    "root = insert(None,15)\n",
    "insert(root,10)\n",
    "insert(root,24)\n",
    "insert(root,5)\n",
    "insert(root,14)\n",
    "insert(root,22)\n",
    "insert(root,55)\n",
    "print(\"inorder traversaal of bst\")\n",
    "inorder(root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "32e624ce",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Node' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SAIVAR~1\\AppData\\Local\\Temp/ipykernel_2892/4192094034.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# verticle order traversal\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mclass\u001b[0m \u001b[0mNode\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mNode\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mNode\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\SAIVAR~1\\AppData\\Local\\Temp/ipykernel_2892/4192094034.py\u001b[0m in \u001b[0;36mNode\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# verticle order traversal\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mNode\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mNode\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mNode\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Node' is not defined"
     ]
    }
   ],
   "source": [
    "# verticle order traversal\n",
    "class Node:\n",
    "    def __init__(self,key,l=Node,r=Node):\n",
    "        self.key=key\n",
    "        self.l=l\n",
    "        self.r=r\n",
    "def vot(node,dist,d):\n",
    "    if node is Node:\n",
    "        return\n",
    "    d.setdefault(dist,[].append(node.key))\n",
    "    \n",
    "if __name__=='__main__':\n",
    "    root=Node(1)\n",
    "    root.l=Node(2)\n",
    "    root.r=Node(3)\n",
    "    root.r.l=Node(4)\n",
    "    root.r.r=Node(5)\n",
    "    root.r.l.l=Node(6)\n",
    "    root.r.l.r=Node(7)\n",
    "    root.r.l.r.l=Node(8)\n",
    "    root.r.l.r.r=Node(9)\n",
    "    pvot(root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "aa5e3ba6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "22 9 4 7 8\n",
      "[22, 4, 8, 9, 7]\n"
     ]
    }
   ],
   "source": [
    "# print all even numbers first and odd numbers next\n",
    "n=int(input())\n",
    "l=list(map(int,input().strip().split()))\n",
    "l1=[]\n",
    "l2=[]\n",
    "for i in l:\n",
    "    if i%2==0:\n",
    "        l1.append(i)\n",
    "    else:\n",
    "        l2.append(i)\n",
    "l1=l1+l2\n",
    "print(l1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b0f71eda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'abc', 'age': '100', 'branch': 'aeronautical'}\n"
     ]
    }
   ],
   "source": [
    "keys=['name','age','branch']\n",
    "values=['abc','100','aeronautical']\n",
    "outsource=dict(zip(keys, values))\n",
    "#abc=dict(outsource)\n",
    "print(outsource)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a47ec0b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{(0, 3): 1, (1, 0): 2, (1, 4): 3, (2, 3): 4}\n"
     ]
    }
   ],
   "source": [
    "#write a program to store a sparse matrix in to a dictonary\n",
    "array     = [[0,0,0,1,0],\n",
    "            [2,0,0,0,3],\n",
    "            [0,0,0,4,0]]\n",
    "dic={}\n",
    "for i in range(len(array)):\n",
    "    for j in range(len(array[i])):\n",
    "        if array[i][j]!=0:\n",
    "            dic[i,j]=array[i][j]\n",
    "print(dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3479afba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "level\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "l=list(map(str,input().strip().split()))\n",
    "l1=[]\n",
    "for i in range(0,len(l)):\n",
    "    for j in range(1,len(l)):\n",
    "        if l[i]!=l[j]:\n",
    "            l1.append(l[i])\n",
    "print(l1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "1bec6dd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "level\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "l=list(map(str,input().strip().split()))\n",
    "l1=[]\n",
    "l2=[]\n",
    "for i in range(0,len(l)):\n",
    "    l1.append(l[i])\n",
    "    for j in range(1,len(l)):\n",
    "        if l[j]!=l1[i]:\n",
    "            l2.append(l[j])\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ad477547",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the  on repeaatinf char is v\n"
     ]
    }
   ],
   "source": [
    "str='level'\n",
    "for i in str:\n",
    "    c=0\n",
    "    for j in str:\n",
    "        if i==j:\n",
    "            c+=1\n",
    "        if c>1:\n",
    "            break\n",
    "    if c==1:\n",
    "        print(\"the  on repeaatinf char is\",i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2fc681ec",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_9500/1237670871.py, line 34)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\SAIVAR~1\\AppData\\Local\\Temp/ipykernel_9500/1237670871.py\"\u001b[1;36m, line \u001b[1;32m34\u001b[0m\n\u001b[1;33m    if __name__=='__main__'\u001b[0m\n\u001b[1;37m                           ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#write a program to insert delete a node in a single linked list 1,3,5,8\n",
    "class node:\n",
    "    def __init__(self,num):\n",
    "        self.num=num\n",
    "        self.next=node\n",
    "class llist:\n",
    "    def __init__(self):\n",
    "        self.head=node\n",
    "    def push(self,newnum):\n",
    "        newnode=node(newnum)\n",
    "        newnode.next=self.head\n",
    "        self.head=newnode\n",
    "    def insertnext(self,prenode,newnode):\n",
    "        if prenode is None:\n",
    "            print(\"the previous node\")\n",
    "            return\n",
    "        newnode=node(newnum)\n",
    "        newnode.next=prenode.next\n",
    "        prenode.next=newnode\n",
    "    def append(self,newnum):\n",
    "        newnode=node(newnum)\n",
    "        if self.head is None:\n",
    "            self.head=newnode\n",
    "            return\n",
    "        last=self.head\n",
    "        while(last.next):\n",
    "            last=last.next\n",
    "        last.next=newnode\n",
    "    def printnum(self):\n",
    "        t=self.head\n",
    "        while(t):\n",
    "            print(t.data)\n",
    "            t=temp.next\n",
    "if __name__=='__main__'\n",
    "ll=llist()\n",
    "ll.append(1)\n",
    "ll.append(3)\n",
    "ll.append(5)\n",
    "ll.append(8)\n",
    "print(printnum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8315d688",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no\n"
     ]
    }
   ],
   "source": [
    "s1=\"klmn\"\n",
    "s2=\"lmnk\"\n",
    "c=0\n",
    "for i in s1:\n",
    "    for j in s2:\n",
    "        if i in s2:\n",
    "            c+=1\n",
    "            break\n",
    "        else:\n",
    "            c=0\n",
    "if c==1:\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"no\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c2bbb18b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pqr\n",
      "pqrst\n",
      "no\n"
     ]
    }
   ],
   "source": [
    "s1=input()\n",
    "s2=input()\n",
    "if(sorted(s1)==sorted(s2)):\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"no\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2285075",
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
