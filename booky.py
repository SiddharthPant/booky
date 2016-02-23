import sys

level = 0
startChar = "{"
endChar = "}"
for line in sys.stdin:
	line = line.strip()
	if line == startChar:
		level = level + 1
	elif line == endChar:
		level = level - 1
	elif line:
		commaIndex = line.rfind(',')
		title = line[:commaIndex]
		pageNo = line[commaIndex + 1:].strip()
		print("BookmarkBegin")
		print("BookmarkTitle:", title.strip())
		print("BookmarkLevel:", level)
		print("BookmarkPageNumber:", pageNo.strip())
