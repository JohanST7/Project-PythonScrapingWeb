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
    xmlOutput(Product, CVES)
    jsonOutput(Product, CVES)

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
        cveNode = getChild("cve")
        cveNode.append(getChildWithText(CVE_FIELDS.CVE_ID.value, cve.CVE_ID))
        cveNode.append(getChildWithText(CVE_FIELDS.vType.value, cve.vType))
        cveNode.append(getChildWithText(CVE_FIELDS.pDate.value, cve.pDate))
        cveNode.append(getChildWithText(CVE_FIELDS.uDate.value, cve.uDate))
        cveNode.append(getChildWithText(CVE_FIELDS.score.value, cve.score))
        cveNode.append(getChildWithText(CVE_FIELDS.gainedAccessLevel.value, cve.gainedAccessLevel))
        cveNode.append(getChildWithText(CVE_FIELDS.access.value, cve.access))
        cveNode.append(getChildWithText(CVE_FIELDS.complexity.value, cve.complexity))
        cveNode.append(getChildWithText(CVE_FIELDS.authentication.value, cve.authentication))
        cveNode.append(getChildWithText(CVE_FIELDS.confidentiality.value, cve.confidentiality))
        cveNode.append(getChildWithText(CVE_FIELDS.integrity.value, cve.integrity))
        cveNode.append(getChildWithText(CVE_FIELDS.availability.value, cve.availability))
        
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
        cveNode[CVE_FIELDS.CVE_ID.value] = cve.CVE_ID
        cveNode[CVE_FIELDS.vType.value] = cve.vType
        cveNode[CVE_FIELDS.pDate.value] = cve.pDate
        cveNode[CVE_FIELDS.uDate.value] = cve.uDate
        cveNode[CVE_FIELDS.score.value] = cve.score
        cveNode[CVE_FIELDS.gainedAccessLevel.value] = cve.gainedAccessLevel
        cveNode[CVE_FIELDS.access.value] = cve.access
        cveNode[CVE_FIELDS.complexity.value] = cve.complexity
        cveNode[CVE_FIELDS.authentication.value] = cve.authentication
        cveNode[CVE_FIELDS.confidentiality.value] = cve.confidentiality
        cveNode[CVE_FIELDS.integrity.value] = cve.integrity
        cveNode[CVE_FIELDS.availability.value] = cve.availability
        CVEList[cve.CVE_ID] = cveNode
    product["name"] = Product
    root["product"] = product
    root["cve-list"] = CVEList
    write(os.path.join(productDirPath, Product+".json"), json.dumps(root, indent=4))
