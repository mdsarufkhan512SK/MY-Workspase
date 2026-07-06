#67 Python Regular Expression

##Metacharacters


import re

#[]	A set of characters

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department"

Condition = re.findall("[a-zA-z]",Saruf)

print(Condition)


#\	Signals a special sequence (can also be used to escape special characters)
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("\d",Saruf)

print(Condition)



#$	Ends with
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("227603$",Saruf)

if Condition:
    print("Yes,This is a special number")
else:
    print("Not Match")


#.	Any character (except newline character)
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("Sa..f",Saruf)

print(Condition)


#^	Starts with
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("^Saruf",Saruf)

if Condition:
    print("Yes, the string starts with 'Saruf'")
else:
    print("Not Match")


#*	Zero or more occurrences
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("Sa.*f",Saruf)

print(Condition)


#+	One or more occurrences
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("Sa.+f",Saruf)

print(Condition)

#{}	Exactly the specified number of occurrences
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("Sa.{2}f",Saruf)

print(Condition)

#?	Zero or one occurrences
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("Sa.?f",Saruf)

print(Condition)





####Special Sequences


#\A	Returns a match if the specified characters are at the beginning of the string

# Work: পুরো টেক্সট বা স্ট্রিংয়ের একদম শুরুতে নির্দিষ্ট কোনো শব্দ বা অক্ষর আছে কিনা তা চেক করে।

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall("\ASaruf",Saruf)

if Condition:
    print("Yes, the string starts with 'Saruf'")
else:
    print("Not Match")


#\b	Returns a match where the specified characters are at the beginning or at the end of a word
#(the "r" in the beginning is making sure that the string is being treated as a "raw string")

#Work:r"\bain" দিলে এমন শব্দ খুঁজবে যার শুরুতে "ain" আছে।


Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"\bKhu",Saruf)

if Condition:
    print("Yes,This is a special number, 'Khulna'")
else:
    print("Not Match")



#Work:r"ain\b" দিলে এমন শব্দ খুঁজবে যার শেষে "ain" আছে (যেমন: rain, train)।
Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"ruf\b",Saruf)

if Condition:
    print("Yes,This is a special number, 'Saruf'")
else:
    print("Not Match")


#\d	Returns a match where the string contains digits (numbers from 0-9

#কাজ: যেকোনো সংখ্যা বা ডিজিট (0 থেকে 9) খুঁজে বের করে।

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"\d",Saruf)

if Condition:
    print("Yes,This is a special number, 227603 ")
else:
    print("Not Match")


#\D (সংখ্যা ছাড়া অন্য কিছু)
#কাজ: এটি \d এর উল্টো। টেক্সটের ভেতরের সংখ্যা (0-9) ছাড়া বাকি যা কিছু আছে (অক্ষর, স্পেস, সিম্বল) সবকিছু ম্যাচ করে।

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"\D",Saruf)

print(Condition)
if Condition:
    print("Yes,there is at least one match!, ")
else:
    print("Not Match")


#৬. \s (হোয়াইট স্পেস)
#কাজ: টেক্সটের ভেতরের যেকোনো খালি জায়গা বা স্পেস (White space, Tab, Newline) খুঁজে বের করে।

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"\s",Saruf)

if Condition:
    print("Yes,there is at least one match!, ")
else:
    print("Not Match")


#৭. \S (স্পেস ছাড়া অন্য কিছু)
#কাজ: এটি \s এর উল্টো। টেক্সটের ভেতরের স্পেস বা খালি জায়গা ছাড়া বাকি সব অক্ষর বা সংখ্যা ম্যাচ করে।

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"\S",Saruf)

print(Condition)
if Condition:
    print("Yes,there is at least one match!, ")
else:
    print("Not Match")


#৮. \w (অক্ষর, সংখ্যা এবং আন্ডারস্কোর)
#কাজ: যেকোনো Word Character খুঁজে বের করে। এর মধ্যে রয়েছে ছোট-বড় সব অক্ষর (a-z, A-Z), যেকোনো সংখ্যা (0-9) এবং আন্ডারস্কোর (_) চিহ্ন।

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"\w",Saruf)

print(Condition)
if Condition:
    print("Yes,there is at least one match!, ")
else:
    print("Not Match")


#৯. \W (স্পেশাল ক্যারেক্টার ও স্পেস)
#কাজ: এটি \w এর উল্টো। অক্ষর, সংখ্যা বা আন্ডারস্কোর ছাড়া বাকি যা আছে—যেমন স্পেস ( ), বিরামচিহ্ন (,, .,

Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"\W",Saruf)

print(Condition)
if Condition:
    print("Yes,there is at least one match!, ")
else:
    print("Not Match")


#১০. \Z (শেষ ম্যাচ করা)
#কাজ: পুরো টেক্সট বা স্ট্রিংয়ের একদম শেষে নির্দিষ্ট কোনো শব্দ বা অক্ষর আছে কিনা তা চেক করে।

#উদাহরণ: r"Spain\Z" দিলে পুরো স্ট্রিংয়ের একদম শেষ শব্দটি "Spain" হলে সেটি ম্যাচ কর


Saruf = "Saruf is a students at Khulna Polytechnic Institute in C.S.T department,Class Roll 227603"

Condition = re.findall(r"22603\Z",Saruf)

print(Condition)
if Condition:
    print("Yes, there is a match!, ")
else:
    print("Not Match")

