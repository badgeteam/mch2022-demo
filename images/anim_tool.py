
import math, os
from PIL import Image

nFrames = 28
def getPath(frameno):
	frameno += 1
	if frameno < 10:
		return "./anim_intro/0{f}.png".format(f=frameno)
	else:
		return "./anim_intro/{f}.png".format(f=frameno)

def matrixOf(image):
	"""
	Creates a matrix of the image.
	"""
	image = image.convert("RGB")
	out = []
	raw = list(image.getdata())
	for y in range(image.height):
		out.append([])
		for x in range(image.width):
			out[y].append(raw[x+y*image.width])
	return out

def diffMatrix(mtx1, mtx2):
	"""
	Creates a matrix indicating which pixels differ between mtx1 and mtx2.
	"""
	out = []
	h = len(mtx1)
	w = len(mtx1[0])
	h2 = len(mtx2)
	w2 = len(mtx2[0])
	if w != w2 or h != h2:
		raise ValueError("mtx1 size must match mtx2 size!")
	for y in range(h):
		out.append([])
		for x in range(w):
			isDiff = mtx1[y][x] != mtx2[y][x]
			out[y].append(isDiff)
	return out

def diffMatrixToImage(mtx):
	height = len(mtx)
	width  = len(mtx[0])
	img = Image.new("RGB", (width, height))
	for y in range(height):
		for x in range(width):
			val = (255,255,255) if mtx[y][x] else (0,0,0)
			img.putpixel((x, y), val)
	return img

class Rect:
	def __init__(self, x, y, w, h):
		self.x      = x
		self.y      = y
		self.width  = w
		self.height = h
		self.area   = abs(w * h)
	def __str__(self):
		return "<Rect {w}x{h} @ {x},{y} (a={a})>".format(x=self.x, y=self.y, w=self.width, h=self.height, a=self.area)
	def __repr__(self):
		return "Rect({x}, {y}, {w}, {h})".format(x=self.x, y=self.y, w=self.width, h=self.height)
	
	def neighbours(self, x, y, lenience=1):
		"""
		Returns whether the given point lies around the rectangle with an optional lenience.
		"""
		return x+lenience >= self.x and x-lenience <= self.x + self.width - 1 and y+lenience >= self.y and y-lenience <= self.y + self.height - 1
	def contains(self, x, y):
		"""
		Returns whether the given point lies inside the rectangle.
		"""
		return self.neighbours(x, y, 0)
	
	def withPoint(self, x, y):
		"""
		Creates a new rect that includes the given point.
		"""
		newX = self.x
		newY = self.y
		newW = self.width
		newH = self.height
		if x < self.x:
			newX = x
			newW += self.x - x
		elif x > self.x + self.width - 1:
			newW = x - self.x + 1
		if y < self.y:
			newY = y
			newH += self.y - y
		elif y > self.y + self.height - 1:
			newH = y - self.y + 1
		return Rect(newX, newY, newW, newH)
	
	def splitArea(self, max_area):
		"""
		Creates a few rectangles that are split into areas of approximately max_area.
		"""
		segments = math.ceil(self.area / max_area)
		out = []
		if self.width > self.height:
			# Divide by width.
			x = self.x
			w = self.width
			delta = math.ceil(self.width / segments)
			for i in range(segments):
				out.append(Rect(x, self.y, min(delta, w), self.height))
				x += delta
				w -= delta
		else:
			# Divide by height.
			y = self.y
			h = self.height
			delta = math.ceil(self.height / segments)
			for i in range(segments):
				out.append(Rect(self.x, y, self.width, min(delta, h)))
				y += delta
				h -= delta
		return out

def isPointIn(rects, x, y, lenience=3):
	"""
	Checks whether the point lies in one of the rects, and if so returns which one.
	"""
	for rect in rects:
		if rect.neighbours(x, y, lenience):
			return rect
	return None

def diffRects(mtx, lenience=3):
	"""
	Converts a difference matrix into a set of difference rectangles.
	"""
	rects = []
	for y in range(len(mtx)):
		row = mtx[y]
		for x in range(len(row)):
			if not row[x]:
				continue
			rect = isPointIn(rects, x, y, lenience)
			if rect:
				rects[rects.index(rect)] = rect.withPoint(x, y)
			else:
				rects.append(Rect(x, y, 1, 1))
	return rects

# def cropImage(img : Image.Image, rect : Rect):
# 	"""
# 	I have your Image.crop().
# 	"""
# 	out = Image.new(img.mode, (rect.width, rect.height))
# 	for y in range(rect.height):
# 		for x in range(rect.width):
# 			out.putpixel((x, y), img.getpixel((x+rect.x, y+rect.y)))
# 	return out

def diffImages(img0, img1, max_area=10000):
	"""
	Creates a list of difference images between img0 and img1.
	"""
	# Create a difference map.
	mtx0 = matrixOf(img0)
	mtx1 = matrixOf(img1)
	diff = diffRects(diffMatrix(mtx0, mtx1))
	# Split rects that are too big.
	rects = []
	for rect in diff:
		rects.extend(rect.splitArea(max_area))
	# Create images of these rects.
	out = []
	for rect in rects:
		bounds = (rect.x, rect.y, rect.x + rect.width, rect.y + rect.height)
		out.append((rect.x, rect.y, img1.crop(bounds)))
		# out.append((rect.x, rect.y, cropImage(img1, rect)))
	return out

