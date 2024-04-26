a="Hello"
b="Hello"
c="Hello let's start"
d='Hello "world"'
e="""Hello
World
How 
are
you
"""
print(a,b,c,d,e,sep="\n")
print(a[3])

x="techno IT hub"
print("slicing", x[1:5])
print("slicing", x[1:])
print("slicing", x[:5])

print("Length:", len(x))

print("Uppercase", x.upper())
print("Is Uppercase", x.isupper())

print("Lowercase", x.lower())
print("Is Lowercase", x.islower())

y="Hello !!!!!!"
print("rstrip ", y.rstrip("!"))

print("Replace ", x.replace("IT", "it"))

print("Split", x.split( ))

print("Capitalize ", x.capitalize())

print("Center", x.center(50))

print("Count ", x.count("t"))

print("Endswith ",y.endswith("!"))

print("find ", x.find("Techno"))

p="Techno123"
q="Techno"

print("is alphanumeric x ",x.isalnum())
print("is alphanumeric p ",p.isalnum())
print("is alphanumeric q ",q.isalnum())

print("is alpha x ",x.isalpha())
print("is alpha p ",p.isalpha())
print("is alpha q ",q.isalpha())

w="Hello\n"
print("is printable x ",x.isprintable())
print("is printable w ",w.isprintable())

print("Space ", x.isspace())

print("is Title ", x.istitle())

print("Swapcase", x.swapcase())

print("title ", x.title())

print("startswith", x.startswith("t"))