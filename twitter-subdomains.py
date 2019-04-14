#!/usr/bin/env python # Assume 2
# api-23-0-0.twitter.com
file = "/tmp/subdomains.txt"
unique = False

domain = "twitter.com"
subdomains = []

startI, endI = 0, 51
startJ, endJ = 0, 51
startK, endK = 0, 51

for i in range(startI, endI):
    string = "api-" + str(i) + "-0-0"
    subdomains.append('.'.join([string, domain]))
    for j in range(startJ, endJ):
        string = "api-" + str(i) + "-" + str(j) + "-0"
        subdomains.append('.'.join([string, domain]))
        for k in range(startK, endK):
            string = "api-" + str(i) + "-" + str(j) + "-" + str(k)
            subdomains.append('.'.join([string, domain]))


# Remove Duplicates (Or let Pi-hole do it)
if unique == True:
    subdomains = list(set(subdomains))

# Write the subdomains to the specified file
with open(file, 'w') as file_handler:
    for item in subdomains:
        file_handler.write("{}\n".format(item))
