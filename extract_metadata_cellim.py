import argparse
import os
import xmltodict

def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--czi_image',
                        type=str,
                        help='Image in czi format with metadata.')
    args = parser.parse_args()
    return args

def extract_metadata(czi_image):
    os.system(f"bftools/bfconvert {czi_image} tmp.ome")
    metadata_lines = []
    for line in open('tmp.ome', 'r', encoding='utf-8').readlines():
        metadata_lines.append(line)
        if line.strip() == "<LightPath></LightPath></Channel>":
            break
    metadata_lines.append("</Pixels></Image></OME>")
    metadata_string = "\n".join(metadata_lines)
    xml_dict = xmltodict.parse(metadata_string)
    os.system("rm tmp.ome")
    return xml_dict

def validate_metadata():
    pass

if __name__ == "__main__":
    args = load_arguments()
    metadata = extract_metadata(args.czi_image)







    # import bioformats
    # import javabridge
    # import html_to_json
    # import os
    # import time
    # args = load_arguments()
    # javabridge.start_vm(class_path=bioformats.JARS)
    # metadata_xml = bioformats.get_omexml_metadata(args.czi_image)
    # a = bioformats.OMEXML(metadata_xml)
    # print(dir(a.image()))
    #
    #
    # javabridge.kill_vm()


    # # metadata_dict = html_to_json.convert(metadata_xml)
    #
    # from json import loads
    # metadata_dict = loads(open("pokus.json").read())
    #
    # metadata = {"Name": metadata_dict["ome"][0]["image"][0]["_attributes"]["name"],
    #             "File Type": "Carl Zeiss Image (*.czi)",
    #             "File Path": os.path.abspath(args.czi_image),
    #             "File Size": f"{round(os.path.getsize(args.czi_image)/100000, 2)} MB",
    #             "Created": time.ctime(os.path.getctime(args.czi_image)),
    #             "Modified": time.ctime(os.path.getmtime(args.czi_image))}