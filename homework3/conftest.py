# from client import ApiClient
#
#
# class UniqId:
#
#     site_id = None
#
#     def get_id(self):
#         url = "https://target.my.com/api/v1/urls/"
#         headers = {
#             'X-CSRFToken': f'{ApiClient.csrftoken}',
#         }
#         params = {
#             "url": "https://www.google.com/"
#         }
#         site_id = ApiClient.session.get(url, headers=headers, params=params).json()["id"]
#         print(site_id)
#         self.site_id = site_id
