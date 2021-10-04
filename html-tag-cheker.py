HTML_TAGS = {"</html>": "<html>", "</head>": "<head>", "</title>": "<title>", "</body>": "<body>", "</div>": "<div>",
             "</span>": "<span>", "</table>": "<table>", "</thead>": "<thead>", "</tr>": "<tr>", "</td>": "<td>",
             "</script>": "<script>", "</ul>": "<ul>", "</strong>": "<strong>"}#i try to use keys as closing tag and values an an openining tags
list = []
#my_file = open('TSEGANESH YIFRU.html', 'r')#u can insert the file that u want to check
MY_FILE = my_file.read().split()#i try to split into an arrays
for tag in MY_FILE:
    #i try to check wether it is in my value or in my key if it is in my value it appends to my empty list and if it is in key and its is the same as the cheked tag  i poped up
    if tag in HTML_TAGS.values():
        list.append(tag)
    elif tag in HTML_TAGS.keys():
        if HTML_TAGS[tag] == list[-1] or list[-1] == '<br>' or (
                list[-1].startswith('<img') and list[-1].endswith('/>')) or (
                list[-1].startswith('<title>') and list[-1].endswith('/title')) or (
                list[-1].startswith('<h>') and list[-1].endswith('</h>')) or (
                list[-1].startswith('<a') and list[-1].endswith('</a>')) or (
                list[-1].startswith('<td>') and list[-1].endswith('</td>')) or (
                list[-1].startswith('<tr>') and list[-1].endswith('</tr>')) or (
                list[-1].startswith('<li>') or (list[-1].startswith('<li>') and list[-1].endswith('</li>'))) or (
                list[-1].startswith('<strong>') and list[-1].endswith('</strong>')):
            list.pop(-1)
if len(list) == 0:#finally when my list is empty then it is valid
    print("YOUR HTML FILE IS VALID")
elif len(list) != 0:
    print(list)
    print('PLEASE CHECK YOUR FILE,IT IS INVALID')
