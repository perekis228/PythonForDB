from lxml import etree
def validate_xml(xml_file, xsd_file):
    with open(xsd_file, 'rb') as schema_file:
        schema_root = etree.XML(schema_file.read())
        schema = etree.XMLSchema(schema_root)
    with open(xml_file, 'rb') as xml_file:
        xml_doc = etree.parse(xml_file)
    if schema.validate(xml_doc):
        print("XML документ валиден.")
    else:
        print("XML документ не валиден.")
        for error in schema.error_log:
            print(error.message)

validate_xml('ex_1.xml', 'ex_1_xsd.xsd')
validate_xml('ex_1_err.xml', 'ex_1_xsd.xsd')