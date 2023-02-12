import os
import sys
import json

from commons import CVE
from commons import CVE_FIELDS
from lxml import etree

productDirPath = ""

def parse(Vendor, Product, CVES):
    #Create Vendor directory
    vendorDirPath = os.path.join(os.getcwd(), Vendor)
    if not os.path.exists(vendorDirPath):
        os.makedirs(vendorDirPath)
    #Create Product directory in
    global productDirPath
    productDirPath = os.path.join(vendorDirPath, Product)
    if not os.path.exists(productDirPath):
        os.makedirs(productDirPath)
    
    # Launch formatters
    xmlOutput(Product, CVES[0])
    jsonOutput(Product, CVES[0])
    # Plain HTML in CVES[1]
    htmlOutput(Product, CVES[1])

###############
#    Utils    #
###############
def write(file_path, txt):
    with open(file_path, 'w+') as f:
        f.write(txt)

###############
#  XML Format #
###############
def getChildWithText(name, text):
    child = etree.Element(name)
    child.text = text
    return child

def getChild(name):
    return etree.Element(name)

def xmlOutput(Product, CVES):
    root = etree.Element("product")
    root.append(getChildWithText("name", Product))
    cveList = getChild("cve-list")
    for cve in CVES:
        #cve = (CVE, link_to_cve)
        cveNode = getChild("cve")
        cveNode.append(getChildWithText(CVE_FIELDS.CVE_ID.value, cve[0].CVE_ID))
        cveNode.append(getChildWithText(CVE_FIELDS.vType.value, cve[0].vType))
        cveNode.append(getChildWithText(CVE_FIELDS.pDate.value, cve[0].pDate))
        cveNode.append(getChildWithText(CVE_FIELDS.uDate.value, cve[0].uDate))
        cveNode.append(getChildWithText(CVE_FIELDS.score.value, cve[0].score))
        cveNode.append(getChildWithText(CVE_FIELDS.gainedAccessLevel.value, cve[0].gainedAccessLevel))
        cveNode.append(getChildWithText(CVE_FIELDS.access.value, cve[0].access))
        cveNode.append(getChildWithText(CVE_FIELDS.complexity.value, cve[0].complexity))
        cveNode.append(getChildWithText(CVE_FIELDS.authentication.value, cve[0].authentication))
        cveNode.append(getChildWithText(CVE_FIELDS.confidentiality.value, cve[0].confidentiality))
        cveNode.append(getChildWithText(CVE_FIELDS.integrity.value, cve[0].integrity))
        cveNode.append(getChildWithText(CVE_FIELDS.availability.value, cve[0].availability))
        cveNode.append(getChildWithText("link", cve[1]))
    
        cveList.append(cveNode)
    root.append(cveList)
    write(os.path.join(productDirPath, Product+".xml"), etree.tostring(root, encoding="unicode", pretty_print=True))

###############
# JSON Format #
###############
def jsonOutput(Product, CVES):
    root = {}
    product = {}
    CVEList = {}
    for cve in CVES:
        cveNode = {}
        #cve = (CVE, link_to_cve)
        cveNode[CVE_FIELDS.CVE_ID.value] = cve[0].CVE_ID
        cveNode[CVE_FIELDS.vType.value] = cve[0].vType
        cveNode[CVE_FIELDS.pDate.value] = cve[0].pDate
        cveNode[CVE_FIELDS.uDate.value] = cve[0].uDate
        cveNode[CVE_FIELDS.score.value] = cve[0].score
        cveNode[CVE_FIELDS.gainedAccessLevel.value] = cve[0].gainedAccessLevel
        cveNode[CVE_FIELDS.access.value] = cve[0].access
        cveNode[CVE_FIELDS.complexity.value] = cve[0].complexity
        cveNode[CVE_FIELDS.authentication.value] = cve[0].authentication
        cveNode[CVE_FIELDS.confidentiality.value] = cve[0].confidentiality
        cveNode[CVE_FIELDS.integrity.value] = cve[0].integrity
        cveNode[CVE_FIELDS.availability.value] = cve[0].availability
        cveNode["link"] = cve[1]
        CVEList[cve[0].CVE_ID] = cveNode
    product["name"] = Product
    root["product"] = product
    root["cve-list"] = CVEList
    write(os.path.join(productDirPath, Product+".json"), json.dumps(root, indent=4))

###############
# HTML Format #
###############
def htmlOutput(Product, page):
    write(os.path.join(productDirPath, Product+".html"), page)