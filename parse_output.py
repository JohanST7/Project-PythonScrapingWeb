import os
import sys

from commons import CVE
from commons import CVE_FIELDS
from lxml import etree

productDirPath = ""

def write(file_path, txt):
    with open(file_path, 'w+') as f:
        f.write(txt)

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
    
    xmlOutput(Product, CVES)

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


CVEs = []
CVEs.append(CVE("0", "Overflow", "2019-02-08", "2021-11-30", "6.8", "None", "remote", "Medium", "Not required", "Partial", "Partial", "Partial"))
CVEs.append(CVE("1", "Overflow", "2019-02-08", "2021-11-30", "6.8", "None", "remote", "Medium", "Not required", "Partial", "Partial", "Partial"))
CVEs.append(CVE("2", "Overflow", "2019-02-08", "2021-11-30", "6.8", "None", "remote", "Medium", "Not required", "Partial", "Partial", "Partial"))
parse("Microsoft","Windows",CVEs)