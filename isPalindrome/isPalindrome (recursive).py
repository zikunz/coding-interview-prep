{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf840
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Time Complexity: O(N), where N represents number of characters in string\
# Space Complexity: O(N) (adding frames to the call stack due to recursive calls uses extra memory)\
\
def isPalindrome(string):\
	return isPalindromeHelper(string, 0, len(string) - 1)\
	\
def isPalindromeHelper(array, leftPtr, rightPtr):\
	if leftPtr >= rightPtr:\
		return True\
	\
	if array[leftPtr] != array[rightPtr]:\
		return False\
		\
	return isPalindromeHelper(array, leftPtr + 1, rightPtr - 1)	}