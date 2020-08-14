import requests


#false is get request,true is post request
def _makerequest(url,type,post_fields='',timeout=10):
	if type :
		response = requests.post(url, data=post_fields, timeout=timeout)
	else :
		response = requests.get(url,timeout=timeout)
	print(response)
	return response.elapsed.total_seconds()


def main():
	print(_makerequest('https://www.google.com/',False))


if __name__ == '__main__':
	main()