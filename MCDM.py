#print "Enter the number of alternatives"
alternativeCount = int(raw_input())
#print "Enter the number of attributes"
attributeCount = int(raw_input())

Alternatives = [["" for x in range(attributeCount)] for x in range(alternativeCount)]

weights = []
for x in xrange(len(Alternatives[0])):
	#print "Enter the weights for the attributes"
	weights.append(float(raw_input()))

for i in range(len(Alternatives)):
	#print"Enter attribute values for alternative ",i + 1,":"
	for j in range(len(Alternatives[i])):
		#print"Attribute ",j,":"
		Alternatives[i][j] = int(raw_input())

print "Number of alternatives:", alternativeCount
print "Number of attributes:", attributeCount
print "Weights of every attribute are: "
for i in range(len(weights)):
	print weights[i]

print "All the alternatives with attribute specific scores are: "
for i in range(alternativeCount):
	print Alternatives[i]

scores = [0.0 for i in range(alternativeCount)]
for i in range(3):
	for j in range(4):
		scores[i] += Alternatives[i][j]**weights[j]
print "\n\n"
print "Acording to WPM, the scores of the alternatives are: "
for i in range(3):
	print scores[i]

print "\nThe best WPM alternative is alternative", scores.index(max(scores)) + 1
print "\n\n"

scores = [0.0 for i in range(3)]
for i in range(3):
	for j in range(4):
		scores[i] += Alternatives[i][j]*weights[j] 

print "Acording to SAW, the scores of the alternatives are: "
for i in range(3):
	print scores[i]

print "\nThe best SAW alternative is alternative", scores.index(max(scores)) + 1