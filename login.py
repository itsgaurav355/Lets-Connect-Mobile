from firebase import firebase

# Initialize firebase
firebase = firebase.FirebaseApplication('https://test-a5e66-default-rtdb.firebaseio.com/',None)

# data = {
#     'Email':'prajapatigaurav@gmail.com'
#     ,'Password':'1234'
# }

# #post data
# #Database Name /Table Name
# firebase.post("test-a5e66-default-rtdb/Users",data)

#Get Data
result = firebase.get('test-a5e66-default-rtdb/Users','')
print(result)

#Get specific column like email or password 
for i in result.keys():
    print(result[i]['Email'])