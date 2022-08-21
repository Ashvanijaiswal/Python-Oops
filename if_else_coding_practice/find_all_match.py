import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""
print(re.sub(r'<!--.*?-->',"",html))

a=[('ashvani',23,4.5),('siddiq',24,5.5),('sandesh',23,5)]
print(list(zip(*a)))
