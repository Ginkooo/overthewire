from natas import Natas

natas = Natas('natas16')

post = {'needle': '$()'}

response = natas.get_response(post_data=post)
print(response.prettify())
