from urllib import request


goog_url = "file:///C:/Users/Acer/Desktop/amazon.pdf"


def download_data_web(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("//n")
    dest = r'shanto.pdf'
    fx = open(dest, "w")
    for line in lines:
        fx.write(line + "/n")
    fx.close()

download_data_web(goog_url)