def combineDiff(images, width, height):
	"""
	Combines a list of difference images into an ARGB image.
	"""
	img = Image.new("RGBA", (width, height))
	# Fill the image with EMPTY SPACE.
	for y in range(height):
		for x in range(width):
			img.putpixel((x, y), (0, 0, 0, 0))
	# Overlay ALL the OTHER piXelS.
	for set in images:
		overlay: Image = set[2].convert("RGBA")
		dX             = set[0]
		dY             = set[1]
		for y in range(overlay.height):
			for x in range(overlay.width):
				img.putpixel((x + dX, y + dY), overlay.getpixel((x, y)))
	return img

def saveDiffs(diffs, width, height, path, prefix="anim", includefile=None):
	"""
	Outputs some C files for your enjoyment.
	Expects path to be a complete .c file path.
	The prefix will be used for all generated variables.
	"""
	# Open the output C file.
	file = open(path, "w")
	file.write("// WARNING: This is a generated file, do not edit it!\n")
	file.write("// Animation is {w}x{h}, {n} frame{s}.\n".format(w=width, h=height, n=len(diffs), s="s" if len(diffs) != 1 else ""))
	if includefile:
		file.write("#include \"{incl}\"\n".format(incl=includefile))
	file.write("#include <stdint.h>\n")
	file.write("#include <stddef.h>\n\n")
	# Write individual image data.
	for frame in range(len(diffs)):
		images = diffs[frame]
		print("Encoding {frame}/{of}...".format(frame=frame+1, of=len(diffs)))
		for num in range(len(images)):
			# Save the image to a temp file.
			path    = "/tmp/anim_tool_work.png"
			images[num][2].save(path)
			# Then read it right back in.
			tmpfile = open(path, "rb")
			tmpdata = tmpfile.read()
			tmpfile.close()
			# Finally append it as a C array.
			file.write("const char {prefix}_{frame}_{num}[] = {{\n".format(prefix=prefix, frame=frame, num=num))
			for byte in tmpdata:
				file.write("{hex},".format(hex=hex(byte)))
			file.write("\n}};\nconst size_t {prefix}_{frame}_{num}_len = sizeof({prefix}_{frame}_{num}) / sizeof(char);\n\n".format(prefix=prefix, frame=frame, num=num))
		
		# Now describe all parts of the frame.
		file.write("const {prefix}_part_t {prefix}_{frame}_parts[] = {{\n".format(prefix=prefix, frame=frame))
		for num in range(len(images)):
			file.write("\t{prefix}_def_part({x}, {y}, {prefix}_{frame}_{num}, {prefix}_{frame}_{num}_len),\n".format(x=images[num][0], y=images[num][1], prefix=prefix, frame=frame, num=num))
		file.write("}};\nconst size_t {prefix}_{frame}_parts_len = sizeof({prefix}_{frame}_parts) / sizeof({prefix}_part_t);\n\n".format(prefix=prefix, frame=frame))
	
	# Write a meta-array.
	file.write("const {prefix}_frame_t {prefix}_frames[] = {{\n".format(prefix=prefix))
	for frame in range(len(diffs)):
		file.write("\t{prefix}_def_frame({prefix}_{frame}_parts, {prefix}_{frame}_parts_len),\n".format(prefix=prefix, frame=frame))
	file.write("}};\nconst size_t {prefix}_frames_len = sizeof({prefix}_frames) / sizeof({prefix}_frame_t);\n".format(prefix=prefix))
	file.close()
	print("Done!")

def test0():
	img0 = Image.open(getPath(0))
	img1 = Image.open(getPath(1))
	diff = diffImages(img0, img1)
	print(diff)
	out  = combineDiff(diff, 320, 240)
	out.save("/home/julian/Pictures/out.png")
	print("Saved to:")
	print("/home/julian/Pictures/out.png")

def test1():
	img0 = Image.open(getPath(0))
	img1 = Image.open(getPath(1))
	diffmtx = diffMatrix(matrixOf(img0), matrixOf(img1))
	rects = diffRects(diffmtx)
	diff = diffImages(img0, img1)
	out  = combineDiff(diff, 320, 240)
	return diffmtx, rects, diff, out

def test2():
	img0 = Image.open(getPath(0))
	img1 = Image.open(getPath(1))
	diff = diffMatrix(matrixOf(img0), matrixOf(img1))
	out  = diffMatrixToImage(diff)
	out.save("/home/julian/Pictures/diff.png")
	print("Saved to:")
	print("/home/julian/Pictures/diff.png")

def performEncoding():
	# Initial background color.
	bg_col = (191, 241, 241)
	# Initial frame.
	print("Processing {frame}/{of}...".format(frame=1, of=nFrames))
	initial = Image.new("RGB", (320, 240), bg_col)
	frame01 = Image.open(getPath(0))
	diffList = [ diffImages(initial, frame01) ]
	# Remaining frames.
	for i in range(nFrames-1):
		print("Processing {frame}/{of}...".format(frame=i+2, of=nFrames))
		img0 = Image.open(getPath(i))
		img1 = Image.open(getPath(i + 1))
		diffList.append(diffImages(img0, img1))
	# Package it up.
	saveDiffs(diffList, 320, 240, "anim_intro.c", "td_anim", "td_anim.h")

if __name__ == "__main__":
	performEncoding()
